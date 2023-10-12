from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context, loader

def mi_vista(request):
    return HttpResponse('<h1>Hola, bienvenido a mi pagina!!!</h1>')

def otra_vista(request):
    fecha = datetime.now()
    return HttpResponse(f'<h3>{fecha}</h3>')

# def saludo(request, nombre, apellido):
#     nombre_completo = nombre + ' ' + apellido
#     return HttpResponse(f'Hola {nombre_completo}!!!') 

def saludo(request, nombre_completo):
    return HttpResponse(f'Hola {nombre_completo}!!!') 

def mi_primer_template(request):
    
    datos = {
        'nombre': 'Pepe',
        'apellido': 'Grillo',
        'numeros': [1,2,3]
    }
    
    # v1
    # archivo = open(r'C:\Users\cdbia\Desktop\47775\primer-django\templates\mi_template.html', 'r')
    # template = Template(archivo.read())
    # archivo.close()
    
    # contexto = Context(datos)
    # template_renderizado = template.render(contexto)


    # v2
    template = loader.get_template('mi_template.html')
    template_renderizado = template.render(datos)
    
    return HttpResponse(template_renderizado)