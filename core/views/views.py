from django.shortcuts import render
import requests, json

def load(request):
    productos = []
    resp = requests.get('http://127.0.0.1:8000/api/v1/productos')
    print(resp.status_code)
    if resp.status_code == 200:
        productos = resp.json()
        print(productos)
    else:
        print('Error en la busqueda')
    return render(request, 'index.html', {'productos': productos})
    

def producto(request, id):
    resp = requests.get(f'http://127.0.0.1:8000/api/v1/productos/{id}').json()
    return render(request, 'producto.html' , {"resp":resp})
