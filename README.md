# Environment Setup

Below, you will find instructions for the basic setup steps required to run the application on your local environment. 
This involves database setup and population, package/dependency installations, and other necessary configurations.

## Database Setup

We have decomposed our dataset into two tables, `pitches` and `at_bats`, the data for which are in `/raw_data/pitches.csv` and `/raw_data/atbats.csv` respectively.
We modeled our schema, `pitch_data`, to reflect this decomposition. The two tables are linked by foreign key `ab_id`, with a 1..* cardinality (i.e. one at bat can have multiple pitches, and each pitch is associated with one single at bat). 

To create the schema and tables, run the SQL script in `/scripts/create_pitch_schema_tables.sql`, which will create the `pitch_data` schema containing tables:

* `pitch_data` (Megatable)
* `pitches`
* `at_bats` 


Now run the SQL script in `/scripts/load_pitch_data.sql`, which will populate all three tables. After insertion, the `atbats` table should have 740,390 rows and the `pitches` and `pitches_data` tables should have 2,867,154 rows.

Due to the size of the datasets, we have not uploaded the original files to GitHub. However, they can be downloaded at: https://www.kaggle.com/datasets/pschale/mlb-pitch-data-20152018. Make sure you place the downloaded files in the `/raw_data` directory.

Also, you will need to create the triggers, views, and stored procedures that are required for the site to function. They are also located under the `/scripts/` directory. Run them in the following order (after the tables have been created and populated):

* `PitcherProcedures.sql`
* `views.sql`
* `triggers.sql`

After running these scripts, your local MySQL environment should be fully set up for this application.

## Environment/Code Setup

For the client side app, we are using Python with the Django framework to visualize our data. Below you can find the required installations for Mac OS:

* Python3: `brew install python`
* Django: `pip install django`
* MySQL: `brew install mysql`
* MySQL Client: `pip install mysqlclient`


Now, activate the virtual environment by running:

`python manage.py startapp <app name>`


The app should be automatically configured to connect to your local MySQL connection; however, if any of the database connection parameters are different, you can specify them in `/app/settings.py` under: 

```
DATABASES = { 
    'default': { 
        ... 
    }
}
``` 

You can double check that the database is connected by running `python manage.py inspectdb`, which should provide you Schema information if the db is connected.

Once the app is connected to the database, we have to create and run the necessary migrations (in the root app directory):

* `python manage.py makemigrations`
* `python manage.py migrate`


Once the migrations have completed, the server can be started from the `/app` directory using:

`python manage.py runserver`

The app should now be running at `http://localhost:8000`. 
