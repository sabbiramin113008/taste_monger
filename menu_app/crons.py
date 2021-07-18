# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 18 Jul 2021
email: sabbiramin.cse11ruet@gmail.com, sabbir@rokomari.com

"""
from apscheduler.schedulers.background import BackgroundScheduler
from .tasks import leaderboard_generation_task
from apscheduler.triggers.cron import CronTrigger


def start_job():
    leaderboard_scheduler = BackgroundScheduler()
    # leaderboard_cron = CronTrigger(hour=23, minute=58)
    leaderboard_cron = CronTrigger(hour=19, minute=42)
    leaderboard_scheduler.add_job(leaderboard_generation_task,
                                  trigger=leaderboard_cron,
                                  # "interval",
                                  # minutes=2,
                                  id='update_leaderboard',
                                  replace_existing=True)
    leaderboard_scheduler.start()
