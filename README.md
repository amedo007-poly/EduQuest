# 🎓 EduQuest - Village Numérique Résistant

> Plateforme d'apprentissage gamifiée, open-source, propulsée par l'IA
> "L'éducation libre contre les Big Tech"

## 🎯 Concept

Une plateforme éducative inspirée de Duolingo mais **100% open-source et gratuite** que les écoles peuvent héberger elles-mêmes. Elle utilise une IA éthique (DeepSeek) pour personnaliser les quiz, motiver les élèves avec des streaks et des classements.

## 🚀 Quick Start

```bash
docker-compose up --build
```
Ouvrir http://localhost:3000

## ✨ Fonctionnalités

### 🧠 Section 1 - IA Adaptative
- Profil personnalisé par étudiant
- Recommandation de quiz selon le niveau
- Chatbot tuteur IA (DeepSeek)

### 🎮 Section 2 - Gamification (Duolingo-style)
- Quiz adaptatifs
- Système de scoring
- Streaks quotidiens
- Leaderboard
- Règle des 3 échecs → reset score

### 🏫 Section 3 - Souveraineté Numérique
- 100% Open Source
- Auto-hébergeable
- Pas de tracking
- Données restent à l'école

## 🛠️ Stack

- **Frontend:** React + TailwindCSS
- **Backend:** Flask + SQLAlchemy
- **Database:** SQLite (dev) / PostgreSQL (prod)
- **IA:** DeepSeek via OpenRouter

## 📁 Structure

```
EduQuest/
├── frontend/           # React app
├── backend/            # Flask API
├── docker-compose.yml
└── README.md
```

## 🏆 Équipe

- **Développeur:** Ahmed Dinari
- **École:** École Polytechnique de Sousse
- **Challenge:** Défi National Nuit de l'Info 2025

---
Made with ❤️ for open education
