from project.logger.project_logging import logger


def subtract_numbers(x: int, y: int) -> int:
    return x - y


if __name__ == '__main__':
    logger.info('Running subtract_numbers')
