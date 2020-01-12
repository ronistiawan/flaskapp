'''
REST API : Accessing MongoDB with pymongo
'''
from flask import Blueprint, request, jsonify, Response
from appdb import db, ObjectId
from bson.json_util import dumps

hotelapi = Blueprint('hotel',__name__)

@hotelapi.route('/hotel',methods=['GET'])
def hotels():    
    return Response(dumps(db.hotels.find()), content_type='application/json')

@hotelapi.route('/hotel/<id>',methods=['GET'])
def get_hotel_by_id(id):
    return Response(dumps(db.hotels.find_one({'_id':ObjectId(id)}), content_type='application/json'))

@hotelapi.route('/hotel/add', methods=['POST'])
def add_hotel():
    hotel = request.get_json(force=True)
    db.hotels.insert_one(hotel)
    return Response(dumps(hotel), content_type='application/json')

@hotelapi.route('/hotel/update', methods=['POST'])
def edit_hotel():
    hotel = request.get_json(force=True)
    query = {"name": "My Everything"}
    newvalues = {"$set":hotel}
    db.hotels.update_one(query, newvalues)
    return Response(dumps(hotel), content_type='application/json')