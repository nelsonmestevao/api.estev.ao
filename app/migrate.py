#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import create_app
from app.extensions.database import db

db.create_all(app=create_app())
