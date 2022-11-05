import os

from project.config import DATA_PATH
from project.logger.project_logging import logger
from project.module1.add_numbers import add_numbers
from project.module1.read_file import read_file
from project.module2.subract_numbers import subtract_numbers


def main():
    logger.info('Started sample project!')

    logger.info(f'Current working directory: "{os.getcwd()}"')

    file_content = read_file(f'{DATA_PATH}/sample_file.txt')
    logger.info(f'File content: {file_content}')

    res = add_numbers(1, 2)
    logger.info(f'Addition result: {res}')

    res = subtract_numbers(1, 2)
    logger.info(f'Subtraction result: {res}')


if __name__ == '__main__':
    main()
