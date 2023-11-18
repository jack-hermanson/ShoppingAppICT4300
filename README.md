# ShoppingAppICT4300

Warning: This application was written and tested on Python version 3.11.5. Python 3.12 does not work. You will also need `npm`.
 
## How to Run the App Locally

To get started, clone this repository or unzip the files into a fresh folder.

This `readme.md` file, `requirements.txt`, and `run.py` should all be at the top level of the folder.

At this point, you need to create a file to store environment variables.
At the top level, alongside this `readme.md`, create a new file with the name `.env`. 

You will need to supply values for `ENVIRONMENT`, `SECRET_KEY`, and `FLASK_APP`. Do not add any other values; the database URL is only for production environments.

The secret key can be any string. To generate a secret key, you can follow the steps at this [GitHub Gist](https://gist.github.com/dehamzah/3db8fec14d19af50f7fcba2e74bdfb26), or you can just make something up.


```dotenv
ENVIRONMENT=dev
SECRET_KEY=SOMESECRETKEY
FLASK_APP=main

# production only!:
DATABASE_URL=PRODUCTIONDBURL
```

Once you have your `.env` ready, open up a terminal. These instructions assume a Mac or Unix-like environment.

You will need to create a virtual environment. This can be done by making sure you're in the top-level at the same level as this file, then running the following command in the terminal:

```sh
python3 -m venv venv
```

That will create a virtual environment called `venv`. To activate it, run the following command in the same terminal:

```sh
source venv/bin/activate
```

At this point, your prompt should have `(venv)` at the beginning.

Now, with this virtual environment activated, install the dependencies by running the following command in the same directory:

```sh
pip install -r requirements.txt
```

Now that all the dependencies are installed, we need to initialize the database by running all migrations.
Run the following command:

```sh
flask --app main db upgrade
```

At this point, the application will run, but the front-end will not function properly because it needs JavaScript libraries to be installed.

I would recommend opening a new terminal so you can keep the same directory and activated virtual environment when you are ready to start the app.

In a new terminal, `cd` into the `static` folder by executing the following command:

```sh
cd main/web/static 
```

Once you're in that folder, run the following command to install `npm` packages:

```sh
npm install
```

Once that finishes installing front-end libraries, close that terminal and go back to the other one you had open, at the top level of the directory structure, with the virtual environment activated.

If all of that worked, you are good to go.
Run the following command to start the app:

```sh
python run.py
```
