from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from info.models import Repositorio, PackageGeneric, PackageGenericEdu


class RepositorioResource(ModelResource):
    class Meta:
        #Query que va a mostarar la api
        queryset = Repositorio.objects.all()
        #El limite de registro que tendra la api, en este caso es 0 infinitos
        limit = 0
        #Nombre por el cual van acceder a la api
        resource_name = 'repositorios'
        #Metodos que va a permitir la api
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        always_return_data = True
        authorization = Authorization()

class PackageGenericResource(ModelResource):
    class Meta:
        #Query que va a mostarar la api
        queryset = PackageGeneric.objects.all()
        #El limite de registro que tendra la api, en este caso es 0 infinitos
        limit = 0
        #Nombre por el cual van acceder a la api
        resource_name = 'paquetes-generic'
        #Metodos que va a permitir la api
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        always_return_data = True
        authorization = Authorization()

class PackageGenericEduResource(ModelResource):
    class Meta:
        queryset = PackageGenericEdu.objects.all()
        limit = 0
        resource_name = 'paquetes-generic-edu'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        always_return_data = True
        authorization = Authorization()
