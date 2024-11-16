import json
import os


archivo_json = 'tareas.json'


def inicializar_json():
    if not os.path.exists(archivo_json):
        with open(archivo_json, 'w') as f:
            json.dump([], f)

def obtener_tareas():
    inicializar_json()
    with open(archivo_json, 'r') as f:
        tareas = json.load(f)
    return tareas


def agregar_tarea(descripcion):
    inicializar_json()
    tareas = obtener_tareas()
    nueva_tarea = {
        "id": len(tareas) + 1,
        "descripcion": descripcion,
        "completada": False
    }
    tareas.append(nueva_tarea)
    with open(archivo_json, 'w') as f:
        json.dump(tareas, f)


def eliminar_tarea(id_tarea):
    inicializar_json()
    tareas = obtener_tareas()
    tareas = [tarea for tarea in tareas if tarea['id'] != id_tarea]
    with open(archivo_json, 'w') as f:
        json.dump(tareas, f)

def marcar_completada(id_tarea):
    inicializar_json()
    tareas = obtener_tareas()
    for tarea in tareas:
        if tarea['id'] == id_tarea:
            tarea['completada'] = True
    with open(archivo_json, 'w') as f:
        json.dump(tareas, f)
