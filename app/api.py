#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import create_app, VERSION, DESCRIPTION


app = create_app()


@app.route("/")
def index():
    """Welcome entry point"""
    return {
        "name": "api.estev.ao",
        "description": DESCRIPTION,
        "version": VERSION
    }


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
