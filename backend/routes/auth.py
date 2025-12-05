"""Authentication routes"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import db, User
import bcrypt

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['POST'])
def register():
    """Register a new user"""
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Données manquantes"}), 400
    
    username = data.get('username', '').strip()
    email = data.get('email', '').strip().lower()
    password = data.get('password', '')
    
    # Validation
    if not username or len(username) < 3:
        return jsonify({"error": "Le pseudo doit faire au moins 3 caractères"}), 400
    
    if not email or '@' not in email:
        return jsonify({"error": "Email invalide"}), 400
    
    if not password or len(password) < 6:
        return jsonify({"error": "Le mot de passe doit faire au moins 6 caractères"}), 400
    
    # Check if user exists
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Cet email est déjà utilisé"}), 409
    
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Ce pseudo est déjà pris"}), 409
    
    # Hash password
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    # Create user
    user = User(
        username=username,
        email=email,
        password_hash=password_hash
    )
    
    db.session.add(user)
    db.session.commit()
    
    # Create token
    access_token = create_access_token(identity=user.id)
    
    return jsonify({
        "message": "Bienvenue sur EduQuest! 🎓",
        "token": access_token,
        "user": user.to_dict()
    }), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    """Login user"""
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Données manquantes"}), 400
    
    email = data.get('email', '').strip().lower()
    password = data.get('password', '')
    
    if not email or not password:
        return jsonify({"error": "Email et mot de passe requis"}), 400
    
    # Find user
    user = User.query.filter_by(email=email).first()
    
    if not user:
        return jsonify({"error": "Email ou mot de passe incorrect"}), 401
    
    # Check password
    if not bcrypt.checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8')):
        return jsonify({"error": "Email ou mot de passe incorrect"}), 401
    
    # Create token
    access_token = create_access_token(identity=user.id)
    
    return jsonify({
        "message": f"Content de te revoir, {user.username}! 👋",
        "token": access_token,
        "user": user.to_dict()
    })


@auth_bp.route('/me', methods=['GET'])
@jwt_required()
def get_current_user():
    """Get current user info"""
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({"error": "Utilisateur non trouvé"}), 404
    
    return jsonify({"user": user.to_dict()})


@auth_bp.route('/me', methods=['PUT'])
@jwt_required()
def update_profile():
    """Update user profile"""
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({"error": "Utilisateur non trouvé"}), 404
    
    data = request.get_json()
    
    if 'avatar' in data:
        user.avatar = data['avatar']
    
    if 'username' in data:
        new_username = data['username'].strip()
        if len(new_username) >= 3:
            # Check if taken
            existing = User.query.filter_by(username=new_username).first()
            if existing and existing.id != user.id:
                return jsonify({"error": "Ce pseudo est déjà pris"}), 409
            user.username = new_username
    
    db.session.commit()
    
    return jsonify({
        "message": "Profil mis à jour! ✨",
        "user": user.to_dict()
    })
