import sys
import os
import shutil
from concurrent.futures import ThreadPoolExecutor


def file_worker(source_file, target_dir) -> None:
    file_extension = os.path.splitext(source_file)[1][1:].lower()
    destination_dir = os.path.join(target_dir, file_extension)
    os.makedirs(destination_dir, exist_ok=True)
    shutil.copy(source_file, destination_dir)


def directory_worker(source_dir, target_dir="dist") -> None:
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_file = os.path.join(root, file)
            with ThreadPoolExecutor() as executor:
                executor.submit(file_worker, source_file, target_dir)


if __name__ == "__main__":
    source_dir: str = sys.argv[1]
    target_dir: str = sys.argv[2] if len(sys.argv) > 2 else "dist"
    directory_worker(source_dir, target_dir)
