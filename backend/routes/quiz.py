"""Quiz routes"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, User, Quiz, Question, Attempt
from services.scoring import calculate_attempt_result, update_user_stats, get_recommended_quizzes

quiz_bp = Blueprint('quiz', __name__)


@quiz_bp.route('/', methods=['GET'])
@jwt_required()
def get_quizzes():
    """Get all available quizzes for user's level"""
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({"error": "Utilisateur non trouvé"}), 404
    
    # Get quizzes at or below user's level
    quizzes = Quiz.query.filter(
        Quiz.level_required <= user.level + 1
    ).all()
    
    return jsonify({
        "quizzes": [q.to_dict() for q in quizzes],
        "user_level": user.level
    })


@quiz_bp.route('/recommended', methods=['GET'])
@jwt_required()
def get_recommended():
    """Get recommended quizzes for user"""
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({"error": "Utilisateur non trouvé"}), 404
    
    quizzes = get_recommended_quizzes(user, Quiz, limit=5)
    
    return jsonify({
        "quizzes": [q.to_dict() for q in quizzes]
    })


@quiz_bp.route('/<int:quiz_id>', methods=['GET'])
@jwt_required()
def get_quiz(quiz_id):
    """Get a specific quiz with questions"""
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({"error": "Utilisateur non trouvé"}), 404
    
    quiz = Quiz.query.get(quiz_id)
    
    if not quiz:
        return jsonify({"error": "Quiz non trouvé"}), 404
    
    # Check if user has required level
    if quiz.level_required > user.level + 1:
        return jsonify({
            "error": f"Tu dois atteindre le niveau {quiz.level_required - 1} pour débloquer ce quiz!",
            "required_level": quiz.level_required
        }), 403
    
    # Get questions (without correct answers in response)
    questions = Question.query.filter_by(quiz_id=quiz_id).all()
    
    questions_data = []
    for q in questions:
        questions_data.append({
            "id": q.id,
            "question_text": q.question_text,
            "option_a": q.option_a,
            "option_b": q.option_b,
            "option_c": q.option_c,
            "option_d": q.option_d
            # Note: correct_option not included!
        })
    
    return jsonify({
        "quiz": quiz.to_dict(),
        "questions": questions_data
    })


@quiz_bp.route('/<int:quiz_id>/submit', methods=['POST'])
@jwt_required()
def submit_quiz(quiz_id):
    """Submit quiz answers and get results"""
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({"error": "Utilisateur non trouvé"}), 404
    
    quiz = Quiz.query.get(quiz_id)
    
    if not quiz:
        return jsonify({"error": "Quiz non trouvé"}), 404
    
    data = request.get_json()
    answers = data.get('answers', {})  # {question_id: "A/B/C/D"}
    
    if not answers:
        return jsonify({"error": "Aucune réponse fournie"}), 400
    
    # Get questions
    questions = Question.query.filter_by(quiz_id=quiz_id).all()
    
    if not questions:
        return jsonify({"error": "Quiz vide"}), 400
    
    # Calculate results
    correct_count = 0
    total = len(questions)
    results = []
    
    for q in questions:
        user_answer = answers.get(str(q.id), "").upper()
        is_correct = user_answer == q.correct_option
        
        if is_correct:
            correct_count += 1
        
        results.append({
            "question_id": q.id,
            "question_text": q.question_text,
            "user_answer": user_answer,
            "correct_answer": q.correct_option,
            "is_correct": is_correct,
            "options": {
                "A": q.option_a,
                "B": q.option_b,
                "C": q.option_c,
                "D": q.option_d
            }
        })
    
    # Calculate score
    attempt_result = calculate_attempt_result(correct_count, total)
    
    # Update user stats
    stats_changes = update_user_stats(user, attempt_result, db)
    
    # Save attempt
    attempt = Attempt(
        user_id=user.id,
        quiz_id=quiz_id,
        score_gained=attempt_result["score"] if attempt_result["passed"] else 0,
        correct_answers=correct_count,
        total_questions=total,
        passed=attempt_result["passed"]
    )
    db.session.add(attempt)
    db.session.commit()
    
    # Build response
    response = {
        "passed": attempt_result["passed"],
        "percentage": attempt_result["percentage"],
        "correct_answers": correct_count,
        "total_questions": total,
        "score_gained": attempt_result["score"] if attempt_result["passed"] else 0,
        "results": results,
        "user": user.to_dict(),
        "changes": stats_changes
    }
    
    # Add special messages
    if stats_changes["reset_triggered"]:
        response["special_message"] = "😢 3 échecs... Tu repars à zéro! Mais ne t'inquiète pas, c'est l'occasion d'apprendre mieux!"
    elif stats_changes["level_change"] > 0:
        response["special_message"] = f"🎉 LEVEL UP! Tu passes au niveau {user.level}!"
    elif attempt_result["passed"]:
        response["special_message"] = f"✨ Bravo! +{attempt_result['score']} points!"
    else:
        fails_left = 3 - user.fail_count
        response["special_message"] = f"😅 Pas cette fois... Encore {fails_left} essai(s) avant le reset!"
    
    return jsonify(response)


@quiz_bp.route('/history', methods=['GET'])
@jwt_required()
def get_history():
    """Get user's quiz history"""
    user_id = get_jwt_identity()
    
    attempts = Attempt.query.filter_by(user_id=user_id).order_by(
        Attempt.completed_at.desc()
    ).limit(20).all()
    
    history = []
    for a in attempts:
        quiz = Quiz.query.get(a.quiz_id)
        history.append({
            "id": a.id,
            "quiz_title": quiz.title if quiz else "Quiz supprimé",
            "quiz_subject": quiz.subject if quiz else "?",
            "score_gained": a.score_gained,
            "correct_answers": a.correct_answers,
            "total_questions": a.total_questions,
            "passed": a.passed,
            "completed_at": a.completed_at.isoformat()
        })
    
    return jsonify({"history": history})
