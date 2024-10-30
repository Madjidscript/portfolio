from flask import Flask, request # type: ignore
from flask_restful import Api, Resource # type: ignore
from helpers.certif import *



class CertiftApi(Resource) :

    def post (self,route):
        if route == "createcertif":
            return CreatCertif()
        if route == "deletecertif":
            return DeleteCertif()
        if route == "updatecertif":
            return Updatecertif()
    
    def get (self,route,certif_id=None):
        if route =="getallcertif":
            return GetAllCertif()
        
        if route == "getsingulcertif" and certif_id is not None:
            return  SingulCertif(certif_id)