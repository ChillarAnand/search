## Setup

Install elasticsearch>=5.0

Clone repository

```
git clone https://github.com/ChillarAnand/search.git
```

Install requirements

```
cd search && pip install -r requirements.txt
```

Start server

```
python manage.py migrate
python manage.py runserver --settings=settings.local
```

-----

If you are using ubuntu/ansible, you can onliner below to setup.

```
sh -c "$(wget https://raw.githubusercontent.com/ChillarAnand/search/master/scripts/setup.sh -O -)"
```
