class SessionMemory:
    def __init__(self, user_id):
        self.user_id = user_id
        self.store = {}

    def save(self, key, value):
        self.store[key] = value

    def load(self, key):
        return self.store.get(key, None)
