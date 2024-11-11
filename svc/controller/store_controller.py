from flask import Blueprint, request, jsonify

from svc.services.store_service import StoreService

store_controller = Blueprint('store_controller', __name__)

# Initialize the StoreService
store_service = StoreService()


@store_controller.route('/set', methods=['POST'])
def set_key():
    """
    Endpoint to set a key-value pair in the store.
    Expects JSON data: {"key": "some_key", "value": "some_value"}
    """
    data = request.get_json()

    # Validate input
    if not data or 'key' not in data or 'value' not in data:
        msg = {"error": "Invalid input, key and value are required"}
        return jsonify(msg), 400

    key = data['key']
    value = data['value']

    status = store_service.set(key, value)
    return jsonify({"status": status})


@store_controller.route('/get', methods=['GET'])
def get_key():
    """
    Endpoint to get the value of a key from the store.
    Expects query parameter: key=<key>
    Returns "Key not found" if the key doesn't exist.
    """
    key = request.args.get('key')
    result = store_service.get(key)

    if result == "Key not found":
        return jsonify({"error": "Key not found"}), 404

    return jsonify({"key": key, "value": result})


@store_controller.route('/exists', methods=['GET'])
def exists_keys():
    """
    Endpoint to check if keys exist in the store.
    Expects query parameter: keys=key1,key2,...
    Returns the number of existing keys.
    """

    keys = request.args.get('keys', '')
    if not keys:
        return jsonify({"error": "No keys provided"}), 400

    key_list = keys.split(',')
    count = store_service.exists(*key_list)
    return jsonify({"exists": count})


@store_controller.route('/delete', methods=['DELETE'])
def delete_keys():
    """
    Endpoint to delete keys from the store.
    Expects JSON body: {"keys": ["key1", "key2", ...]}
    """

    data = request.get_json()
    keys = data.get('keys', [])
    if not keys:
        return jsonify({"error": "No keys provided"}), 400

    deleted_count = store_service.delete(*keys)
    return jsonify({"deleted": deleted_count})


@store_controller.route('/incrby', methods=['POST'])
def incrby_key():
    """
    Endpoint to increment a key by a specified increment value.
    Expects JSON data: {"key": "some_key", "increment": 1}
    """
    data = request.get_json()

    # Validate input
    if not data or 'key' not in data or 'increment' not in data:
        msg = {"error": "Invalid input, key and increment are required"}
        return jsonify(msg), 400

    key = data['key']
    increment = data['increment']

    result = store_service.incrby(key, increment)

    if isinstance(result, str):
        return jsonify({"error": result}), 400

    return jsonify({"key": key, "new_value": result})