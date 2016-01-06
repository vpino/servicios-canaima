# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from info.models import Repositorio, PackageGeneric, PackageGenericEdu
from info.form import PackageGenericForm, RepositorioForm, PackageGenericEduForm

def homepage(request):

    return render_to_response('info/homeapis.html',
                              context_instance=RequestContext(request))

#View que muestra todos los repositorios
def repositorios_list(request):

    #Guardamos en el objeto repositorios todos los repositorios
    repositorios = Repositorio.objects.all()


    #Retornamos a el templates y le pasamos todas los paquetes
    return render_to_response('info/repositorios_list.html',
                                {'repositorios': repositorios,})

def repositorios_create(request):

    #Si el metodo enviado por el formulario es POST
    if request.method == 'POST':

        #Instanciamos un objeto de tipo Repositorio y le pasamos como parametros los elementos
        #que enviaron por el formulario y lo guardamos en un objeto
        form = RepositorioForm(request.POST)

        #Validamos que los datos enviados se han correctos (campos no vacios, validaciones)
        if form.is_valid():
            #Si usamos ModelForm si pasa las validaciones simplemente le decimos que
            # lo inserte en la base de datos con form.save() ya el metodo hace la instancia por si solo
            # del modelo pasado y lo inserta
            form.save()

            #retornamos a la vista de repositorios
            return redirect('repositorios_list')

    #Si los datos no fueron enviados por post
    else:
        #Instaciamos un objeto de tipo RepositorioForm
        form = RepositorioForm()

    #Retornamos al template generic_create.html y le pasamos el formulario instanciado
    return render_to_response('info/repositorios_create.html', {'form': form},
                              context_instance=RequestContext(request))

#View para modificar un paquete generic
def repositorios_edit(request, repositorio_id):
    #Usamos el metodo get_object_or_404 donde le pasamos 2 parametos el objeto del modelo y un id
    # lo guardamos en un objeto, y si no existe retornamos a la pagina de error 404
    repositorio = get_object_or_404(Repositorio, pk=repositorio_id)

    #Si el metodo enviado por el formulario es POST
    if request.method == 'POST':

        #Le pasamos los datos del form mas la instancia del objeto capturado en el metodo get_object_or_404
        form = RepositorioForm(request.POST, instance=repositorio)

        #Validamos que los datos enviados se han correctos (campos no vacios, validaciones)
        if form.is_valid():

            #Insertamos en el base de datos el registro actualizado
            form.save()

            #retornamos a la vista generic que tiene la lista de paquetes y le pasamos el id
            return redirect('repositorios_list')

    #Si los datos no fueron enviados por post
    else:
        #Instaciamos un objeto de tipo RepositorioForm y le mostramos el registro
        #capturado con el metodo get_object_or_404
        form = RepositorioForm(instance=repositorio)

    #Retornamos al template gereric_edit.html y le pasamos el formulario instanciado
    return render_to_response('info/repositorios_edit.html', {'form': form},
                              context_instance=RequestContext(request))

#View para borrar un repositorio
def repositorios_delete(request, repositorio_id):
      #Usamos el metodo get_object_or_404 donde le pasamos 2 parametos el objeto del modelo y un id
    # lo guardamos en un objeto, y si no existe retornamos a la pagina de error 404
    repositorio = get_object_or_404(Repositorio, pk=repositorio_id)

    repositorios = Repositorio.objects.all()

    #Si elimina el repo
    if repositorio.delete():

        #retornamos a la vista de la lista de repositorios
        return redirect('repositorios_list')

    else:

         return redirect('repositorios_list')

def package_generic(request):
    #Guardamos en el objeto generic todos los paquetes
    generic = PackageGeneric.objects.all()


    #Retornamos a el templates y le pasamos todas los paquetes
    return render_to_response('info/PackageGeneric.html',
                                {'generic': generic,})

def generic_create(request):
    #Si el metodo enviado por el formulario es POST
    if request.method == 'POST':

        #Instanciamos un objeto de tipo PackageGeneric y le pasamos como parametros los elementos
        #que enviaron por el formulario y lo guardamos en un objeto
        form = PackageGenericForm(request.POST)

        #Validamos que los datos enviados se han correctos (campos no vacios, validaciones)
        if form.is_valid():
            #Si usamos ModelForm si pasa las validaciones simplemente le decimos que
            # lo inserte en la base de datos con form.save() ya el metodo hace la instancia por si solo
            # del modelo pasado y lo inserta
            form.save()

            #retornamos a la vista de preguntas
            return redirect('generic')

    #Si los datos no fueron enviados por post
    else:
        #Instaciamos un objeto de tipo PackageGeneric
        form = PackageGenericForm()

    #Retornamos al template generic_create.html y le pasamos el formulario instanciado
    return render_to_response('info/generic_create.html', {'form': form},
                              context_instance=RequestContext(request))

