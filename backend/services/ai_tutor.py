"""AI Tutor service using DeepSeek via OpenRouter"""

import requests
import json
from config import Config


SYSTEM_PROMPT = """Tu es EduBot, un tuteur IA bienveillant et pédagogue pour la plateforme EduQuest.

🎓 TON RÔLE:
- Aider les étudiants à comprendre leurs erreurs
- Expliquer les concepts de manière simple et accessible
- Encourager et motiver sans jamais décourager
- Adapter tes explications au niveau de l'élève

📚 TES MATIÈRES:
- Mathématiques (calcul, algèbre, géométrie)
- Français (grammaire, conjugaison, orthographe)
- Sciences (physique, chimie, biologie, SVT)
- Culture générale

💡 TES PRINCIPES:
1. Toujours encourager, même en cas d'erreur
2. Donner des exemples concrets et du quotidien
3. Poser des questions pour faire réfléchir
4. Féliciter les progrès, même petits
5. Jamais donner directement la réponse, guider vers elle

🎮 CONTEXTE GAMIFICATION:
- Les élèves gagnent des points et des niveaux
- 3 échecs = retour au niveau 1 (motive à bien apprendre!)
- Streak quotidien pour récompenser la régularité

Réponds TOUJOURS en français, de manière chaleureuse et pédagogique! 🌟"""


def get_ai_response(user_message: str, context: dict = None) -> str:
    """
    Get AI tutor response using DeepSeek via OpenRouter
    
    context can include:
    - user_level: int
    - last_quiz_subject: str
    - last_quiz_score: int
    - streak: int
    """
    try:
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        
        # Add context if available
        if context:
            context_msg = f"""
Contexte de l'élève:
- Niveau actuel: {context.get('user_level', 1)}
- Streak: {context.get('streak', 0)} jours
"""
            if context.get('last_quiz_subject'):
                context_msg += f"- Dernier quiz: {context.get('last_quiz_subject')} (Score: {context.get('last_quiz_score', 0)}%)\n"
            
            messages.append({"role": "system", "content": context_msg})
        
        messages.append({"role": "user", "content": user_message})
        
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {Config.OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "http://localhost:3000",
                "X-Title": "EduQuest AI Tutor"
            },
            json={
                "model": "tngtech/deepseek-r1t2-chimera:free",
                "messages": messages,
                "max_tokens": 500,
                "temperature": 0.7,
                "presence_penalty": 0.5,
                "frequency_penalty": 0.5
            },
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            return data["choices"][0]["message"]["content"]
        else:
            print(f"API Error: {response.status_code} - {response.text}")
            return "Oups! Je suis un peu fatigué là... Peux-tu reformuler ta question? 🐱"
            
    except requests.exceptions.Timeout:
        return "Je réfléchis trop longtemps! Réessaie dans un instant. 🤔"
    except Exception as e:
        print(f"AI Error: {e}")
        return "Hmm, j'ai un petit souci technique. Réessaie! 🔧"


def explain_wrong_answer(question: str, user_answer: str, correct_answer: str, subject: str) -> str:
    """Generate explanation for a wrong answer"""
    prompt = f"""L'élève a fait une erreur sur cette question:

📝 Question: {question}
❌ Sa réponse: {user_answer}
✅ Bonne réponse: {correct_answer}
📚 Matière: {subject}

Explique-lui pourquoi sa réponse est incorrecte et comment trouver la bonne réponse.
Sois encourageant et pédagogique! Utilise des exemples si possible."""

    return get_ai_response(prompt)


def generate_encouragement(streak: int, level: int, last_score: int) -> str:
    """Generate personalized encouragement message"""
    if streak >= 7:
        return f"🔥 WOW! {streak} jours de suite! Tu es en feu! Continue comme ça, champion!"
    elif last_score >= 80:
        return f"🌟 Excellent travail! {last_score}% c'est super! Tu progresses vraiment bien!"
    elif last_score >= 60:
        return f"👍 Pas mal du tout! Avec un peu plus de pratique, tu vas cartonner!"
    else:
        return f"💪 Chaque erreur est une chance d'apprendre! Révise bien et réessaie!"
