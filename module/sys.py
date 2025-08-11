import os
from system import memory
def execute(args, state):
    if not args:
        print("Uso: sys info")
        return
    if args[0] == "info":
        print("SilverOS v3.0 - Orion Mind")
        print("Usuario:", state.get("usuario"))
        print("Directorio actual:", state.get("cwd"))
        print("Memoria:", memory.summary())
        print("Comandos instalados: modules/ (ls, ai_cmd, mem, clear, ayuda, ejecutar, pyApp_install, history, sys)")
