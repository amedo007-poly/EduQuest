"""Leaderboard routes"""

from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import User
from services.scoring import calculate_leaderboard_rank

leaderboard_bp = Blueprint('leaderboard', __name__)


@leaderboard_bp.route('/', methods=['GET'])
@jwt_required()
def get_leaderboard():
    """Get top 50 players leaderboard"""
    user_id = get_jwt_identity()
    current_user = User.query.get(user_id)
    
    # Get top 50 by score
    top_users = User.query.order_by(User.score.desc()).limit(50).all()
    
    leaderboard = []
    for rank, user in enumerate(top_users, 1):
        leaderboard.append({
            "rank": rank,
            "username": user.username,
            "avatar": user.avatar,
            "level": user.level,
            "score": user.score,
            "streak": user.streak,
            "is_current_user": user.id == user_id
        })
    
    # Get current user's rank if not in top 50
    current_rank = None
    if current_user:
        current_rank = calculate_leaderboard_rank(current_user, User)
    
    return jsonify({
        "leaderboard": leaderboard,
        "current_user_rank": current_rank,
        "total_players": User.query.count()
    })


@leaderboard_bp.route('/top3', methods=['GET'])
def get_top3():
    """Get top 3 players (public endpoint)"""
    top_users = User.query.order_by(User.score.desc()).limit(3).all()
    
    podium = []
    medals = ["🥇", "🥈", "🥉"]
    
    for rank, user in enumerate(top_users):
        podium.append({
            "rank": rank + 1,
            "medal": medals[rank],
            "username": user.username,
            "avatar": user.avatar,
            "level": user.level,
            "score": user.score
        })
    
    return jsonify({"podium": podium})


@leaderboard_bp.route('/streaks', methods=['GET'])
@jwt_required()
def get_streak_leaderboard():
    """Get top streaks leaderboard"""
    top_streaks = User.query.filter(User.streak > 0).order_by(
        User.streak.desc()
    ).limit(20).all()
    
    streaks = []
    for rank, user in enumerate(top_streaks, 1):
        fire = "🔥" * min(user.streak, 5)  # Max 5 fire emojis
        streaks.append({
            "rank": rank,
            "username": user.username,
            "avatar": user.avatar,
            "streak": user.streak,
            "fire": fire
        })
    
    return jsonify({"streaks": streaks})
