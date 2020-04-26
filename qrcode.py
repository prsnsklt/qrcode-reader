from pyzbar.pyzbar import decode
from PIL import Image
path=""
d=decode(Image.open(path))
print(d[0].data.decode())