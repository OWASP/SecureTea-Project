"""Docstring."""
import json


def get_creds():
    """Docstring."""
    try:
        with open('conf.json') as f:
            creds = json.load(f)
            return creds
    except Exception:
        return False
