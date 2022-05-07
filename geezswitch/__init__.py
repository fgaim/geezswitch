"""
GeezSwitch Language Identification Library
"""

from .lang_detect_exception import LangDetectException
from .detector_factory import detect, detect_langs
from .detector_factory import DetectorFactory, PROFILES_DIRECTORY

version_info = (1, 0, 1)
__version__ = '.'.join(str(c) for c in version_info)


__all__ = (
    'version_info', '__version__',
)
