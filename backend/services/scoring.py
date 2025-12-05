"""Scoring and level adaptation service"""

from datetime import datetime, timedelta


def calculate_attempt_result(correct_answers: int, total_questions: int) -> dict:
    """
    Calculate quiz attempt results
    Returns score and whether user passed (80%+ = pass)
    """
    if total_questions == 0:
        return {"score": 0, "percentage": 0, "passed": False}
    
    percentage = (correct_answers / total_questions) * 100
    passed = percentage >= 80
    
    # Base score calculation
    base_score = correct_answers * 10
    
    # Bonus for perfect score
    if percentage == 100:
        base_score += 20
    elif passed:
        base_score += 10
    
    return {
        "score": base_score,
        "percentage": round(percentage, 1),
        "passed": passed
    }


def update_user_stats(user, attempt_result: dict, db) -> dict:
    """
    Update user stats based on attempt result
    - Pass: +score, +streak, reset fail_count
    - Fail: +fail_count, if fail_count >= 3 → reset to level 1
    """
    changes = {
        "score_change": 0,
        "level_change": 0,
        "streak_change": 0,
        "reset_triggered": False
    }
    
    if attempt_result["passed"]:
        # Success!
        user.score += attempt_result["score"]
        changes["score_change"] = attempt_result["score"]
        
        # Check streak (daily activity)
        today = datetime.utcnow().date()
        if user.last_activity:
            last_date = user.last_activity.date()
            if last_date == today - timedelta(days=1):
                # Consecutive day
                user.streak += 1
                changes["streak_change"] = 1
            elif last_date != today:
                # Streak broken
                user.streak = 1
        else:
            user.streak = 1
        
        # Level up check (every 100 points = level up)
        new_level = (user.score // 100) + 1
        if new_level > user.level:
            changes["level_change"] = new_level - user.level
            user.level = new_level
        
        # Reset fail count on success
        user.fail_count = 0
        
    else:
        # Failed
        user.fail_count += 1
        
        # 3 fails = reset to 0
        if user.fail_count >= 3:
            user.score = 0
            user.level = 1
            user.streak = 0
            user.fail_count = 0
            changes["reset_triggered"] = True
    
    user.last_activity = datetime.utcnow()
    db.session.commit()
    
    return changes


def get_recommended_quizzes(user, Quiz, limit: int = 5) -> list:
    """
    Get quizzes recommended for user's level
    Returns quizzes at current level and one level above
    """
    quizzes = Quiz.query.filter(
        Quiz.level_required <= user.level + 1
    ).order_by(Quiz.level_required.desc()).limit(limit).all()
    
    return quizzes


def calculate_leaderboard_rank(user, User) -> int:
    """Calculate user's rank on leaderboard"""
    higher_scores = User.query.filter(User.score > user.score).count()
    return higher_scores + 1
