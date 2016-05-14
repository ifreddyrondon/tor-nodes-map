from django.core.management import call_command
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(minute='*/180')),  # every 3h
    name="task_download_latest_tor_nodes",
    ignore_result=True
)
def some_task():
    call_command('get_tor_nodes_data')
    logger.info("Downloaded latest tor nodes")
