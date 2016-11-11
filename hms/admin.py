from django.contrib import admin
from hms.models import Disease,Location,Hospital
# Register your models here.

admin.site.register([Disease,Location,Hospital])