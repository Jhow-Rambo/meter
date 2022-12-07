from ..index import *
from services.convert_img import *
from services.save_img import *
from services.PaddleOCR.paddle_process import *

@router.post("/process-img")
async def process_image(request: Request):
  # img = await request.json()
  img = await request.json()
  print(img['base64'])
  new_img = convert_b64_to_img(img['base64'])
  save_img(new_img)
  process_ocr()
  return await request.json()
