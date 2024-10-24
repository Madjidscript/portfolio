from flask import Flask, request # type: ignore
from flask_restful import Api, Resource # type: ignore
from helpers.projet import *



class ProjetApi(Resource) :

    def post (self,route):
        if route == "createprojet":
            return CreatProjet()
        if route == "deleteprojet":
            return DeleteProjet()
        if route == "updateprojet":
            return UpdateProjet()
    
    def get (self,route,projet_id=None):
        if route =="getallprojet":
            return GetAllProjet
        
        if route == "getsingulprojet" and projet_id is not None:
            return  SingulProjet(projet_id)