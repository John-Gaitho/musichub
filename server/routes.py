from flask import  Blueprint, request, jsonify
from models import db, User, Song, Playlist

api_bp = Blueprint('api', __name__)

# to create a new user
@api_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User()
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User has been created'}), 201

# to Get all songs
@api_bp.route('/songs', methods=['GET'])
def get_songs():
    songs = Song.query.all()
    return jsonify([song.title for song in songs])

# to create a new playlist
@api_bp.route('/playlists', methods=['POST'])
def create_playlist():
    data = request.get_json()
    playlist = Playlist(name=data['name'], user_id=data['user_id'])
    db.session.add(playlist)
    db.session.commit()
    return jsonify({'message': 'Playlist created'}), 201

