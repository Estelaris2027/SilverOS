# mem subcomandos: save, read, list
from system import memory
def execute(args, state):
    if not args:
        print("Uso: mem save <k> <v> | mem read <k> | mem list")
        return
    sub = args[0]
    if sub == "save":
        if len(args) < 3:
            print("Uso: mem save <clave> <valor>")
            return
        key = args[1]
        val = " ".join(args[2:])
        # intentar parsear JSON simple: si empieza con [ or { -> guardar como JSON
        try:
            import json
            if (val.strip().startswith("{") or val.strip().startswith("[")):
                val_parsed = json.loads(val)
            else:
                val_parsed = val
        except Exception:
            val_parsed = val
        memory.save(key, val_parsed)
        print("Guardado:", key)
    elif sub == "read":
        if len(args) < 2:
            print("Uso: mem read <clave>")
            return
        key = args[1]
        print(memory.read(key))
    elif sub == "list":
        print(memory.list_keys())
    else:
        print("Subcomando mem desconocido.")
