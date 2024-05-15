import hashlib
from celery import Celery
from config import Config

celery_app = Celery(
    "tasks",
    broker=Config.CELERY_BROKER_URL,
    backend=Config.CELERY_RESULT_BACKEND,
)


celery_app.conf.broker_url = Config.CELERY_BROKER_URL
celery_app.conf.result_backend = Config.CELERY_RESULT_BACKEND
# celery_app.conf.task_serializer = "json"
# celery_app.conf.result_serializer = "json"
celery_app.conf.update(result_expires=3600)


@celery_app.task
def calc_hash(string: str) -> str:
    """
    Задача для вычисления хэша строки.
    ### Params:
    data: str - Строка, которую нужно хэшировать.
    ### Return:
    str - Хэш строки в виде шестнадцатеричной строки.
    """
    hash_str = hashlib.sha256(string.encode()).hexdigest()
    return hash_str
