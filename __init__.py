
from .latent_interpolator_multi import LatentInterpolatorMulti
from .latent_interpolator_sequence import LatentInterpolatorSequences
from .latent_loop import LatentLooper
from .print_latent_sequences import LatentPrinter
from .int_looper import IntLooper

NODE_CLASS_MAPPINGS = {
    "Int Looper": IntLooper,
    "Latent Interpolator Multi": LatentInterpolatorMulti,
    "Latent Interpolator Sequence": LatentInterpolatorSequences,
    "Latent Looper": LatentLooper,
    "Latent Printer": LatentPrinter,
}

WEB_DIRECTORY = "./js"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
