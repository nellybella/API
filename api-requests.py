import requests
from PIL import Image
import io

response = requests.get('http://127.0.0.1:8000/iris')
file = io.BytesIO(response.content)
image = Image.open(file)
image.show()