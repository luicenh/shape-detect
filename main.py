from fastapi import FastAPI, Request
import uvicorn

from src import detect_api

app = FastAPI()

@app.post("/shape/detect")
async def shape_detect(request: Request):
    body = await request.json()
    points = body["points"]
    shape, width, height, angle = detect_api.detect1(points)
    return {"code": 0, "obj": {"shape": shape, "width": width, "height": height, "angle": angle}}


if __name__ == '__main__':
     uvicorn.run(app='main:app', host="0.0.0.0", port=7001, reload=True)


