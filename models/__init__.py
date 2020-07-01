"""realoading for persistence data"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

