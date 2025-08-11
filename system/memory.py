import os, json
MEM_DIR = os.path.join(os.getcwd(), "memory")
_data = {}

def ensure_dir():
    if not os.path.isdir(MEM_DIR):
        os.makedirs(MEM_DIR, exist_ok=True)

def load_all():
    ensure_dir()
    global _data
    _data = {}
    for fname in os.listdir(MEM_DIR):
        if fname.endswith(".json"):
            key = fname[:-5]
            try:
                with open(os.path.join(MEM_DIR, fname), "r", encoding="utf-8") as f:
                    _data[key] = json.load(f)
            except Exception:
                _data[key] = None

def save_all():
    ensure_dir()
    for key, val in _data.items():
        try:
            with open(os.path.join(MEM_DIR, f"{key}.json"), "w", encoding="utf-8") as f:
                json.dump(val, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print("Error guardando memoria", key, e)

def save(key, value):
    _data[key] = value
    save_all()

def read(key):
    return _data.get(key)

def list_keys():
    return list(_data.keys())

def summary():
    return {"entries": len(_data)}
