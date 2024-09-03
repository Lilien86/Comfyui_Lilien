import torch

class IntLooper:
    CATEGORY = "lauger_NP"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "initial_value": ("INT", {
                    "default": 0,
                    "min": 0,
                    "display_name": "Initial Value"
                }),
                "index": ("INT", {
                    "default": 0,
                    "min": 0,
                    "display_name": "Index"
                }),
                "max_value": ("INT", {
                    "default": 10,
                    "min": 1,
                    "display_name": "Max Value"
                }),
            },
        }

    RETURN_TYPES = ("INT",)
    FUNCTION = "increment_int"

    def increment_int(self, initial_value, index, max_value):
        """
        Incrémente un entier en boucle basé sur l'index et renvoie la nouvelle valeur.

        Parameters:
        - initial_value (int): La valeur initiale à incrémenter.
        - index (int): L'index qui détermine le montant d'incrémentation.
        - max_value (int): La valeur maximale à atteindre avant de recommencer.

        Returns:
        - tuple: Contient la nouvelle valeur entière après incrémentation.
        """
        # Validation des entrées
        if not isinstance(initial_value, int):
            raise TypeError("La valeur initiale doit être un entier.")
        
        if not isinstance(index, int):
            raise TypeError("L'index doit être un entier.")
        
        if not isinstance(max_value, int):
            raise TypeError("La valeur maximale doit être un entier.")

        # Calcul de la nouvelle valeur en boucle
        incremented_value = (initial_value + index) % max_value
        
        # Retourner la nouvelle valeur entière dans un tuple
        return (incremented_value,)
