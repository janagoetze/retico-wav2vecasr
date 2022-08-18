"""
Setup script.

Use this script to install the Huggingface wav2vec ASR incremental modules for the retico framework.
Usage:
    $ python3 setup.py install
The run the simulation:
    $ retico [-h]
"""

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

exec(open("retico_wav2vecasr/version.py").read())

config = {
    "description": "The Huggingface wav2vec ASR incremental modules for the retico framework",
    "author": "Tahsin Mir Imtiaz, Ryan Whetten, Casey Kennington, Thilo Michael",
    "url": "https://github.com/retico-team/retico-wav2vecasr",
    "download_url": "https://github.com/retico-team/retico-wav2vecasr",
    "author_email": "caseykennington@boisestate.edu",
    "version": "0.1",
    "install_requires": [
        "retico-core~=0.2",
        "transformers",
        "webrtcvad",
        "pydub",
        "numpy",
    ],
    "packages": find_packages(),
    "name": "retico-wav2vecasr",
}

setup(**config)
