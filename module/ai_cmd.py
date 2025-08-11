# interfaz de consola para system.ai
from system import ai, memory
def execute(args, state):
    if not args:
        print("Uso: ai <texto> | ai start | ai stop")
        return
    sub = args[0]
    if sub == "start":
        print("Modo conversacional AI. Escribe 'ai stop' para salir.")
        while True:
            try:
                line = input("AI> ").strip()
            except KeyboardInterrupt:
                print("\nSaliendo modo AI.")
                break
            if not line:
                continue
            if line.lower() == "stop" or line.lower() == "ai stop":
                print("Modo AI detenido.")
                break
            resp = ai.answer(line, state)
            print("IA:", resp)
    else:
        prompt = " ".join(args)
        resp = ai.answer(prompt, state)
        print("IA:", resp)
