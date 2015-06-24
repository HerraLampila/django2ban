#django2ban

Simple authentication backend for logging invalid login attempts. 
Intended to use with something like "fail2ban". 

## Install instructions

- Add 'django2ban' to your INSTALLED_APPS

```
INSTALLED_APPS = (  
    ...  
    'django2ban',  
)  
```

- Add django2ban middleware

```
MIDDLEWARE_CLASSES = (
    ...  
    'django2ban.middlewares.ThreadLocal.ThreadLocalMiddleware',  
)  
```

- Add django2ban authentication backend

```
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'django2ban.backend.InvalidLoginBackend',
)
```

Make sure django2ban is the **last** authentication backend!

## Example logging

```
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'auth_format': {
            'format': "%(asctime)s {} [%(name)s]: %(message)s".
                      format(project_module.__name__),
            'datefmt': "%B %d %H:%M:%S"
        },
    },
    'handlers': {
        'auth_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(PROJECT_ROOT, 'data/', 'auth.log'),
            'formatter': 'auth_format'
        },
    },
    'loggers': {
        'django2ban': {
            'handlers': ['auth_file', ],
            'propagate': True,
            'level': 'DEBUG',
        },
    }
}
```
