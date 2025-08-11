import importlib
from system import kernel
from system import memory as memory_sys

def main():
    print("=== SilverOS v3.0 - Orion Mind ===")
    kernel.bootstrap()
    try:
        kernel.run()
    except KeyboardInterrupt:
        print("\nInterrupción por teclado. Saliendo...")
    finally:
        memory_sys.save_all()
        print("Memoria guardada. Adiós.")

if __name__ == "__main__":
    main()
