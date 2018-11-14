# Posts and Comments
Using the tutorial from the first day of Django, we're going to create an app where we can view posts and comments

## Release 0
Set up your Django project and app. Ensure that they are registered with each other

## Release 1
Create your routes in `urls.py`. Specifically, I want to see:
- `/posts`: All posts
- `/posts/:id`: Information about a post with a specific ID number. I can also see all the comments on a post on this page

## Release 2
Set up your database with your two models and migrate them into your database. Specifically, I want a `Post` to have a `title` and `body`. A `Comment` should have a `body` and belong to a `Post`

## Release 3
Populate the database using the Django shell. Create 3 posts with 2 comments associated with them.

## Release 4
Create your views using helper methods and generic, Class-Based Views
