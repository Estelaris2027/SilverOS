import os, importlib, time
from system import memory

# Runtime state
state = {
    "usuario": "invitado",
    "cwd": os.getcwd(),
    "history": []
}

def bootstrap():
    # Cargar memoria persistente
    memory.load_all()
    print("Kernel cargado. Memoria disponible:", memory.summary())

def prompt():
    user = state.get("usuario", "invitado")
    cwd = state.get("cwd", os.getcwd())
    return f"{user}@SilverOS3:{cwd}$ "

def run():
    while True:
        cmdline = input(prompt()).strip()
        if not cmdline:
            continue
        state["history"].append(cmdline)
        partes = cmdline.split()
        cmd = partes[0]
        args = partes[1:]

        # Comandos internos rápidos
        if cmd in ("salir","exit"):
            print("Apagando SilverOS...")
            break
        if cmd == "cd":
            cambiar_dir(args)
            continue

        # intentar cargar modulo de modules/
        mod = cargar_modulo(cmd)
        if mod:
            try:
                mod.execute(args, state)
            except Exception as e:
                print("Error al ejecutar comando:", e)
        else:
            print(f"Comando no reconocido: {cmd}")

def cambiar_dir(args):
    if not args:
        print("Uso: cd <ruta>")
        return
    ruta = args[0]
    if os.path.isdir(ruta):
        state["cwd"] = os.path.abspath(ruta)
    else:
        print("Directorio no válido:", ruta)

def cargar_modulo(nombre):
    try:
        return importlib.import_module(f"modules.{nombre}")
    except Exception:
        return None
