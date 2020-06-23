#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A short and simple redirecting service"""
from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy

from app import create_app

__version__ = "0.1.0"

app = create_app()


@app.route("/")
def index():
    """Welcome entry point"""
    return {
        "name": "api.estev.ao",
        "description": __doc__,
        "version": __version__
    }


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
