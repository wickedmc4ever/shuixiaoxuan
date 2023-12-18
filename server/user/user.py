from fastapi import FastAPI, Response, Request,Depends
from fastapi.responses import HTMLResponse,RedirectResponse
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from fastapi import HTTPException

from starlette.middleware.sessions import SessionMiddleware
from fastapi.responses import RedirectResponse
from main import app,templates
from fastapi import Form

# Define the SQLAlchemy model
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    #email=Column(String)

# Create the database engine and session
engine = create_engine('sqlite:///./databases/users.db')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# login
@app.get("/userlogin",response_class=HTMLResponse)
async def login(request:Request):
    return templates.TemplateResponse("login.html", { "request": request })

# register
@app.get("/user_register",response_class=HTMLResponse)
async def register(request:Request):
    return templates.TemplateResponse("register.html",{"request":request})

# Define the request body model
class UserCreate(BaseModel):
    username: str
    password: str
    #email:str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# index
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    db = get_db()
    return templates.TemplateResponse("index.html", { "request": request })

# jump2login
@app.get("/user/login",response_class=HTMLResponse)
async def login(request:Request):
    return templates.TemplateResponse("login.html", { "request": request })

# validate_login_status 如果处于登陆状态则无法注销
# @app.post("/validate_login",response_class=HTMLResponse)
# async def validate(request:Request):
    # Validate the login credentials
    # username = request.form.get("username")
    # password = request.form.get("password")
    # if not username or not password:
        # raise HTTPException(status_code=400, detail="Invalid username or password")
    # db = get_db()
    # user = db.query(User).filter(User.username == username, User.password == password).first()
    # if not user:
        # raise HTTPException(status_code=401, detail="Invalid username or password")
    # 
    # return templates.TemplateResponse("index.html", {"request": request})

@app.post("/validate_login", response_class=HTMLResponse)
async def validate(request: Request, username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username, User.password == password).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    request.session['username'] = user.username  # Store username in session
    return RedirectResponse(url="/", status_code=302)

# 访问register页面
@app.get('/user/register',response_class=HTMLResponse)
async def loadregister(request:Request):
    return templates.TemplateResponse("register.html",{"request":request})

# Define the route to handle the form submission
# 获取返回data的username属性作为用户名，password属性作为密码。
@app.post('/api/save_register')
async def register_user(request:Request,username: str = Form(...), password: str = Form(...)):
    db = SessionLocal()
    new_user = User(username=username, password=password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return templates.TemplateResponse("index.html", {"request": request})

# expire for user session
@app.get("/some_endpoint")
async def some_endpoint(request: Request):
    username = request.session.get('username')
    if username is None:
        # Handle the case where the user is not logged in
        ...
    # Proceed with the logic for logged-in users
    ...

# logout
@app.get("/user/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="./templates/login.html", status_code=302)
