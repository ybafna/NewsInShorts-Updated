# NewsInShorts2.0

Install the following dependencies<br>
python<br>
pip<br>
django<br>
crispy_forms<br>
<br>

Run the following commands in the "NewsInShorts" directory<br>
python manage.py makemigrations<br>
python manage.py migrate<br>
<br>
python manage.py runserver<br>
<br>
This should load the website at http://127.0.0.1/<br>
<br>
There are 2 paths available:<br>
<br>
1)/news - This loads the web applications<br>
2)/admin - This is the in-built Django Admin site. In order to access this, we need to create a new superuser using the command<br>
  python manage.py createsuperuser<br>
  Enter the details and use those details to access /admin portal<br>
  
<br>
In order to fetch the updated news, create an account on www.newsapi.org and create an API Token<br>
<br>
Create a .env file in the "NewsInShorts" directory and save the following details in it<br>
<br>
API_KEY={your_api_key}<br>

Go to views.py under "getNews" directory and uncomment the get_sources() and get_all_news() function
That'll fetch the updated news articles and sources using the API.


  
