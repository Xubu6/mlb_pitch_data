# Environment Setup

Below, you will find instructions for the basic setup steps required to run the application on your local environment. 
This involves database setup and population, package/dependency installations, and other necessary configurations.

## Database Setup

We have decomposed our dataset into two tables, `pitches` and `at_bats`, the data for which are in `/raw_data/pitches.csv` and `/raw_data/atbats.csv` respectively.
We modeled our schema, `pitch_data`, to reflect this decomposition. The two tables are linked by foreign key `ab_id`, with a 1..* cardinality (i.e. one at bat can have multiple pitches, and each pitch is associated with one single at bat). To create the schema and tables, run the SQL script in `/scripts/create_pitch_schema_tables.sql`, which will create the `pitch_data` schema, the megatable `pitch_data.pitch_data`, and tables `pitches` and `at_bats`. 

Once the schema and tables have been created, the data will be loaded from the two .csv files. Run the SQL script in `/scripts/load_pitch_data.sql`, which will populate all three tables. After insertion, the `atbats` table should have 740,390 rows and the `pitches` and `pitches_data` tables should have 2,867,154 rows.

Due to the size of the datasets, we have not uploaded the original files to GitHub. However, they can be downloaded at: https://www.kaggle.com/datasets/pschale/mlb-pitch-data-20152018. Make sure you place the downloaded files in the `/raw_data` directory.

After running the two scripts, your local MySQL environment should be fully set up for this application.

## Environment/Code Setup

For the client side app, we are using Python with the Django framework to visualize our data. Below you can find the required installations for Mac OS:

* Python3: `brew install python`
* MySQL: `brew install mysql`
* MySQL Client: `pip install mysqlclient`


The app should be automatically configured to connect to your local MySQL connection; however, if any of the database connection parameters are different, you can specify them in `/app/settings.py` under `DATABASES = { 'default': { ... }}`. Once the app is connected to the database, we have to create and run the necessary migrations (in the root app directory):

* python manage.py makemigrations
* python manage.py migrate


Once the migrations have completed, the server can be started using:

`python manage.py runserver`


The app should now be running at `http://localhost:8000`. 
