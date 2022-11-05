import unittest

from project.config import DATA_PATH
from project.logger.project_logging import logger
from project.module1.read_file import read_file


class TestReadFile(unittest.TestCase):

    def test_read_file(self):
        file_path = f'{DATA_PATH}/sample_file.txt'
        logger.info(f'Reading file: "{file_path}"')
        self.assertEqual(read_file(f'{DATA_PATH}/sample_file.txt'), 'Sample file content')


if __name__ == '__main__':
    unittest.main()
