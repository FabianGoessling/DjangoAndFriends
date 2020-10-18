# Django & Friends

This repo contains examples for possible integrations of other
python frameworks and general how-to-does for Django extension. 
The repos is by means complete nor necessarily best-practice.
Instead it evolves step by step as I dig deeper into the Django Framework.
In particular the repo covers (or will cover):

### bokeh & panel 
Integration of [bokeh](https://docs.bokeh.org/en/latest/) and [panel](https://panel.holoviz.org)
is straightforward given the respective documentation. In particular, the panel package
provides a nice [example](https://panel.holoviz.org/user_guide/Django_Apps.html).
Bokeh documentation is not as simple, but the implementation follows the same route.

Required Packages:  
* Django Channels

Django Apps:
* bokeh_app
* panel_app
* ipyaggrid_app


#### Dash

#### Chart.js 
#### REST API
#### GraphQL API
#### datatables.net
#### Database Visualization
#### Database signals
Extends the User model with a Profile and auto-generates 
Profile Instances on each save of a new User instance.
#### Django Messaging Framework
#### Prefect Integration
#### Celery Integration
Celery can be used to run background tasks while the Django Server is not blocked. 
I.e. a request can trigger an expensive calculation but return the response immediately.
The example in the current repo is based on the Celery Official Documentation and Stackoverflow.
The 
To interact between the Django Server and the Celery workers a message Broker, i.e. [Redis](https://redis.io) is required. 
After downloading Redis simple change to the folder and run a '''make'''.
To run the celery workers we need
1) The running Django App
2) Running Redis Server
3) Running Celery Queue  
celery -A mysite worke -l info
4) Runniny Celery Beat  
celery -A mysite beat -l info


#### Bootstrap Templates
#### Django Crispy Forms

