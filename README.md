# Utopia

is a geographic social network. It's meant to connect people, places and initiatives locally. Therefore it uses a geographic map as a landing page.

The scope is limited to mapping and sharing of real life data. Meetings and communication will happen face to face.

Check out our working prototype at [new.docutopia.de](https://new.docutopia.de)

## Features

* Register / Login...to create a profile and share your profile location wherever you would like to map it.

* Your Profile includes:
    * avatar (sml. profile picture)
    * offers (you would like to make)
    * needs (you would like to be satisfied)
    * free text (please add your phonenr. or mail to be reachable)

* These three types of entries you can search and/or map easily yourself:
    * Places
    * Events (temporary places)
    *  People (profiles)

Sharing of places and events does not require registration/login

HAPPY MAPPING . . . .

NAMA(P)STÉ

## Install
```
git clone https://github.com/antontranelis/utopia.git
cd utopia/
pip install -r requirements.txt
python manage.py migrate
```
## Run
```
python manage.py runserver
```
