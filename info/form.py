from django import forms
from info.models import Repositorio, PackageGeneric, PackageGenericEdu
from django.utils.translation import ugettext_lazy as _

#Con ModelForm
class RepositorioForm(forms.ModelForm):
    class Meta:
        #Le pasamos el modelo al cual le va hacer el formulario
        model = Repositorio
        #
        widgets={"Nombre":forms.TextInput(attrs={'placeholder':'nombre del repo','name':'nombre',
                                               'id':'Nombre',
                                               'class':'validate'}),

                 'Url':forms.TextInput(attrs={'placeholder': 'url del repositorio', 'name': 'url',
                                              'id': 'url',
                                              'class': 'validate'})
                 }
        labels = {
            'Nombre': _('Nombre del Paquete'),
            'Url': _('Url'),
        }
        #Le pasamos que campos del modelo va a crear
        fields = "__all__"

#Con ModelForm
class PackageGenericForm(forms.ModelForm):
    class Meta:
        #Le pasamos el modelo al cual le va hacer el formulario
        model = PackageGeneric
        #
        widgets={"Nombre":forms.TextInput(attrs={'placeholder':'Paquete','name':'nombre',
                                               'id':'Nombre',
                                               'class':'validate'}),
                 }
        labels = {
            'Nombre': _('Nombre del Paquete'),
        }
        #Le pasamos que campos del modelo va a crear
        fields = "__all__"

class PackageGenericEduForm(forms.ModelForm):
    class Meta:
        #Le pasamos el modelo al cual le va hacer el formulario
        model = PackageGenericEdu
        #
        widgets={"Nombre":forms.TextInput(attrs={'placeholder':'Paquete','name':'nombre',
                                               'id':'Nombre',
                                               'class':'validate'}),
                 }
        labels = {
            'Nombre': _('Nombre del Paquete'),
        }
        #Le pasamos que campos del modelo va a crear
        fields = "__all__"
