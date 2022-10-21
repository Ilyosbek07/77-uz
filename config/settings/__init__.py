from .base import *


if env.str('ENVIRONMENT', 'dev') == 'dev':
    try:
        from .local_settings import *
    except ModuleNotFoundError:
        pass
elif env.str('ENVIRONMENT') == 'prod':
    from .prod import *
