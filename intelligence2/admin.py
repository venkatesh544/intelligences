from django.contrib import admin

# Register your models here.
from intelligence2.models import Python, Java,  Save, Intel

admin.site.register(Python)
admin.site.register(Java)
admin.site.register(Save)
admin.site.register(Intel)