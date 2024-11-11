import pytest


class TestStoreOperations:
    def setup_method(self, method):
        self.store = {"initial_key": "initial_value"}

    def test_set_operation(self):
        self.store["key1"] = "value1"
        assert self.store["key1"] == "value1"

    def test_get_operation(self):
        assert self.store.get("initial_key") == "initial_value"

    def test_delete_operation(self):
        del self.store["initial_key"]
        assert "initial_key" not in self.store
