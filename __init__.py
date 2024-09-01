
from .latent_interpolator_multi import LatentInterpolatorMulti

NODE_CLASS_MAPPINGS = {
    "Latent Interpolator Multi": LatentInterpolatorMulti,
}

WEB_DIRECTORY = "./js"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
