# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
# Copyright (C) 2020 Graz University of Technology.
#
# invenio-exporter is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio module that adds Exporter programmatic API."""

from flask_babelex import gettext as _

from . import config


class InvenioExporter(object):
    """invenio-exporter extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)
        app.extensions['invenio-exporter'] = self

    def init_config(self, app):
        """Initialize configuration."""
        for k in dir(config):
            if k.startswith('INVENIO_EXPORTER_'):
                app.config.setdefault(k, getattr(config, k))
