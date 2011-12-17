##Django Twitter App Shell (or dtas)

There has been plenty of times I just wanted to fire up a quick Twitter app to scrape a search, find out some information or test some new idea. Each time however I had to reengineer a previous version of a Twitter app, and that usually ended up with me losing motivation. I'm recently into Django (due to the ease-of-use of Heroku), and decided to create a Twitter App Shell for Django.

##What?

So basically, it allows you to focus on setting up a quick Twitter app instead of having to work on reinventing the wheel in terms of setting up the OAuth authentication flows.

##How to use it

Prequisites:

This was built on Python 2.7 and Django 1.3. The latest version of python-twitter must also be downloaded. On OS X, you simply run "easy_install python-twitter".

1) Download the files. Go to where manage.py is located and run "python manage.py syncdb".
2) Assuming you have created your Twitter app, go to "settings.py" and add your keys.
3) Finally run "python manage.py runserver" and you are good.

##Acknowledgements

Raphael Cruzeiro has a great tutorial on how to create the flow. Some of the code is borrowed from that post.
http://raphaelcruzeiro.com/blog/2011/07/22/integrating-a-python-application-with-twitter/

##Plans

I probably want to make a more full-fledged example for people wanting to make a Twitter application with Django to explain more of what happens in the background with the tokens.
