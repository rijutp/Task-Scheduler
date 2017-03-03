from celery.schedules import crontab
from datetime import timedelta
BROKER_URL = 'amqp://guest@localhost//'
CELERY_RESULT_BACKEND = 'amqp://guest@localhost//'
# CELERY_RESULT_DBURI = 'mysql://user:password@localhost/database'

CELERYBEAT_SCHEDULE = {
    'every-minute': {
        'task': 'task.add',
        'schedule': crontab(minute='*/1'),
        'args': (1,2),

        # 'task': 'task.mad',
        # 'schedule': crontab(minute='*/1'),
        # 'args': ('please send datas....',),
    },
     'add-every-10-seconds': {
        'task': 'task.mad',
        'schedule': 10.0,
        'args': ('http://docs.python-requests.org',),
    },
}
