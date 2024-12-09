kill -9 $(lsof -i:8001 -t) 2> /dev/null
python3 manage.py runserver 0.0.0.0:8001