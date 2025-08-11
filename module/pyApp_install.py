import shutil, os
def execute(args, state):
    if len(args) < 1:
        print("Uso: pyApp install <archivo.py>")
        return
    archivo = args[0]
    if not os.path.isfile(archivo):
        print("Archivo no encontrado:", archivo)
        return
    dest_dir = os.path.join(os.getcwd(), "apps")
    os.makedirs(dest_dir, exist_ok=True)
    dest = os.path.join(dest_dir, os.path.basename(archivo))
    try:
        shutil.copy(archivo, dest)
        print("App instalada en apps/", os.path.basename(archivo))
    except Exception as e:
        print("Error instalando app:", e)
