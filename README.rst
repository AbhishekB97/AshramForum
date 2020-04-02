<<<<<<< HEAD
django-simple-forum:

=======
>>>>>>> 41db00d6c0568ffdb5c274648beb629ba282c376
Introduction:
=============

`django simple forum`_ is a discussion board where people with similar interests can create and discuss various topics. You can also mention any particpant those are involved in the repsective topic in the comment. You can also receive email notifications when there is an update in the topic, when you follow the topic.


Modules used:

<<<<<<< HEAD
    * 3.7 >= Python  >= 3.0
=======
    * Python  == 3.7
>>>>>>> 41db00d6c0568ffdb5c274648beb629ba282c376
    * Django  = 3.0
    * JQuery  >= 1.7
    * Microurl >=3.6.1
    * Boto == 2.40.0
    * Sendgrid == 2.2.1
    * django-ses-gateway

Installation Procedure
======================

1. Install django-simple-forum using the following command::

    pip install django-simple-forum

            (or)

    git clone git://github.com/micropyramid/django-simple-forum.git

    cd django-simple-forum

    python setup.py install

2. Add app name in settings.py::

    INSTALLED_APPS = [
       '..................',
       'compressor',
       'django_simple_forum',
       '..................'
    ]

3. After installing/cloning, add the following details in settings file to send emails notifications::

    # AWS details

    AWS_ACCESS_KEY_ID = "Your AWS Access Key"

    AWS_SECRET_ACCESS_KEY = "Your AWS Secret Key"

                or

    SG_USER = "Your Sendgrid Username"
    SG_PWD = "Your Sendgrid Password"

4. Use virtualenv to install requirements::

    pip install -r requirements.txt

<<<<<<< HEAD
=======

>>>>>>> 41db00d6c0568ffdb5c274648beb629ba282c376
