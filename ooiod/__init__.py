"""
OOIOD
=====
Provides
  1. Tools for authenticating with Azure and moving data from OOI into Azure Open Datasets

Available subpackages
---------------------
secrets
    Functions for working with the secrets files and authentication.
blobs
    Functions for working with blobs in ooiopendata.
"""
from . import secrets
from . import blobs
