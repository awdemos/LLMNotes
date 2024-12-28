import requests
import struct
import base64

def get_random_float32_base64():
    url = "https://www.random.org/integers/"
    params = {
        "num": 4,
        "min": 0,
        "max": 255,
        "col": 1,
        "base": 10,
        "format": "plain",
        "rnd": "new"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        # Get 4 random bytes
        random_bytes = bytes([int(num) for num in response.text.strip().split()])
        # Convert bytes to float32
        float32_value = struct.unpack('f', random_bytes)[0]
        # Encode float32 to base64
        base64_encoded = base64.b64encode(struct.pack('f', float32_value)).decode('utf-8')
        return base64_encoded
    else:
        return None

# Example usage
random_float32_base64 = get_random_float32_base64()
print(random_float32_base64)

# Decode and print the original float32 value
if random_float32_base64:
    decoded_float32 = struct.unpack('f', base64.b64decode(random_float32_base64))[0]
    print(f"Decoded float32 value: {decoded_float32}")

