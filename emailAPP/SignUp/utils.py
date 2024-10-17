from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
import json
import base64

def encode_uid(data):
    return urlsafe_base64_encode(force_bytes(json.dumps(data)))


def decode_uid(encoded_uid):
    try:
        decoded_bytes = base64.urlsafe_b64decode(encoded_uid.encode())
        return json.loads(decoded_bytes.decode())
    except Exception as e:
        print(f"Error decoding UID: {e}")
        return None