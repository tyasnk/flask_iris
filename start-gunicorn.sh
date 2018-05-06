#!/usr/bin/env bash
gunicorn server:app -c gunicorn.py