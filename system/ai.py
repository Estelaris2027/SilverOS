# IA básica offline: respuesta por patrones + memoria simple
from system import memory
def answer(prompt, state=None):
    # busqueda simple en memoria por claves mencionadas
    if prompt.strip().lower() in ("hola","hello","hi"):
        return "Hola — soy el asistente de SilverOS. ¿En qué puedo ayudarte?"
    if "memoria" in prompt.lower() or "recordar" in prompt.lower():
        return "Puedo guardar 'clave:valor' con 'mem save <clave> <valor>'. Usa 'mem list' para verlas."
    # si pregunta por algo guardado
    parts = prompt.split()
    if parts and parts[0].endswith("?"):
        return "Buena pregunta. Aún no tengo una respuesta completa sin internet."
    # fallback creativo sencillo
    stored = memory.read("notes") or []
    if isinstance(stored, list) and stored:
        return f"Recuerdo algunas notas: {stored[:3]}"
    return "Lo siento, no puedo buscar en internet. Puedo ayudarte a ejecutar comandos o guardar notas."
