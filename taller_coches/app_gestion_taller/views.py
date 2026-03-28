from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .models import Cliente, Coche, Servicio, CocheServicio

def lista_clientes(request):
    clientes = list(Cliente.objects.values("id", "nombre", "telefono", "email"))
    return JsonResponse(clientes, safe=False)

def detalle_cliente(request, cliente_id):
    try:
        cliente = Cliente.objects.values("id", "nombre", "telefono","email").get(id=cliente_id)
        return JsonResponse(cliente)

    except Cliente.DoesNotExist:
        return JsonResponse({"error": "Cliente no encontrado"}, status=404)

#Registrar cliente
@csrf_exempt
def registrar_cliente(request): 
    if request.method == 'POST': #Accedemos mediante un POST
        try:
            data = json.loads(request.body) #Cargamos todo lo que venga en el body
            cliente = Cliente.objects.create( #Entry (Cliente) #Le paso todos los campos
                    nombre=data['nombre'],
                    telefono=data['telefono'],
                    email=data['email']
            )
            return JsonResponse({"mensaje": "Cliente registrado con éxito","cliente_id": cliente.id}) #Si todo va bien, te devuelvo un id con un 200
        except KeyError:
                return JsonResponse({"error": "Datos incompletos"}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)

#Registrar coche
@csrf_exempt
def registrar_coche(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body) #Cargamos
            cliente = Cliente.objects.get(id=data['cliente_id'])
            coche = Coche.objects.create(
                        cliente=cliente,
                        marca=data['marca'],
                        modelo=data['modelo'],
                        matricula=data['matricula']
            )
            return JsonResponse({"mensaje": "Coche registrado con éxito", "coche_id":coche.id})
        except Cliente.DoesNotExist:
            return JsonResponse({"error": "Cliente no encontrado"}, status=404)
        except KeyError:
            return JsonResponse({"error": "Datos incompletos"}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)

#Registrar servicio
@csrf_exempt
def registrar_servicio(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            coche = Coche.objects.get(id=data['coche_id'])
            servicio = Servicio.objects.create(
                        nombre=data['nombre'],
                        descripcion=data['descripcion']
            )
            CocheServicio.objects.create(coche=coche, servicio=servicio)
            return JsonResponse({"mensaje": "Servicio registrado con éxito","servicio_id": servicio.id})
        except Coche.DoesNotExist:
            return JsonResponse({"error": "Coche no encontrado"}, status=404)
        except KeyError:
            return JsonResponse({"error": "Datos incompletos"}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)

#Buscar cliente. Te paso un cliente_id y me devuelve el cliente
@csrf_exempt
def buscar_cliente(request, cliente_id):
    if request.method == 'GET':
        try:
            cliente = Cliente.objects.values("id", "nombre", "telefono","email").get(id=cliente_id)
            return JsonResponse(cliente)
        except Cliente.DoesNotExist:
            return JsonResponse({"error": "Cliente no encontrado"}, status=404)
    return JsonResponse({"error": "Método no permitido"}, status=405)

#Buscar el coche por matricula. Te paso una matricula y me devuelves el coche que tiene esa matricula (por eso, matricula es un campo unico)
    #En este caso, me devuelve el coche y el cliente. Lo del cliente se puede quitar.
@csrf_exempt
def buscar_coche_por_matricula(request, matricula):
    if request.method == 'GET':
        try:
            coche = Coche.objects.select_related('cliente').get(matricula=matricula)
            respuesta = {
                "coche": {
                    "id": coche.id,
                    "marca": coche.marca,
                    "modelo": coche.modelo,
                    "matricula": coche.matricula,
                },
                "cliente": {
                    "id": coche.cliente.id,
                    "nombre": coche.cliente.nombre,
                    "telefono": coche.cliente.telefono,
                    "email": coche.cliente.email,
                }
            }
            return JsonResponse(respuesta)
        except Coche.DoesNotExist:
            return JsonResponse({"error": "Coche no encontrado"}, status=404)
    return JsonResponse({"error": "Método no permitido"}, status=405)

#Buscar coches por cliente
@csrf_exempt
def buscar_coches_de_cliente(request, cliente_id):
    if request.method == 'GET':
        try:
            coches = list(Coche.objects.filter(cliente_id=cliente_id).values("id","marca", "modelo", "matricula"))
            return JsonResponse(coches, safe=False)
        except Cliente.DoesNotExist:
            return JsonResponse({"error": "Cliente no encontrado"}, status=404)
    return JsonResponse({"error": "Método no permitido"}, status=405)

#Buscar servicio por coche
@csrf_exempt
def buscar_servicios_de_coche(request, coche_id):
    if request.method == 'GET':
        try:
            coche = Coche.objects.get(id=coche_id)
            servicios = list(
                CocheServicio.objects.filter(coche=coche)
                .select_related('servicio')
                .values("servicio__id", "servicio__nombre", "servicio__descripcion")
            )
            respuesta = {
                    "coche": {
                        "id": coche.id,
                        "marca": coche.marca,
                        "modelo": coche.modelo,
                        "matricula": coche.matricula,
                    },
                    "servicios": servicios,
            }
            return JsonResponse(respuesta)
        except Coche.DoesNotExist:
            return JsonResponse({"error": "Coche no encontrado"}, status=404)
    return JsonResponse({"error": "Método no permitido"}, status=405)

#Nuevos endpoints (pruebas Celia)
#Actualizar cliente
@csrf_exempt
def actualizar_cliente(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            cliente = Cliente.objects.get(id=data['cliente_id'])

            cliente.nombre = data['nombre']
            cliente.telefono = data['telefono']
            cliente.email = data['email']
            cliente.save()

            return JsonResponse({"mensaje": "Cliente actualizado con éxito", "cliente_id": cliente.id})
        except Cliente.DoesNotExist:
            return JsonResponse({"error": "Cliente no encontrado"}, status=404)
        except KeyError:
            return JsonResponse({"error": "Datos incompletos"}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)

#Buscar coches por marca
@csrf_exempt
def buscar_coche_por_marca(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            coches = list(
                Coche.objects.filter(marca=data['marca']).values(
                    "id", "marca", "modelo", "matricula", "cliente_id"
                )
            )
            return JsonResponse(coches, safe=False)
        except KeyError:
            return JsonResponse({"error": "Datos incompletos"}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)

#Buscar cliente por email
@csrf_exempt
def buscar_cliente_por_email(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            cliente = Cliente.objects.values("id", "nombre", "telefono", "email").get(email=data['email'])
            return JsonResponse(cliente)
        except Cliente.DoesNotExist:
            return JsonResponse({"error": "Cliente no encontrado"}, status=404)
        except KeyError:
            return JsonResponse({"error": "Datos incompletos"}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)

