from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Configurações do Django para o Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myfilms.settings')

app = Celery('myfilms')

# Carregue as configurações do Django no Celery
app.config_from_object('django.conf:settings', namespace='CELERY')

#tarefas nos módulos Django
app.autodiscover_tasks()

@app.task(bind=True, ingnore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')