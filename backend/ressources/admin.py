from flask import Flask, request # type: ignore
from flask_restful import Api, Resource # type: ignore
from helpers.admin import *


class AdminApi (Resource):
    def post (self,route):
        if route == "creatadmin":
            return CreatAdmin()
        if route == "loginadmin":
            return LoginAdmin()
        if route == "adminupdate":
            return UpdateAdmin()
        
    def get (self,route,article_id=None):
        if route=="allAdmin":
            return GetAllAdmin()
        if route =="getsingullarticle" and article_id is not None:
            return GetSingulAdmin(article_id)
      
    def delete (self,route):
        if route=="deleteadmin":
            return DeleteAdmin()