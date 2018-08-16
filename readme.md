# AFSP-Seed Project:
**Angular -> Flask -> SQLAlchemy -> Postgres**

# Pre-requisites 
## Env
```
brew install python
pip install --upgrade pip setuptools
sudo pip install virtualenv
pip install virtualenv
```

## Pre-requisite Postgres
```
brew install postgresql
pg_ctl -D /usr/local/var/postgres start
psql then createdb afsp_seed_dev
```

## Setup dev env
```
virtualenv venv --distribute
source venv/bin/activate
pip install -r requirements.txt
``` 

# Run
```
source .alias
pg_ctl -D /usr/local/var/postgres start
python -m server/server app run
```

# LICENSE
The MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.