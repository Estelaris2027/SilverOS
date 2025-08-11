def execute(args, state):
    hist = state.get("history", [])
    for i, cmd in enumerate(hist[-50:], start=1):
        print(f"{i}: {cmd}")
