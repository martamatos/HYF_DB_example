# Small example for the DB class


Assuming you have the database up and running on the localhost, and you have miniconda/anaconda installed:

1. Set up the environment: `conda env create -f env.yml`
2. Modify .env.example to work for you
3. Run the app with `flask run`  in the main directory.
4. Go to 127.0.0.1:5000, ignore the login screen and go to `See data`  or `Add data` and explore.

If you want to modify a data entry, just select it in `See data`.

If you need to change any MySQL configurations, go to `config.py` on the main folder.