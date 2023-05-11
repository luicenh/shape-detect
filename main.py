from fastapi import FastAPI, Request
import uvicorn

from src import detect

app = FastAPI()

@app.post("/test")
async def root(request: Request):
    body = await request.json()
    points = body["points"]
    shape, ratio = detect.detect(points)

    return {"code": 0, "obj": {"shape": shape, "ratio": ratio}}


if __name__ == '__main__':
     uvicorn.run(app='main:app', host="127.0.0.1", port=7001, reload=True)


# 输入图形
