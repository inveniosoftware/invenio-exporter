# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
# Copyright (C) 2020 Graz University of Technology.
#
# invenio-exporter is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Module tests."""

from flask import Flask

from invenio_exporter import InvenioExporter


def test_version():
    """Test version import."""
    from invenio_exporter import __version__
    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask('testapp')
    ext = InvenioExporter(app)
    assert 'invenio-exporter' in app.extensions

    app = Flask('testapp')
    ext = InvenioExporter()
    assert 'invenio-exporter' not in app.extensions
    ext.init_app(app)
    assert 'invenio-exporter' in app.extensions
