from enum import Enum
from pathlib import Path
from definitions import ROOT_DIR
from typing import Union


class DataFolder(Enum):
    APP_DATA = './dionysus_app/app_data/'
    CLASS_DATA = APP_DATA + 'class_data'
    CLASS_REGISTRY = APP_DATA + 'class_registry.index'
    IMAGE_DATA = APP_DATA + 'image_data'

    @staticmethod
    def generate_rel_path(path: str) -> Path:
        if not path:
            return Path.cwd()

        path_parts = path.split('/')
        path_parts.insert(0, ROOT_DIR)
        return Path(*path_parts).resolve()
