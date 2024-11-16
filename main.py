import tkinter as tk
from tkinter import messagebox
from json_manager import agregar_tarea, obtener_tareas, eliminar_tarea, marcar_completada


def agregar_tarea_gui():
    descripcion = entry_tarea.get()
    if descripcion:
        agregar_tarea(descripcion)
        actualizar_lista()
        entry_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Debe ingresar una tarea")

def eliminar_tarea_gui(id_tarea):
    eliminar_tarea(id_tarea)
    actualizar_lista()

def marcar_completada_gui(id_tarea):
    marcar_completada(id_tarea)
    actualizar_lista()

def actualizar_lista():
  
    for widget in frame_lista.winfo_children():
        widget.destroy()
    

    tareas = obtener_tareas()
    
    for tarea in tareas:
        id_tarea = tarea['id']
        descripcion = tarea['descripcion']
        completada = tarea['completada']
        
        tarea_frame = tk.Frame(frame_lista, bg="#f0f0f0", padx=10, pady=5)
        tarea_frame.pack(fill='x', pady=5, padx=10)
        
        estado = "Completada" if completada else "Pendiente"
        
        etiqueta = tk.Label(tarea_frame, text=f"{descripcion} - {estado}", width=40, anchor="w", bg="#f0f0f0", font=("Arial", 12))
        etiqueta.pack(side="left")
        
        if not completada:
            boton_completar = tk.Button(tarea_frame, text="Completar", command=lambda id=id_tarea: marcar_completada_gui(id), bg="#4CAF50", fg="white", font=("Arial", 10), relief="solid", bd=2)
            boton_completar.pack(side="right", padx=5)
        
        boton_eliminar = tk.Button(tarea_frame, text="Eliminar", command=lambda id=id_tarea: eliminar_tarea_gui(id), bg="#F44336", fg="white", font=("Arial", 10), relief="solid", bd=2)
        boton_eliminar.pack(side="right")


ventana = tk.Tk()
ventana.title("Gestor de Tareas")
ventana.geometry("500x500") 
ventana.configure(bg="#e0e0e0")


frame_entrada = tk.Frame(ventana, bg="#e0e0e0", pady=10)
frame_entrada.pack(fill='x', padx=20)


frame_entry = tk.Frame(frame_entrada, bg="#e0e0e0")
frame_entry.pack(side="left", padx=5)


entry_tarea = tk.Entry(frame_entry, width=30, font=("Arial", 14), bd=2, relief="solid")
entry_tarea.pack()

boton_agregar = tk.Button(frame_entrada, text="Agregar tarea", command=agregar_tarea_gui, bg="#2196F3", fg="white", font=("Arial", 12), relief="solid", bd=2)
boton_agregar.pack(side="left", padx=5)


frame_lista = tk.Frame(ventana, bg="#e0e0e0", pady=10)
frame_lista.pack(fill='both', expand=True, padx=20)


actualizar_lista()


ventana.mainloop()
