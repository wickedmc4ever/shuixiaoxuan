from fastapi import FastAPI, Request, Response, Depends,Form
import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import StreamingResponse
from starlette.middleware.sessions import SessionMiddleware
from pydantic import BaseModel
import os 
import configparser
from server.user import user    # 用户操作方法
#from server.workflow import config # 用户配置
from server.router import route # 服务器路由方法
import server.orm  # orm 操作db
import server.log  # 服务器日志 

# 从config.ini读取
USER_DIR = './config/user/'

# 创建文件夹并返回路径
def createDir(dirpath,dirname):
    os.mkdir(dirpath+dirname)
    return dirpath+dirname

# 返回指定文件夹的文件集合
def listFile(dir:str):
    fileobject = {}
    filelist = []
    for dirpath, dirnames, filenames in os.walk(dir,
                                                topdown=True):
        for file in filenames:
            filelist.append(file) 

    fileobject["filelist"] = filelist
    return fileobject

# 读取配置文件
def readConfig(config_file):
    obj = {}
    config = configparser.ConfigParser()
    config.read(config_file)
    
    for section in config.sections():
        obj[section] = {}
        for key, value in config.items(section):
            obj[section][key] = value
    
    return obj

obj = readConfig("./config/server/config.ini") # 读取系统配置
app = FastAPI()
# app.add_middleware(SessionMiddleware, secret_key="YOUR_SECRET_KEY") 添加中间件
app.add_middleware(SessionMiddleware,secret_key='')

# 模板引擎 templates
templates = Jinja2Templates(directory="templates")

# 静态文件目录,html
app.mount("/static", StaticFiles(directory="static"), name="static")

# 静态文件目录 - 用户上传
app.mount("/upload",StaticFiles(directory="upload"),name="upload")

# 静态文件目录 - 用户生成
app.mount("/output",StaticFiles(directory="output"),name="output")

# 静态文件目录 - 文本型内容
app.mount("/files",StaticFiles(directory="files"),name="files")

# index
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", { "request": request })

# map upload pics and generated vids.
@app.get("/mapping",response_class=HTMLResponse)
async def generatemapping(request:Request):
    pass

#user_config 跳转到用户配置页面
@app.get('/api/settings/userconfig',response_class=HTMLResponse)
async def redirectconfig(request:Request):
    return templates.TemplateResponse("config.html",{"request":request})

# 保存用户配置,写入config/user/{userid}/config.ini中
@app.post("/api/save/userconfig",response_class=HTMLResponse)
async def saveconfig(request:Request,openai:str = Form(...), zhipu :str= Form(...)):
    openai_key = openai
    zhipu_key = zhipu
    # 使用用户uuid创建目录
    uuid = user.get_db().query(user.User).filter(username=request.session['username']).first("uuid")
    createDir(dirpath=USER_DIR,dirname=uuid)
    # 写入配置文件至config.ini

# 读取
@app.get("api/load/userconfig",response_class=HTMLResponse)
async def loadconfig(request:Request):
    pass

#/upload 读取上传历史
@app.get("/api/load/upload_history",response_class=HTMLResponse)
async def listUploadFiles(request:Request):
    return templates.TemplateResponse("uploadfiles.html",{"request":request})

#/output 读取输出历史
@app.get("/api/load/output_history/",response_class=HTMLResponse)
async def listOutputfiles(request:Request):
    return templates.TemplateResponse("outputfiles.html",{"request":request})

# 加载对应关系
@app.post('api/load/mapping',response_class=HTMLResponse)
async def loadmapping(request:Request):
    pass

if __name__ == "__main__":    
    uvicorn.run("main:app", port=8000,  reload=True, log_level="info")
