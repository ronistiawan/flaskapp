from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from services.sms import SMS

hotelapi = Blueprint('hotel',__name__)

@hotelapi.route('/hotel')
def hotels():
    
    return 'List of hotels'

@hotelapi.route('/hotel/<id>')
def get_hotel_by_id(id):

    SMS.send('62837482734','YEAAAYYYY')
    return 'hotel: ' + id

@hotelapi.route('/hotel/add', methods=['POST'])
def add_hotel():
    return 'a new hotel add'

@hotelapi.route('/hotel/edit', methods=['POST'])
def edit_hotel():
    return 'Hotel edited'