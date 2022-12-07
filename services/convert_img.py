import base64
from io import BytesIO
from PIL import Image
import numpy as np

def convert_b64_to_img(img):
  dec = base64.b64decode(img + "===")
  image = Image.open(BytesIO(dec)).convert("RGB")

  i = np.array(image)
  red = i[:, :, 0].copy()
  i[:, :, 0] = i[:, :, 2].copy()
  i[:, :, 2] = red

  return i