# README.md

## Taste Monger (Skanus meniu)

A Food Review/Rating Application for Employees of an Office on the Everyday Meal they get from different Restaurants.

## Environment Preparation

1. Make sure `venv` or any virtual environment is installed. If not, try, `sudo apt-get install python3-venv` and also,
   please make sure the pip is upgraded to the latest version. If Not, then try `pip install ---upgrade pip`
2. If you are using `venv` make sure to activate it via `source venv/bin/activate`.
3. Make sure to install the exact same version of the modules docked in `requirements.txt`.
   Type `pip install -r requirements.txt` on terminal and you are ready to go.

## Database and Initial Migrations

1. An SQLite database is added in the project so as to run it without setting up database, admin or other stuff. For
   this,
    1. Use `sabbir` and `123456` as admin username and password respectively.
2. Run `python manage.py makemigrations` and `python manage.py migrate` to take the make the migrations if setting up
   new db.
3. Run `python manage createsuperuser` for creating Admin.

## Creating `.ENV` File

Create a .env file as it is being ignored

```json
CRON_HOUR=23
CRON_MINUTE=58
```

## Setting Up Cronjobs

`apscheduler` is used for scheduled tasks. It is used for fetching news by sources, scanning news titles for search
keywords by users and sending emails.

All the tasks can be found in `../menu_app/tasks.py` module. The interval can be set from the `.env`file accordingly.

## Running the Application

1. Make sure db is prepared and `.env` is set up.
2. Run `python manage.py runserver localhost:5003 --noreload` to run the application with all the cronjobs and without
   restart.

## Database Population Scrips

There are several custom commands for easily populating the database. All associated scripts can be found
`./menu_app/management/commands` dir, and can be modified according to need.

1. `../menu_app/management/commands/populate_users.py` - for populating fake users.
2. `../menu_app/management/commands/populate_restaurants.py` - for populating fake Restaurants.
3. `../menu_app/management/commands/populate_menu.py` - for populating fake Menu.
4. `../menu_app/management/commands/populate_votes.py` - for populating fake Votes.

## Application APIs

1. All the APIs can be accessible from HTTP Client.
2. All the Insomnia Sample API Request-Response collections are saved in the `./insomnia_docs` .NB. To Load the file,
   download Insomnia( HTTP Client Tools) from [here](https://insomnia.rest/download).

## Major Components

- `Admin Panel` - is made up of `Django Admin Panel`.
- `Application API Server` - API server for REST interface and REST Integration. `JWT` has been used for authorized API
  calls for endpoints.
- `Cronjobs` - Cron job is added to update the leaderboard by the end of the Day.
    - `Update the Leaderboard` - Though Leaderboard is updated after every leaderboard API call, but to set it finally,
      A cronjob is added for automatic Leaderboard update.

## Milestones Status

- [x]  Django Admin
- [x]  Django REST Framework
- [x]  Service Application APIs
    - [x]  Login
    - [x]  Register
    - [x]  Creating Restaurants
    - [x]  Creating/Uploading Menu Items, for current day and Future entries
    - [x]  Voting for the Best Menu
    - [x]  Leaderboard for Current Day Menu
- [x]  Automated Database Population Script.
- [x]  Crons
    - [x]  News Source Fetcher
- [x]  Insomnia API Docs
- [x]  README

