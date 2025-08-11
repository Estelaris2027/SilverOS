import importlib.util, os
def execute(args, state):
    if not args:
        print("Uso: ejecutar <app>")
        return
    app = args[0]
    ruta = os.path.join(os.getcwd(), "apps", f"{app}.py")
    if not os.path.isfile(ruta):
        print("App no encontrada:", ruta)
        return
    spec = importlib.util.spec_from_file_location(app, ruta)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
        if hasattr(mod, "main"):
            mod.main()
        else:
            print("La app no define main()")
    except Exception as e:
        print("Error ejecutando app:", e)
