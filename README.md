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
python manage.py runserver --settins=settings.local
```

**Note:** If you are using ubuntu/ansible, you can use `setup.yml` playbook in `scripts` folder to setup.
