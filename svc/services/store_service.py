from svc.data.store import Store


class StoreService:
    def __init__(self):
        self.store = Store()

    def set(self, key, value):
        """Sets a key-value pair in the store."""
        return self.store.set(key, value)

    def get(self, key):
        """Gets the value of a key from the store."""
        value = self.store.get(key)
        if value is None:
            return "Key not found"
        return value

    def exists(self, *keys):
        """Checks if the provided keys exist in the store."""
        return self.store.exists(*keys)

    def delete(self, *keys):
        """Deletes one or more keys from the store."""
        count = self.store.delete(*keys)
        return count

    def incrby(self, key, increment):
        """Increments the value of a key by a given increment."""
        return self.store.incrby(key, increment)