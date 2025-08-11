import os
def execute(args, state):
    cwd = state.get("cwd", os.getcwd())
    try:
        for f in os.listdir(cwd):
            print(f)
    except Exception as e:
        print("ls error:", e)