#View para modificar un paquete generic
def generic_edit(request, package_id):
    #Usamos el metodo get_object_or_404 donde le pasamos 2 parametos el objeto del modelo y un id
    # lo guardamos en un objeto, y si no existe retornamos a la pagina de error 404
    package = get_object_or_404(PackageGeneric, pk=package_id)

    #Si el metodo enviado por el formulario es POST
    if request.method == 'POST':

        #Le pasamos los datos del form mas la instancia del objeto capturado en el metodo get_object_or_404
        form = PackageGenericForm(request.POST, instance=package)

        #Validamos que los datos enviados se han correctos (campos no vacios, validaciones)
        if form.is_valid():

            #Insertamos en el base de datos el registro actualizado
            form.save()

            #retornamos a la vista generic que tiene la lista de paquetes y le pasamos el id
            return redirect('generic')

    #Si los datos no fueron enviados por post
    else:
        #Instaciamos un objeto de tipo PackageGenericForm y le mostramos el registro
        #capturado con el metodo get_object_or_404
        form = PackageGenericForm(instance=package)

    #Retornamos al template gereric_edit.html y le pasamos el formulario instanciado
    return render_to_response('info/generic_edit.html', {'form': form},
                              context_instance=RequestContext(request))

#Vista que retorna todos los paquetes genericos  educativos
def package_generic_edu(request):

    #Guardamos en el objeto Generic todos los paquetes genericos educativos
    generic = PackageGenericEdu.objects.all()

    #Retornamos a el templates y le pasamos todas los paquetes
    return render_to_response('info/PackageGenericEdu.html',
                                {'generic': generic})

#Metodo para añadir un paquete a la lista de paquetes genericos educativos
def generic_edu_create(request):
    #Si el metodo enviado por el formulario es POST
    if request.method == 'POST':

        #Instanciamos un objeto de tipo PackageGenericEduForm y le pasamos como parametros los elementos
        #que enviaron por el formulario y lo guardamos en un objeto
        form = PackageGenericEduForm(request.POST)

        #Validamos que los datos enviados se han correctos (campos no vacios, validaciones)
        if form.is_valid():
            #Si usamos ModelForm si pasa las validaciones simplemente le decimos que
            # lo inserte en la base de datos con form.save() ya el metodo hace la instancia por si solo
            # del modelo pasado y lo inserta
            form.save()

            #retornamos a la vista de paquetes educativos
            return redirect('generic_edu')

    #Si los datos no fueron enviados por post
    else:
        #Instaciamos un objeto de tipo PackageGenericEdu
        form = PackageGenericEduForm()

    #Retornamos al template generic_edu_create.html y le pasamos el formulario instanciado
    return render_to_response('info/generic_edu_create.html', {'form': form},
                              context_instance=RequestContext(request))

#View para modificar un paquete generic educativo
def generic_edu_edit(request, package_id):
    #Usamos el metodo get_object_or_404 donde le pasamos 2 parametos el objeto del modelo y un id
    # lo guardamos en un objeto, y si no existe retornamos a la pagina de error 404
    package = get_object_or_404(PackageGenericEdu, pk=package_id)

    #Si el metodo enviado por el formulario es POST
    if request.method == 'POST':

        #Le pasamos los datos del form mas la instancia del objeto capturado en el metodo get_object_or_404
        form = PackageGenericEduForm(request.POST, instance=package)

        #Validamos que los datos enviados se han correctos (campos no vacios, validaciones)
        if form.is_valid():

            #Insertamos en el base de datos el registro actualizado
            form.save()

            #retornamos a la vista generic_edu que tiene la lista de paquetes y le pasamos el id
            return redirect('generic_edu')

    #Si los datos no fueron enviados por post
    else:
        #Instaciamos un objeto de tipo PackageGenericEduForm y le mostramos el registro
        #capturado con el metodo get_object_or_404
        form = PackageGenericEduForm(instance=package)

    #Retornamos al template generic_edu_edit.html y le pasamos el formulario instanciado
    return render_to_response('info/generic_edu_edit.html', {'form': form},
                              context_instance=RequestContext(request))
