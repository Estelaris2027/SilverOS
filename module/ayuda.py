    def execute(args, state):
        print("""Comandos principales:
  ayuda        - muestra esta ayuda
  ls           - lista archivos (modules/ls.py)
  cd <ruta>    - cambiar directorio
  clear        - limpiar pantalla
  mem save/read/list - memoria persistente
  ai <texto>   - pregunta a la IA local
  ai start     - iniciar modo conversacional
  sys info     - info del sistema
  history      - historial de comandos
  pyApp install <archivo.py> - instala app en apps/
  ejecutar <app> - ejecuta app desde apps/
  salir        - salir de SilverOS
""")
