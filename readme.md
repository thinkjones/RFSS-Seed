# React-Flask-SQLAlchemy-SqlLite Project 

# Installation

## Env
```
brew install python
pip install --upgrade pip setuptools
sudo pip install virtualenv
pip install virtualenv
```

## Setup dev env
```
virtualenv venv --distribute
source .alias
pip install -r requirements.txt
``` 

# Client
```
cd client
npm install
```

# Running the App.
## Server
```
source .alias
python server/app.py
```

It should start with the following message:
```
^C(venv) admins-MacBook-Pro:RFSS-Seed thinkjones$ python server/app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

The React client proxies server calls to the server and the default should be `5000` if it isn't you will need to update the proxy
field in client/package.json.  `"proxy": "http://localhost:5000/"`

## Run the client
```
cd client;
npm start;
```

# Ops (Automated Tool Tasks)

## Reset DB
source .alias
python ops/reset_db.py

## Maintenance History and Health of a zip
source .alias
python ops/query_maintenance.py <aircraft_id>

## Mark Maintenance Item of a zip completed
source .alias
python ops/maintenance_completed.py <maintenance_id>