from project.logger.project_logging import logger


def add_numbers(x: int, y: int) -> int:
    return x + y


if __name__ == '__main__':
    logger.info(f'Running add_numbers!')
