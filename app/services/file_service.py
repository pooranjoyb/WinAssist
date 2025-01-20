import os
import shutil

class FileService:
    def __init__(self, root_dir="."):
        self.root_dir = root_dir

    def list_files(self):
        return os.listdir(self.root_dir)

    def copy_file(self, src, dest):
        shutil.copy(src, dest)
        return f"File {src} copied to {dest}"

    def move_file(self, src, dest):
        shutil.move(src, dest)
        return f"File {src} moved to {dest}"

    def delete_file(self, file_path):
        os.remove(file_path)
        return f"File {file_path} deleted"

    def rename_file(self, old_name, new_name):
        os.rename(old_name, new_name)
        return f"File {old_name} renamed to {new_name}"
