from app.api import bp
from flask import request, make_response, jsonify
from app.models import User
from app import db
from app.api.authorization import login_required
from flask_cors import cross_origin


@bp.route('/user', methods=['GET'])
@login_required
def get_user(id):
    return "hi " + str(id)

@bp.route('/user', methods=['POST'])
@login_required
def get_user_two(id):
    return "json: " + str(request.get_json())

@bp.route('/user/register', methods=['POST'])
@cross_origin()
def register():
    # get the post data
    post_data = request.get_json()
    print(post_data)

    email = post_data.get('email').lower()
    
    # check if user already exists
    user = User.query.filter_by(email=email).first()
    if not user:
        try:
            user = User(
                email=email,
                password=post_data.get('password')
            )

            # insert the user
            db.session.add(user)
            db.session.commit()

            print(user.id)

            # generate the auth token
            auth_token = user.encode_auth_token(user.id)
            responseObject = {
                'status': 'success',
                'message': 'Successfully registered.',
                'auth_token': auth_token.decode()
            }
            return make_response(jsonify(responseObject)), 201
        except Exception as e:
            print(e)
            responseObject = {
                'status': 'fail',
                'message': 'Some error occurred while registering user. Please try again.'
            }
            return make_response(jsonify(responseObject)), 401
    else:
        responseObject = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return make_response(jsonify(responseObject)), 202

    
@bp.route('/user/login', methods=['POST'])
@cross_origin()
def login():
    # get the post data
    print("un /user/login")
    print(request.get_json())
    post_data = request.get_json()
    try:
        # fetch the user data
        user: User = User.query.filter_by(
            email=post_data.get('email')
        ).first()
        if user and user.check_password(post_data.get('password')):
            auth_token = user.encode_auth_token(user.id)
            if auth_token:
                responseObject = {
                    'status': 'success',
                    'message': 'Successfully logged in.',
                    'auth_token': auth_token.decode()
                }
                print(responseObject)
                return make_response(jsonify(responseObject)), 200
        else:
            responseObject = {
                'status': 'fail',
                'message': 'User does not exist.'
            }
            return make_response(jsonify(responseObject)), 404
    except Exception as e:
        print(e)
        responseObject = {
            'status': 'fail',
            'message': 'Try again'
        }
        return make_response(jsonify(responseObject)), 500


