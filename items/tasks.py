from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.management import call_command


import requests,datetime
from django.utils import timezone

logger = get_task_logger(__name__)


@shared_task
def checking_tasks():
	logger.info("Checking if tasks are running ")


@shared_task
def update_our_model():
    call_command("update_database", )
