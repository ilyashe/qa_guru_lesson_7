import os
import pytest
import shutil
import zipfile

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIRECTORY = os.path.dirname(CURRENT_FILE)
PROJECT_ROOT = os.path.dirname(CURRENT_DIRECTORY)
TMP_DIR = os.path.join(PROJECT_ROOT, 'tmp')
ZIP_DIR = os.path.join(PROJECT_ROOT, 'resources')
ZIP_FILE = os.path.join(ZIP_DIR, 'archive.zip')
FILES_LIST = os.listdir(TMP_DIR)


@pytest.fixture(scope="module", autouse=True)
def create_archive():
    if not os.path.exists(ZIP_DIR):
        os.mkdir(ZIP_DIR)
    with zipfile.ZipFile(ZIP_FILE, 'w') as zf:
        for file in FILES_LIST:
            add_file = os.path.join(TMP_DIR, file)
            zf.write(add_file, os.path.basename(add_file))

    yield

    shutil.rmtree(ZIP_DIR)