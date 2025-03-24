import base64
import os
import requests

def send_image_to_ollama(prompt_text, image_filename):
    image_folder = 'images'
    image_path = os.path.join(image_folder, image_filename)

    if not os.path.exists(image_path):
        print(f"❌ Image '{image_path}' not found.")
        return

    # Read and encode the image
    with open(image_path, 'rb') as img_file:
        b64_image = base64.b64encode(img_file.read()).decode('utf-8')

    # API request payload
    payload = {
        'model': 'llava',  # or 'bakllava', etc.
        'prompt': prompt_text,
        'images': [b64_image],
        'stream': False
    }

    # Send request to Ollama
    try:
        response = requests.post('http://localhost:11434/api/generate', json=payload)
        response.raise_for_status()
        print("🧠 Ollama response:")
        print(response.json()['response'])
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")

# Example usage:
if __name__ == "__main__":
    prompt = input("Enter your prompt: ")
    image_file = input("Enter image filename (in 'images/' folder): ")
    send_image_to_ollama(prompt, image_file)
