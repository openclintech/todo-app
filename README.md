# todo-app
This repository hosts all the files for deploying a simple web app to Google Cloud. 

# Motivation
I actually built quite a few web apps in the last year - namely using Streamlit to avoid learning how to do front-end development. However, I figured it's time to learn it so I can customize the end-user experience a bit more, but also wanted to figure out the following:
1. Learn a Python framework for web apps - Flask, Django, or FastAPI
2. Learn the minimum set of requirements to deploy a web app, end-to-end, so it's accessible publicly
3. Learn how to deploy web apps on Google Cloud

## Surprisingly, it wasn't very difficult. Some highlights:
1. I chose FastAPI as my framework because it seems to be the cool kid on the block with its super-fast performance, but also because of its swagger docs that are generated automatically. It took about 20 minutes to write the todo web app using FastAPI. 
2. I used Jinja templates with FastAPI for my front-end. Super basic, nothing fancy. Took another 10 minutes to figure that out. 
3. I deployed the web app locally, just to test it out. Found some bugs and learned more about local deployment of these apps. Spent another 15 minutes here. 
4. I created a new project on Google Cloud and used their App Engine cloud service to deploy my web app. Setup took around 10 minutes. Fairly straightforward using their SDK. 
5. Embedded the functioning web app to my personal website to make the URLs easier to navigate. 

Things are always harder until you actually try it. I avoided this for awhile because there was so much technical jargon I just didn't understand. If you've been wanting to learn something new, but afraid to try it out, take this as a sign to go for it! It's easier than you might think!

## Check it out
Here's the link to my to-do list web app https://www.briankfung.com/todo. It's accessible to everyone and everyone will see each other's tasks. You can find all the code for this simple app at OpenClinTech: https://github.com/openclintech/todo-app.
