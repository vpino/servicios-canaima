from django.contrib import admin
from info.models import Repositorio, PackageGeneric, PackageGenericEdu

# Register your models here.
admin.site.register(Repositorio)
admin.site.register(PackageGeneric)
admin.site.register(PackageGenericEdu)

