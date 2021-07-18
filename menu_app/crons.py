# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 18 Jul 2021
email: sabbiramin.cse11ruet@gmail.com, sabbir@rokomari.com

"""
import os

from apscheduler.schedulers.background import BackgroundScheduler
from .tasks import leaderboard_generation_task
from apscheduler.triggers.cron import CronTrigger


def start_job():
    from dotenv import load_dotenv
    load_dotenv()
    leaderboard_scheduler = BackgroundScheduler()
    CRON_HOUR = int(os.getenv('CRON_HOUR', 23))
    CRON_MINUTE = int(os.getenv('CRON_MINUTE', 58))

    leaderboard_cron = CronTrigger(hour=CRON_HOUR, minute=CRON_MINUTE)
    leaderboard_scheduler.add_job(leaderboard_generation_task,
                                  trigger=leaderboard_cron,
                                  # "interval",
                                  # minutes=2,
                                  id='update_leaderboard',
                                  replace_existing=True)
    leaderboard_scheduler.start()
