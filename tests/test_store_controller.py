import pytest


class TestStoreController:

    @pytest.fixture(autouse=True)
    def setup_app(self, app):
        self.client = app.test_client()

    def test_set_key(self):
        response = self.client.post('/api/store/set', json={"key": "key1", "value": "value1"})
        assert response.status_code == 200
        assert response.json == {"status": "OK"}

    def test_get_key(self):
        self.client.post('/api/store/set', json={"key": "key1", "value": "value1"})
        response = self.client.get('/api/store/get?key=key1')
        assert response.status_code == 200
        assert response.json == {"key": "key1", "value": "value1"}

    def test_incrby_key(self):
        self.client.post('/api/store/set', json={"key": "count", "value": 0})
        response = self.client.post('/api/store/incrby', json={"key": "count", "increment": 5})
        assert response.status_code == 200
        assert response.json == {"key": "count", "new_value": 5}

    def test_incrby_invalid(self):
        self.client.post('/api/store/set', json={"key": "invalid", "value": "not_a_number"})
        response = self.client.post('/api/store/incrby', json={"key": "invalid", "increment": 5})
        assert response.status_code == 400
        assert response.json == {"error": "Value is not an integer"}

    def test_delete_key(self):
        self.client.post('/api/store/set', json={"key": "key1", "value": "value1"})
        self.client.post('/api/store/set', json={"key": "key2", "value": "value2"})
        response = self.client.delete('/api/store/delete', json={"keys": ["key1", "key2"]})
        assert response.status_code == 200
        assert response.json == {"deleted": 2}
