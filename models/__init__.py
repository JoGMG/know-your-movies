#!/usr/bin/python3
"""
This determines which storage type is used
based on the environment variable `KYM_STORAGE`.
"""
from models.storage_types.file_storage import FileStorage
from models.storage_types.db_storage import DBStorage
import os

storage = DBStorage() if os.getenv(
    'KYM_STORAGE') == 'db' else FileStorage()
"""
Toggles between storage types based on
environment variable `KYM_STORAGE`.

- If `KYM_STORAGE` = `db`, it uses database storage.
- Else, it uses file storage.
"""
storage.load()
