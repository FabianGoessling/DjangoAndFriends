# Django & Friends

![](/djangoandfriends.png)

This repo contains examples for integrating other frameworks or python packages. 
By no means is the repo complete or necessarily best-practice, instead it represents a diary of my exploration of *Django & Friends*.

In particular the repo covers:


### Vue.js
---
There are several ways to use a fully fledged frontend js library like Vue.js with Django. 
1) Separate frontend and backend. This is the go-to-way for large applications, but requires rewriting the Django Part to a REST API. Thus the django templating system cannot be used anymore.

2) Integrating a standalone vue frontend in Django templates. This approach allows to use single-file-components (SFC) for the vue side while still using Djangos views. A commonly used package is django-webpack-loader which is not maintained and adds additional dependencies. Thus, a better way of integrating vue.js is to use Djangos template system to integrate the vue cli output. A full description is given in the repo (https://github.com/EugeneDae/django-vue-cli-webpack-demo). This approach is applied to the Django&Friends repo in the folder *frontend*.

3) Integrate vue.js via CDN. This approach does not allow to use SFC and thus has to rely on Django template splitting. From my experience this can be a first step for using vue.js but is hardly maintainable. A simple example is given in the app

### bokeh & panel 
---
Integration of [bokeh](https://docs.bokeh.org/en/latest/) and [panel](https://panel.holoviz.org)
is straightforward given the respective documentation. In particular, the panel package
provides a nice [example](https://panel.holoviz.org/user_guide/Django_Apps.html).
Bokeh documentation is not as simple, but the implementation follows the same route.

Required Packages:  
* Django Channels

Django Apps:
* visualization_bokeh


#### Dash
---

#### Chart.js 
---
The visualization_chartjs app shows a simple example of integrating
[Chart.js](https://www.chartjs.org) in a Django app. Besides passing the initial data to the chart,
the app shows how to implement an AJAX POST call to your Django view and
return data to update the chart. Based on the example more complex callbacks can be easily constructed.
Asides from standard Django code this examples requires basic javascript knowledge, but don't worry
the code is straightforward and easy to understand.

 
#### REST API
---

#### GraphQL API
---


#### datatables.net
---

#### Database Visualization
---

#### Database signals
---
Django signals allow to execute specific actions on model.save()
and other methods. The example case is given in the home app, which
extends the User model with a Profile and auto-generates 
Profile instances on each save of a new User instance.


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
[Django crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/) allow to specify Django form logic and templating inside the python code, i.e.
it removes a lot of html code. The crud app shows an extended example of dynamic forms
within a Django app, combining javascript, Django crispy forms, Django formsetfactories
and dealing with foreign keys in forms.

