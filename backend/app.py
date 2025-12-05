"""EduQuest Backend - Flask Application"""

from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from datetime import timedelta

from config import Config
from models import db


def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = Config.SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = Config.JWT_SECRET_KEY
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=7)
    
    # Extensions
    CORS(app, origins=["http://localhost:3000", "http://127.0.0.1:3000"])
    db.init_app(app)
    jwt = JWTManager(app)
    
    # JWT error handlers
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return jsonify({"error": "Token expiré, reconnecte-toi!"}), 401
    
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return jsonify({"error": "Token invalide"}), 401
    
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return jsonify({"error": "Authentification requise"}), 401
    
    # Register blueprints
    from routes.auth import auth_bp
    from routes.quiz import quiz_bp
    from routes.leaderboard import leaderboard_bp
    from routes.ai import ai_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(quiz_bp, url_prefix='/api/quiz')
    app.register_blueprint(leaderboard_bp, url_prefix='/api/leaderboard')
    app.register_blueprint(ai_bp, url_prefix='/api/ai')
    
    # Health check
    @app.route('/api/health')
    def health():
        return jsonify({
            "status": "ok",
            "message": "EduQuest API is running! 🎓"
        })
    
    # Create tables and seed
    with app.app_context():
        db.create_all()
        
        # Seed data
        from seed_data import seed_database
        from models import Quiz, Question
        seed_database(db, Quiz, Question)
    
    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
