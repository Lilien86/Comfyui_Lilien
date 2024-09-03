import torch

class LatentPrinter:
    CATEGORY = "lauger_NP"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "latent_batch": ("LATENT",),  # Prend un lot de latents en entrée
            },
        }

    RETURN_TYPES = ("LATENT",)  # Retourne le premier latent
    FUNCTION = "print_latents"

    def print_latents(self, latent_batch):
        samples = self._extract_samples(latent_batch)

        for idx, sample in enumerate(samples):
            print(f"Latent {idx + 1}:")
            print(sample)

        # Retourne le premier latent du batch
        first_latent = {"samples": samples[0].unsqueeze(0)}
        return (first_latent,)

    def _extract_samples(self, latent_batch):
        if not isinstance(latent_batch, dict):
            raise TypeError("Latent batch should be a dictionary containing 'samples' key")

        samples = latent_batch.get("samples")
        if samples is None:
            raise KeyError("'samples' key is missing in the latent batch dictionary")
        
        return samples
