
# Installation:
1) Install `telethone` and `django`
2) Create at `testarm/adm/parser` file `settings.py`
With api_id and api_hash at `https://my.telegram.org/auth?to=apps`

3) Login in telegram with dev account
```
python .\testarm\adm\parser\parser.py
```

4) Get `settings.py` for django
5) `python manage.py makemigrations` and `python manage.py migrate`
6) Run