# Blog applications

 The application is the best used with a virtual environment.

#### Input in your terminal:

 ```
  mkdir app_dir
  cd app_dir
  virtualenv -p python3 venv
  source venv/bin/activate
 ```

#### Setup application Blog:
 ```
 1.git clone https://github.com/007vict/nekidaem_test.git
 2.docker-compose up
 Input in terminal:
 3.docker-compose run web python manage.py makemigrations
 4.docker-compose run web python manage.py migrate
 5.docker-compose run web python manage.py createsuperuser
 6.sign in admin site and create your new post
 ```
#### Setting for function the 'send email to subscribers' need to change in settings.py:
 ```
 EMAIL_HOST = 'smtp.your_host'
 EMAIL_HOST_USER = 'your_user'
 EMAIL_HOST_PASSWORD = 'your_password'
 EMAIL_PORT = your_host_number_port
 ```