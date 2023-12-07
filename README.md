# letsbloom-assignment
RESTful API for a library with basic functionalities of CRUD

## Running the application
Download `mysite` repository and inside the repository open the terminal. Make sure Django and Django Rest Framework are pre-installed on the machine, if not 
please do so by typing these command:-
```
pip install Django
pip install djangorestframework
```
Now, in the terminal type `python manage.py runserver`.
The server will become live. Our server is hosted at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Seeding the database with mock data
Although, I have already added a few sample books to the database, you can also add books by the following method:-

In the terminal open Django's interactive shell by running `python manage.py shell` command. Within the shell, manually create instances of the model (Library) and save them to the database using Django's ORM. Here is how:-
```
>>> from myapp.models import Library
>>> Library.objects.create(name='12 Rules For Life', description='An antidote to chaos', author='Jorden Peterson', genre='Non-fiction')
```
Replace name, description, author and genre as per your book.

## Endpoint description
### Endpoint 1: Retrieve All Books
Endpoint: GET `/libraryapi/`

### Endpoint 2: Add a New Book
Endpoint: POST `/libraryapi/`
Request Body: JSON object representing the new book. For example:-
```
{
        "name": "The Silent Patient",
        "description": "Shocking psychological thriller of a woman's act of violence against her husband—and of the therapist obsessed with uncovering her motive",
        "author": "Alex Michaelides",
        "genre": "Thriller"
}
```
Note: Please don't miss the '/' at the end of endpoint because it is necessary for POST request

### Endpoint 3: Update Book Details
Endpoint: PUT `/libraryapi/{book_id}/`
Request Body: JSON object with updated book details. For example:-
```
{
        "name": "The Silent Patient",
        "description": "Shocking psychological thriller of a woman's act of violence against her husband—and of the therapist obsessed with uncovering her motive",
        "author": "Alex Michaelides",
        "genre": "Thriller/Crime"
}
```
Note: Please don't miss the '/' at the end of endpoint because it is necessary for PUT request
