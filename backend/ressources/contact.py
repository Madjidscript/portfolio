from flask import Flask, request # type: ignore
from flask_restful import Api, Resource # type: ignore
from helpers.contact import *


class ContactApi(Resource):

    def post(self,route):
        if route == "contactuser":
            return Contacts()