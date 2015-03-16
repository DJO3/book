# debone
debone is a minimal, barebones Django boilerplate with HTML/CSS/JS minification for quickly kickstarting Django projects.

### Features
- [jQuery](https://jquery.com/) 2.1.3
- [Bootstrap](http://getbootstrap.com/) 3.3.2
- [Bower](http://bower.io/) for front-end dependencies management
- [django-compressor](http://django_compressor.readthedocs.org/) 1.4 for compressing CSS and Javascript files
- [django-htmlmin](https://pypi.python.org/pypi/django-htmlmin) 0.7.0 for minifying HTML output

### Requirements
- [Bower](http://bower.io/)

### Quickstart
```
mkdir {{ project_name }} && cd {{ project_name }}
virtualenv .venv
source .venv/bin/activate
pip install django
django-admin startproject --template=https://github.com/CrimsonRay/debone/zipball/master {{ project_name }} .
pip install -r requirements.txt
cd {{ project_name }}
./manage.py runserver
```

### Configuration
Configure your database in `settings.py` and project name in `bower.json`.
