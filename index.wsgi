import os
import sys 
import sae 
import yaml
yaml.load(open('config.yaml'))
app_root = os.path.dirname(__file__) 
sys.path.insert(0, os.path.join(app_root, 'moviepre')) 
import django.core.handlers.wsgi 
os.environ['DJANGO_SETTINGS_MODULE'] = 'moviepre.settings' 
application = sae.create_wsgi_app(django.core.handlers.wsgi.WSGIHandler()) 
