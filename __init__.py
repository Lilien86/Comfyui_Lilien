
from .latent_interpolator_multi import LatentInterpolatorMulti
from .latent_interpolator_sequence import LatentInterpolatorSequences
from .get_latent_at_index import GetLatentAtIndex
from .print_latent_sequences import LatentPrinter

NODE_CLASS_MAPPINGS = {
    "Latent Interpolator Multi": LatentInterpolatorMulti,
    "Latent Interpolator Sequence": LatentInterpolatorSequences,
    "Get Latent At Index": GetLatentAtIndex,
    "Latent Printer": LatentPrinter,
}

WEB_DIRECTORY = "./js"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
