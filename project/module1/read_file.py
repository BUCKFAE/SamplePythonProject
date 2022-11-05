import os


def read_file(file_path: str) -> str:
    assert os.path.isfile(file_path), f'File "{file_path}" does not exist'
    with open(file_path, 'r') as f:
        content = f.readlines()
        assert len(content) == 1
        return content[0].strip()
