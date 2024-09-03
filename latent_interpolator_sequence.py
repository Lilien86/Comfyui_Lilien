import torch
import model_management

class LatentInterpolatorSequences:
    CATEGORY = "lauger_NP"

    def __init__(self):
        self.dtype = torch.float32
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "latent1": ("LATENT",),
                "latent2": ("LATENT",),
                "steps": ("INT", {"default": 10, "min": 2, "max": 100, "display_name": "Number of Steps"})
            },
            "optional": {
                "interpolation_algorithm": (["Linear", "Quadratic", "Cubic", "Sinusoidal", "Noise-Weighted", "Random-Weighted", "Per-Channel", "Logarithmic"], {
                    "default": "Linear",
                    "display_name": "Interpolation Algorithm"
                }),
            },
        }

    RETURN_TYPES = ("LATENT",)
    FUNCTION = "interpolate_latents"

    def interpolate_latents(self, latent1, latent2, steps=10, interpolation_algorithm="Linear"):
        sample1, sample2 = self._prepare_samples(latent1, latent2)
        latents_batch = self._generate_latent_series(sample1, sample2, steps, interpolation_algorithm)
        return (latents_batch,)

    def _prepare_samples(self, latent1, latent2):
        sample1 = self._extract_samples(latent1)
        sample2 = self._extract_samples(latent2)

        sample1 = sample1.to(device=self.device, dtype=self.dtype)
        sample2 = sample2.to(device=self.device, dtype=self.dtype)

        sample2 = self._resize_sample_if_needed(sample1, sample2)

        return sample1, sample2

    def _extract_samples(self, latent):
        if not isinstance(latent, dict):
            raise TypeError("Latents should be dictionaries containing 'samples' key")

        samples = latent.get("samples")
        if samples is None:
            raise KeyError("'samples' key is missing in the latent dictionary")
        
        return samples

    def _resize_sample_if_needed(self, sample1, sample2):
        if sample1.dim() == sample2.dim():
            sample2 = torch.nn.functional.interpolate(
                sample2, size=sample1.shape[2:], mode='nearest'
            )
        elif sample2.dim() > sample1.dim():
            sample2 = sample2.squeeze(0)
            sample2 = torch.nn.functional.interpolate(
                sample2, size=sample1.shape[2:], mode='nearest'
            )
        else:
            raise ValueError("The spatial dimensions of the samples do not match and cannot be interpolated.")
        
        return sample2

    def _generate_latent_series(self, sample1, sample2, steps, interpolation_algorithm):
        latents_series = []
        for i in range(steps):
            mixing_factor = i / (steps - 1)
            alpha = self._compute_alpha(mixing_factor, interpolation_algorithm, sample1, sample2)
            interpolated_sample = self._interpolate_samples(sample1, sample2, alpha, interpolation_algorithm)
            latents_series.append(interpolated_sample)  # Append the interpolated sample tensor to the list
        
        # Concatenate all interpolated samples along the batch dimension (dim=0)
        latents_batch = torch.cat(latents_series, dim=0)
        return {"samples": latents_batch}  # Wrap the batch tensor in a dictionary

    def _compute_alpha(self, mixing_factor, interpolation_algorithm, sample1, sample2):
        alpha = torch.tensor(mixing_factor, device=self.device, dtype=self.dtype)

        if interpolation_algorithm == "Linear":
            return alpha
        elif interpolation_algorithm == "Quadratic":
            return alpha ** 2
        elif interpolation_algorithm == "Cubic":
            return alpha ** 3
        elif interpolation_algorithm == "Sinusoidal":
            return 0.5 * (1 - torch.cos(alpha * torch.pi))
        elif interpolation_algorithm == "Noise-Weighted":
            noise = torch.rand_like(sample1)
            return (1 - alpha) * sample1 + alpha * noise
        elif interpolation_algorithm == "Random-Weighted":
            weights = torch.rand_like(sample1)
            return weights * sample1 + (1 - weights) * sample2
        elif interpolation_algorithm == "Logarithmic":
            return torch.log1p(alpha) / torch.log1p(torch.tensor(1.0, device=self.device, dtype=self.dtype))
        else:
            return alpha

    def _interpolate_samples(self, sample1, sample2, alpha, interpolation_algorithm):
        if interpolation_algorithm == "Per-Channel":
            if sample1.shape[0] == 1:  # Grayscale image (1 channel)
                return (1 - alpha) * sample1 + alpha * sample2
            else:  # Color image (multiple channels)
                alpha_red = alpha ** 2
                alpha_green = alpha ** 1.5
                alpha_blue = alpha
                return torch.stack([
                    (1 - alpha_red) * sample1[0] + alpha_red * sample2[0],
                    (1 - alpha_green) * sample1[1] + alpha_green * sample2[1],
                    (1 - alpha_blue) * sample1[2] + alpha_blue * sample2[2]
                ]).to(device="cpu", dtype=torch.float32)

        return ((1 - alpha) * sample1 + alpha * sample2).to(device="cpu", dtype=torch.float32)
