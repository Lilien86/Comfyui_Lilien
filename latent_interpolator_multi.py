import torch
import model_management

class LatentInterpolatorMulti:
    CATEGORY = "lilien/latent"

    def __init__(self):
        # Initialize the data type for tensor operations
        self.dtype = torch.float32
        
        # Set the device for computations
        # If CUDA (GPU) is available, use it; otherwise, use CPU
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "latent1": ("LATENT",),
                "latent2": ("LATENT",),
            },
            "optional": {
                "interpolation_algorithm": (["Linear", "Quadratic", "Cubic", "Sinusoidal", "Noise-Weighted", "Random-Weighted", "Per-Channel", "Logarithmic"], {
                    "default": "Linear",
                    "display_name": "Interpolation Algorithm"
                }),
                "mixing_factor": ("FLOAT", {
                    "default": 0.5,
                    "min": 0.0,
                    "max": 1.0,
                    "step": 0.01,
                    "display_name": "Interpolation Factor",
                }),
            },
        }

    RETURN_TYPES = ("LATENT",)
    FUNCTION = "interpolate_latents"

    def interpolate_latents(self, latent1, latent2, interpolation_algorithm="Linear", mixing_factor=0.5):
        """
        Interpolate between two latent representations using various algorithms.

        Args:
            latent1 (dict): First latent representation.
            latent2 (dict): Second latent representation.
            interpolation_algorithm (str): The algorithm to use for interpolation.
            mixing_factor (float): The factor determining the mix between latent1 and latent2.

        Returns:
            tuple: A tuple containing a dictionary with the interpolated latent samples.

        This function performs the following steps:
        1. Validates input latents and extracts their samples.
        2. Ensures both samples are on the same device and have the same dtype.
        3. Adjusts the size of sample2 to match sample1 if necessary.
        4. Applies the chosen interpolation algorithm.
        5. Performs the actual interpolation between the two samples.
        6. Returns the interpolated result as a new latent dictionary.
        """
        if not isinstance(latent1, dict) or not isinstance(latent2, dict):
            raise TypeError("Latents should be dictionaries containing 'samples' key")

        sample1 = latent1.get("samples")
        sample2 = latent2.get("samples")

        if sample1 is None or sample2 is None:
            raise KeyError("'samples' key is missing in one of the latent dictionaries")

        sample1 = sample1.to(device=self.device, dtype=self.dtype)
        sample2 = sample2.to(device=self.device, dtype=self.dtype)

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

        # Select the interpolation algorithm
        alpha = torch.tensor(mixing_factor, device=self.device, dtype=self.dtype)
        if interpolation_algorithm == "Linear":
            pass  # No change needed; alpha is already linear
        elif interpolation_algorithm == "Quadratic":
            alpha = alpha ** 2
        elif interpolation_algorithm == "Cubic":
            alpha = alpha ** 3
        elif interpolation_algorithm == "Sinusoidal":
            alpha = 0.5 * (1 - torch.cos(alpha * torch.pi))
        elif interpolation_algorithm == "Noise-Weighted":
            noise = torch.rand_like(sample1)
            alpha = (1 - alpha) * sample1 + alpha * noise
        elif interpolation_algorithm == "Random-Weighted":
            weights = torch.rand_like(sample1)
            alpha = weights * sample1 + (1 - weights) * sample2
        elif interpolation_algorithm == "Per-Channel":
            # Check the number of channels
            if sample1.shape[0] == 1:  # Grayscale image (1 channel)
                interpolated_sample = (1 - alpha) * sample1 + alpha * sample2
            else:  # Color image (multiple channels)
                alpha_red = alpha ** 2
                alpha_green = alpha ** 1.5
                alpha_blue = alpha
                interpolated_sample = torch.stack([
                    (1 - alpha_red) * sample1[0] + alpha_red * sample2[0],
                    (1 - alpha_green) * sample1[1] + alpha_green * sample2[1],
                    (1 - alpha_blue) * sample1[2] + alpha_blue * sample2[2]
                ])
            interpolated_sample = interpolated_sample.to(device="cpu", dtype=torch.float32)
            return ({"samples": interpolated_sample},)
        elif interpolation_algorithm == "Logarithmic":
            alpha = torch.log1p(alpha) / torch.log1p(torch.tensor(1.0, device=self.device, dtype=self.dtype))

        # Default interpolation
        interpolated_sample = (1 - alpha) * sample1 + alpha * sample2

        interpolated_sample = interpolated_sample.to(device="cpu", dtype=torch.float32)
        interpolated_latent = {"samples": interpolated_sample}

        #print(f"Interpolation algorithm used: {interpolation_algorithm}")
        return (interpolated_latent,)