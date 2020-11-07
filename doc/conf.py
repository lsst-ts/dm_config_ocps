"""Sphinx configuration file for an LSST stack package.

This configuration only affects single-package Sphinx documentation builds.
"""

from documenteer.sphinxconfig.stackconf import build_package_configs
import lsst.dm.config.ocps


_g = globals()
_g.update(build_package_configs(
    project_name='dm_config_ocps',
    version=lsst.dm.config.ocps.version.__version__))
