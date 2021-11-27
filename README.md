# NewsInShorts2.0

Install the following dependencies
python
pip
django
crispy_forms


Run the following commands in the "NewsInShorts" directory
python manage.py makemigrations
python manage.py migrate

python manage.py runserver

This should load the website at http://127.0.0.1/

There are 2 paths available:

1)/news - This loads the web applications
2)/admin - This is the in-built Django Admin site. In order to access this, we need to create a new superuser using the command
  python manage.py createsuperuser
  Enter the details and use those details to access /admin portal
  
  
  
