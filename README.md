Blog applications

The application is the best used with a virtual environment.

Input in your terminal:

mkdir app_dir
cd app_dir
virtualenv -p python3 venv
source venv/bin/activate

Setup application Blog:

1.git clone https://github.com/007vict/nekidaem_test.git
2.pip install -r requirements.txt
3.python manage.py makemigrations
4.python manage.py migrate
5.python manage.py createsuperuser
6.python manage.py runserver
7.sign in admin site and create your new post!))

Setting for send_email to subscribers change in settings.py:

EMAIL_HOST = 'smtp.your_host'
EMAIL_HOST_USER = 'your_user'
EMAIL_HOST_PASSWORD = 'your_password'
EMAIL_PORT = your_host_number_port
EMAIL_USE_TLS = True
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
