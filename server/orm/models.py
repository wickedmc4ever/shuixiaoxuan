from sqlalchemy import Column,  Integer, String 
from sqlalchemy.orm import relationships
from .database import Base

class KOL(Base):
    """_summary_ 用于生成公众号下发布文章信息表：

    参数示例
    'mp_name': '36氪', 
    'avatar': 'http://wx.qlogo.cn/mmhead/Q3auHgzwzM6bia44ArPNMqFIeUFznyuic1uaRBHxkkppnTnnYpkPVSXA/0', 
    'time': 1702042197, 
    'payType': 0,
    'inner': 0,
    'score': 1702042197, 
    'mpRank': 15, 
    'topics': [], 
    'isLike': 0, 
    'isReposted': 0, 
    'bookId': '', 
    'format': '', 
    'version': 0, 
    'soldout': 0, 
    'type': 0, 
    'payType': 0, 
    'cover': '', 
    'title': '', 
    'author': '', 
    'userVid': 10003, 
    'name': 'MP', 
    'avatar': '', 
    'isFollowing': 0, 
    'isFollower': 0, 
    'isBlacking': 0, 
    'isBlackBy': 0, 
    'isHide': 1, 
    'isV': 0, 
    'roleTags': [], 
    'followPromote': '', 
    'signature': ''
    """
    __table__name = "articles"
    # 表结构
    id = Column(Integer, primary_key=True, index=True)
    mp_name = Column(String)
    avatar = Column(String)
    time= Column(Integer)
    payType= Column(bool)
    inner= Column(bool)
    score= Column(Integer) 
    mpRank= Column(Integer) 
    topics= Column(object), # 返回一个列表 
    isLike= Column(bool) 
    isReposted= Column(bool)
    bookId= Column(Integer)
    format= Column(String)
    version= Column(Integer)
    soldout= Column(bool)
    type= Column(Integer)
    payType= Column(Integer)
    cover= Column(String)
    title= Column(String)
    author=  Column(String)
    userVid= Column(Integer)
    name=Column(String)
    avatar_user= Column(String)
    isFollowing= Column(bool) 
    isFollower=Column(bool) 
    isBlacking=Column(bool) 
    isBlackBy=Column(bool)  
    isHide= Column(bool)  
    isV=Column(bool)  
    roleTags=Column(object)  # 返回一个角色标签
    followPromote= Column(bool)  
    signature=Column(bool) 

