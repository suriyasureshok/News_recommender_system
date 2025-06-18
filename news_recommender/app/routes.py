from flask import Blueprint, request, jsonify
from . import db
from .models import User, Like, News
from .auth import generate_token, verify_token
from .recommender import recommend

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    if User.query.filter((User.email==data['email']) | (User.username==data['username'])).first():
        return jsonify({"error":"User exists"}), 409
    u = User(username=data['username'], email=data['email'])
    u.set_password(data['password'])
    db.session.add(u); db.session.commit()
    token = generate_token(u.id)
    return jsonify({'token':token}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    u = User.query.filter_by(email=data['email']).first()
    if u and u.check_password(data['password']):
        return jsonify({'token': generate_token(u.id)})
    return jsonify({"error":"Invalid login"}), 401

@auth_bp.route("/like/<int:news_id>", methods=["POST"])
def like(news_id):
    t = request.headers.get("Authorization","").split("Bearer ")[-1]
    uid = verify_token(t)
    if not uid: return jsonify({"error":"Unauthorized"}), 401
    if not Like.query.filter_by(user_id=uid, news_id=news_id).first():
        db.session.add(Like(user_id=uid, news_id=news_id))
        db.session.commit()
    return jsonify({"liked":news_id})

@auth_bp.route("/recommend", methods=["GET"])
def get_recs():
    t = request.headers.get("Authorization", "").split("Bearer ")[-1]
    uid = verify_token(t)
    if not uid:
        return jsonify({"error": "Unauthorized"}), 401

    all_n = News.query.order_by(News.published_at.desc()).all()
    liked_ids = [l.news_id for l in Like.query.filter_by(user_id=uid)]
    liked = [n for n in all_n if n.id in liked_ids]
    
    if not liked:
        fallback = all_n[:10]
        return jsonify([
            {
                'id': n.id,
                'title': n.title,
                'description': n.description,
                'category': n.category
            }
            for n in fallback
        ])

    recs = recommend(liked, all_n)
    return jsonify([
        {
            'id': n.id,
            'title': n.title,
            'description': n.description,
            'category': n.category
        }
        for n in recs
    ])

@auth_bp.route("/news", methods=["GET"])
def all_news():
    t = request.headers.get("Authorization","").split("Bearer ")[-1]
    if not verify_token(t): return jsonify({"error":"Unauthorized"}), 401
    all_n = News.query.order_by(News.published_at.desc()).all()
    return jsonify([{'id':n.id,'title':n.title,'description':n.description,'category':n.category} for n in all_n])
