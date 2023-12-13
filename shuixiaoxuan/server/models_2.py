from sqlalchemy import Column,  Integer, String
from sqlalchemy.orm import relationships,Mapped
from .database import Base

class KOL():
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
     



