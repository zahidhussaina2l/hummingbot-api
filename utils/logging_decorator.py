import logging
import functools
import inspect

logger = logging.getLogger(__name__)

def debug_endpoint(func):
    """
    Decorator to log input args, kwargs, output, and errors for any async or sync method.
    Works for all AccountsService trading endpoints.
    """

    is_coroutine = inspect.iscoroutinefunction(func)

    @functools.wraps(func)
    async def async_wrapper(*args, **kwargs):
        name = func.__qualname__
        logger.debug(f"[CALL] {name} args={args[1:]}, kwargs={kwargs}")

        try:
            result = await func(*args, **kwargs)
            logger.debug(f"[RESULT] {name}: {result}")
            return result
        except Exception as e:
            logger.error(f"[ERROR] {name}: {str(e)}", exc_info=True)
            raise

    @functools.wraps(func)
    def sync_wrapper(*args, **kwargs):
        name = func.__qualname__
        logger.debug(f"[CALL] {name} args={args[1:]}, kwargs={kwargs}")

        try:
            result = func(*args, **kwargs)
            logger.debug(f"[RESULT] {name}: {result}")
            return result
        except Exception as e:
            logger.error(f"[ERROR] {name}: {str(e)}", exc_info=True)
            raise

    return async_wrapper if is_coroutine else sync_wrapper
