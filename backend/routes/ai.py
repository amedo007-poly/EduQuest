"""AI Tutor routes"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import User, Attempt, Quiz
from services.ai_tutor import get_ai_response, explain_wrong_answer, generate_encouragement

ai_bp = Blueprint('ai', __name__)


@ai_bp.route('/chat', methods=['POST'])
@jwt_required()
def chat_with_tutor():
    """Chat with AI tutor"""
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({"error": "Utilisateur non trouvé"}), 404
    
    data = request.get_json()
    message = data.get('message', '').strip()
    
    if not message:
        return jsonify({"error": "Message vide"}), 400
    
    if len(message) > 1000:
        return jsonify({"error": "Message trop long (max 1000 caractères)"}), 400
    
    # Get context from last attempt
    last_attempt = Attempt.query.filter_by(user_id=user_id).order_by(
        Attempt.completed_at.desc()
    ).first()
    
    context = {
        "user_level": user.level,
        "streak": user.streak
    }
    
    if last_attempt:
        quiz = Quiz.query.get(last_attempt.quiz_id)
        if quiz:
            context["last_quiz_subject"] = quiz.subject
            percentage = (last_attempt.correct_answers / last_attempt.total_questions) * 100 if last_attempt.total_questions > 0 else 0
            context["last_quiz_score"] = round(percentage)
    
    # Get AI response
    response = get_ai_response(message, context)
    
    return jsonify({
        "response": response,
        "context": {
            "level": user.level,
            "streak": user.streak
        }
    })


@ai_bp.route('/explain', methods=['POST'])
@jwt_required()
def explain_error():
    """Get AI explanation for a wrong answer"""
    data = request.get_json()
    
    question = data.get('question', '')
    user_answer = data.get('user_answer', '')
    correct_answer = data.get('correct_answer', '')
    subject = data.get('subject', 'général')
    
    if not all([question, user_answer, correct_answer]):
        return jsonify({"error": "Données manquantes"}), 400
    
    explanation = explain_wrong_answer(question, user_answer, correct_answer, subject)
    
    return jsonify({"explanation": explanation})


@ai_bp.route('/encourage', methods=['GET'])
@jwt_required()
def get_encouragement():
    """Get personalized encouragement from AI"""
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({"error": "Utilisateur non trouvé"}), 404
    
    # Get last score
    last_attempt = Attempt.query.filter_by(user_id=user_id).order_by(
        Attempt.completed_at.desc()
    ).first()
    
    last_score = 0
    if last_attempt and last_attempt.total_questions > 0:
        last_score = round((last_attempt.correct_answers / last_attempt.total_questions) * 100)
    
    message = generate_encouragement(user.streak, user.level, last_score)
    
    return jsonify({
        "message": message,
        "stats": {
            "level": user.level,
            "streak": user.streak,
            "last_score": last_score
        }
    })
