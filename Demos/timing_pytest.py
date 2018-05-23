import time
import logging
import decorator


def timing(test_function):
    """
    Used as decorator to test functions
    Shows actual test time execution
    in INFO logs

    Usage:
    pytest <test_name> --log-cli-level=info
    :param test_function:
    :return:
    """
    def wrapper(func, *args, **kwargs):
        logging.basicConfig(level=logging.INFO)
        started_at = time.time()


        def log(started_at):
            elapsed = time.time() - started_at
            logging.info(f"Test {test_function.__name__},"
                         f"took {round(elapsed,3)}s to execute.")

        try:
            test_function(*args, **kwargs)
            log(started_at)
        except Exception as exception_thrown:
            log(started_at)
            raise exception_thrown

    return decorator.decorator(wrapper, test_function)
#
#
# def timing(test_function):
#     def wrapper(func, *args, **kwargs):
#         logging.basicConfig(level=logging.INFO)
#         started_at = time.time()
#         func(*args, **kwargs)
#         elapsed = time.time() - started_at
#         logging.info(f"Test {func.__name__},"
#                      f"took {round(elapsed,3)}s to execute.")
#
#     return decorator.decorator(wrapper, test_function)
