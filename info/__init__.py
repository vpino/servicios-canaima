from tastypie.api import Api
from info.resources import RepositorioResource, PackageGenericResource, PackageGenericEduResource

api_01 = Api(api_name='0.1')
api_01.register(RepositorioResource())
api_01.register(PackageGenericResource())
api_01.register(PackageGenericEduResource())

