import sys, os

activate_this = '/home/a0673218/env/bin/activate_this.py'
with open(activate_this) as f:
  exec(f.read(), {'__file__': activate_this})
sys.path.insert(0, os.path.join('/home/a0673218/domains/hexscan.ru/V3C'))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'V3C.settings')

application = get_wsgi_application()