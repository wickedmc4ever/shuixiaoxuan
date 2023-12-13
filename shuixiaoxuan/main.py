from fastapi import FastAPI, Request, Response, Depends
import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from server import crud, models, schemas
from server.database import SessionLocal, engine
from sqlalchemy.orm import Session
import zhipuai
import dotenv

app = FastAPI()

# 请去智普AI官网申请自己的api_key：www.zhipuai.cn
zhipuai.api_key = dotenv.get_key('zhipu_apikey')


# 用orm生成数据库的表格
models.Base.metadata.create_all(bind=engine)

# 生成文案的提示词的数据结构
class Item(BaseModel):
    prompt: str | None = ''

# 模板引擎 templates
templates = Jinja2Templates(directory="templates")

# 创建静态文件目录
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", { "request": request })

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000,  reload=True, log_level="info")

