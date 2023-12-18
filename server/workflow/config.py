# 读取并加载用户历史配置

from fastapi import Response,Request
from fastapi.responses import HTMLResponse
from main import app,templates


# 读取并加载用户历史配置
@app.post("/api/read/config",response_class=HTMLResponse)
async def readConfig():
    pass


# 用户历史配置备份（序列化至本地）