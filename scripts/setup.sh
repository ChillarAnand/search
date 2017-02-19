#! /bin/bash
set -x

cd
git clone https://github.com/ChillarAnand/search.git
cd search
ansible-playbook scripts/setup.yml -i localhost, -c local

source ~/.virtualenvs/search/bin/activate
python manage.py migrate
python manage.py runserver --settings=settings.local
