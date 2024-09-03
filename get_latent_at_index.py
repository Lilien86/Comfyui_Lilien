import torch

class GetLatentAtIndex:
    CATEGORY = "lilien/latent"

    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "latent": ("LATENT",),  # Le latent contenant plusieurs images latentes
                "index": ("INT", {
                    "default": 0,
                    "min": 0,
                    "display_name": "Index"
                }),
            },
        }

    RETURN_TYPES = ("LATENT",)
    FUNCTION = "get_latent_at_index"

    def get_latent_at_index(self, latent, index):
        """
        Cette fonction extrait un échantillon latent spécifique d'un lot d'échantillons latents.

        Parameters:
        - latent (dict): Un dictionnaire contenant une clé 'samples' avec un tenseur d'échantillons latents.
        - index (int): L'index de l'échantillon latent souhaité à extraire.

        Returns:
        - tuple: Contient un dictionnaire avec la clé 'samples' et le tenseur latent sélectionné comme valeur.
        """
        if not isinstance(latent, dict):
            raise TypeError("Le latent doit être un dictionnaire.")

        if 'samples' not in latent:
            raise KeyError("La clé 'samples' est manquante dans le dictionnaire latent.")

        samples = latent['samples']

        if samples is None:
            raise ValueError("La valeur associée à la clé 'samples' est None.")

        samples = samples.to(device=self.device)

        num_samples = samples.size(0)

        if index >= num_samples:
            raise IndexError(f"L'index spécifié {index} est hors des limites. Le nombre total de latents est {num_samples}.")

        selected_latent = samples[index].unsqueeze(0)

        result_latent = {"samples": selected_latent}

        return (result_latent,)
