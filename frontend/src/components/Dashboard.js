import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

function Dashboard({ user }) {
  const [quizzes, setQuizzes] = useState([]);
  const [encouragement, setEncouragement] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      const [quizzesRes, encourageRes] = await Promise.all([
        axios.get('/quiz/recommended'),
        axios.get('/ai/encourage')
      ]);
      setQuizzes(quizzesRes.data.quizzes);
      setEncouragement(encourageRes.data.message);
    } catch (error) {
      console.error('Error loading dashboard:', error);
    }
    setLoading(false);
  };

  const subjectEmojis = {
    math: '🔢',
    french: '📖',
    science: '🔬',
    history: '🏛️',
    geography: '🌍',
    default: '📚'
  };

  return (
    <div className="max-w-6xl mx-auto p-6">
      {/* Welcome Card */}
      <div className="gradient-bg rounded-3xl p-8 mb-8 text-white">
        <div className="flex items-center justify-between flex-wrap gap-4">
          <div>
            <h1 className="text-3xl font-extrabold mb-2">
              Salut {user.username}! {user.avatar || '👋'}
            </h1>
            <p className="text-white/80 text-lg">{encouragement || 'Prêt à apprendre?'}</p>
          </div>
          
          {/* Stats */}
          <div className="flex gap-4">
            <div className="bg-white/20 backdrop-blur rounded-2xl p-4 text-center">
              <div className="text-3xl font-extrabold">{user.level}</div>
              <div className="text-white/80 text-sm">Niveau</div>
            </div>
            <div className="bg-white/20 backdrop-blur rounded-2xl p-4 text-center">
              <div className="text-3xl font-extrabold">{user.score}</div>
              <div className="text-white/80 text-sm">Points</div>
            </div>
            <div className="bg-white/20 backdrop-blur rounded-2xl p-4 text-center">
              <div className="text-3xl font-extrabold">
                {user.streak > 0 ? `🔥${user.streak}` : '0'}
              </div>
              <div className="text-white/80 text-sm">Streak</div>
            </div>
          </div>
        </div>

        {/* Warning if close to reset */}
        {user.fail_count > 0 && (
          <div className="mt-4 bg-red-500/30 rounded-xl p-3">
            ⚠️ Attention! {3 - user.fail_count} échec(s) restant(s) avant le reset!
          </div>
        )}
      </div>

      {/* Quick Actions */}
      <div className="grid md:grid-cols-3 gap-6 mb-8">
        <Link 
          to="/quizzes" 
          className="bg-white rounded-2xl p-6 shadow-lg card-hover transition-all text-center"
        >
          <div className="text-5xl mb-4">📚</div>
          <h3 className="text-xl font-bold text-gray-800">Tous les Quiz</h3>
          <p className="text-gray-500 mt-2">Explore tous les quiz disponibles</p>
        </Link>

        <Link 
          to="/leaderboard" 
          className="bg-white rounded-2xl p-6 shadow-lg card-hover transition-all text-center"
        >
          <div className="text-5xl mb-4">🏆</div>
          <h3 className="text-xl font-bold text-gray-800">Classement</h3>
          <p className="text-gray-500 mt-2">Vois où tu te situes!</p>
        </Link>

        <Link 
          to="/tutor" 
          className="bg-white rounded-2xl p-6 shadow-lg card-hover transition-all text-center"
        >
          <div className="text-5xl mb-4">🤖</div>
          <h3 className="text-xl font-bold text-gray-800">Tuteur IA</h3>
          <p className="text-gray-500 mt-2">Pose tes questions!</p>
        </Link>
      </div>

      {/* Recommended Quizzes */}
      <h2 className="text-2xl font-extrabold text-gray-800 mb-4">
        📌 Quiz Recommandés
      </h2>

      {loading ? (
        <div className="text-center py-8">
          <div className="text-4xl animate-bounce">⏳</div>
          <p className="text-gray-500 mt-2">Chargement...</p>
        </div>
      ) : (
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
          {quizzes.map((quiz) => (
            <Link
              key={quiz.id}
              to={`/quiz/${quiz.id}`}
              className="bg-white rounded-2xl p-5 shadow-lg card-hover transition-all"
            >
              <div className="flex items-center gap-3 mb-3">
                <span className="text-3xl">
                  {subjectEmojis[quiz.subject] || subjectEmojis.default}
                </span>
                <div>
                  <h3 className="font-bold text-gray-800">{quiz.title}</h3>
                  <p className="text-sm text-gray-500">Niveau requis: {quiz.level_required}</p>
                </div>
              </div>
              <div className="flex justify-between items-center">
                <span className="text-xs bg-primary/10 text-primary px-2 py-1 rounded-full">
                  {quiz.subject}
                </span>
                <span className="text-primary font-bold">Jouer →</span>
              </div>
            </Link>
          ))}
        </div>
      )}

      {quizzes.length === 0 && !loading && (
        <div className="text-center py-8 bg-white rounded-2xl shadow">
          <div className="text-5xl mb-4">🎉</div>
          <p className="text-gray-600">Tu as fait tous les quiz disponibles!</p>
          <p className="text-gray-500">Reviens bientôt pour de nouveaux contenus.</p>
        </div>
      )}
    </div>
  );
}

export default Dashboard;
