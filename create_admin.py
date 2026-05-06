import os
import django 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'workorder_system.settings')

from django.contib.filter.auth.models.import User

if not User.object.filter(username="admin").exist():
    User.object.create_superuser("admin', 'admin@demo.com', 'admin1234")
    print("usuario creado exitosamente")
else:
    print("ya existe")

