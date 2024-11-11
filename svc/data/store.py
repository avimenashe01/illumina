from svc.utils.singleton import Singleton


class Store(Singleton):
    def __init__(self):
        self._store = {}

    def set(self, key, value):
        self._store[key] = value
        return "OK"

    def get(self, key):
        return self._store.get(key)

    def exists(self, *keys):
        return sum(1 for key in keys if key in self._store)

    def delete(self, *keys):
        count = 0
        for key in keys:
            if key in self._store:
                del self._store[key]
                count += 1
        return count

    def incrby(self, key, increment):
        if key not in self._store:
            self._store[key] = 0

        try:
            self._store[key] = int(self._store[key]) + increment
        except (ValueError, TypeError):
            return "Value is not an integer"

        return self._store[key]
