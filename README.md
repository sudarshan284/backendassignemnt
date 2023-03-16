Hi , so this is just a small django application which is having two endpoints.
To run this application first you need to install and activate the virtaul environment.
Command to create virtual environment in linux is virtualenv <the name of your virtual environment>.
to activate it - source venv/bin/activate
AFter that run the requiremtns file.
and then run the django server using Python manage.py runserver
and then you can hit the endpoints and test it.
The models , serializers and views can be found inside the core app.
And the urls you can find inside the csvparser urls.py file.

The endpoints are - 1.  http://127.0.0.1:8000/core/upload-csv/. The rows in the CSV file will be inserted into your database table.
2. http://127.0.0.1:8000/core/sort/column_name/sort_order/, where column_name is the name of the column to sort by and sort_order is either 'asc' or 'desc'. The top 50 rows after sorting will be returned as JSON.

You can test these endpoints on the tools like postman.
