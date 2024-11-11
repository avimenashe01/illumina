class TestStoreService:
    def test_set_and_get(self, store_service):
        result = store_service.set("key1", "value1")
        assert result == "OK"
        assert store_service.get("key1") == "value1"

        # Overwrite an existing key
        result = store_service.set("key1", "new_value")
        assert result == "OK"
        assert store_service.get("key1") == "new_value"

    def test_exists(self, store_service):
        store_service.set("key_exists", "some_value")
        assert store_service.exists("key_exists") == 1
        assert store_service.exists("key_not_exists") == 0
        assert store_service.exists("key_exists", "key_not_exists") == 1

    def test_delete(self, store_service):
        store_service.set("key_to_delete", "delete_me")
        assert store_service.delete("key_to_delete") == 1
        assert store_service.exists("key_to_delete") == 0

        # Deleting non-existent keys should return 0
        assert store_service.delete("non_existent_key") == 0

    def test_incrby(self, store_service):
        store_service.set("counter", "10")
        assert store_service.incrby("counter", 5) == 15

        # Test non-existent key (should initialize to 0 and then increment)
        assert store_service.incrby("new_counter", 3) == 3

        # Test error handling for non-integer values
        store_service.set("invalid_counter", "not_an_int")
        assert store_service.incrby("invalid_counter", 1) == "Value is not an integer"

    def test_delete_multiple_keys(self, store_service):
        store_service.set("key1", "val1")
        store_service.set("key2", "val2")
        store_service.set("key3", "val3")
        assert store_service.delete("key1", "key2", "key3") == 3

