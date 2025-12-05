import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

function QuizList({ user }) {
  const [quizzes, setQuizzes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [filter, setFilter] = useState('all');

  useEffect(() => {
    loadQuizzes();
  }, []);

  const loadQuizzes = async () => {
    try {
      const response = await axios.get('/quiz/');
      setQuizzes(response.data.quizzes || []);
    } catch (error) {
      console.error('Error loading quizzes:', error);
    }
    setLoading(false);
  };

  const subjectEmojis = {
    math: '🔢',
    french: '📖',
    science: '🔬',
    history: '📜',
    geography: '🌍',
    programming: '💻',
    english: '🇬🇧',
    music: '🎵',
    sports: '⚽',
    art: '🎨',
    philosophy: '🤔',
    economics: '💰',
    default: '📚'
  };

  const subjectNames = {
    math: 'Mathématiques',
    french: 'Français',
    science: 'Sciences',
    history: 'Histoire',
    geography: 'Géographie',
    programming: 'Programmation',
    english: 'Anglais',
    music: 'Musique',
    sports: 'Sports',
    art: 'Art',
    philosophy: 'Philosophie',
    economics: 'Économie'
  };

  const filteredQuizzes = filter === 'all' 
    ? quizzes 
    : quizzes.filter(q => q.subject === filter);

  const subjects = [...new Set(quizzes.map(q => q.subject))];

  return (
    <div className="max-w-6xl mx-auto p-6">
      {/* Header */}
      <div className="mb-8">
        <h1 className="text-3xl font-extrabold text-gray-800 mb-2">
          📚 Tous les Quiz
        </h1>
        <p className="text-gray-500">
          Tu es niveau {user.level} - Tu peux accéder aux quiz jusqu'au niveau {user.level + 1}
        </p>
      </div>

      {/* Filters */}
      <div className="flex flex-wrap gap-2 mb-6">
        <button
          onClick={() => setFilter('all')}
          className={`px-4 py-2 rounded-full font-semibold transition-all ${
            filter === 'all' 
              ? 'bg-primary text-white' 
              : 'bg-white text-gray-600 hover:bg-gray-100'
          }`}
        >
          Tous
        </button>
        {subjects.map(subject => (
          <button
            key={subject}
            onClick={() => setFilter(subject)}
            className={`px-4 py-2 rounded-full font-semibold transition-all ${
              filter === subject 
                ? 'bg-primary text-white' 
                : 'bg-white text-gray-600 hover:bg-gray-100'
            }`}
          >
            {subjectEmojis[subject] || '📚'} {subjectNames[subject] || subject}
          </button>
        ))}
      </div>

      {/* Quiz Grid */}
      {loading ? (
        <div className="text-center py-12">
          <div className="text-5xl animate-bounce mb-4">📚</div>
          <p className="text-gray-500">Chargement des quiz...</p>
        </div>
      ) : (
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredQuizzes.map((quiz) => {
            const isLocked = quiz.level_required > user.level + 1;
            
            return (
              <div
                key={quiz.id}
                className={`bg-white rounded-2xl p-6 shadow-lg transition-all ${
                  isLocked ? 'opacity-60' : 'card-hover'
                }`}
              >
                <div className="flex items-start gap-4 mb-4">
                  <span className="text-4xl">
                    {isLocked ? '🔒' : (subjectEmojis[quiz.subject] || subjectEmojis.default)}
                  </span>
                  <div className="flex-1">
                    <h3 className="font-bold text-gray-800 text-lg">{quiz.title}</h3>
                    <p className="text-sm text-gray-500 mt-1">
                      {subjectNames[quiz.subject] || quiz.subject}
                    </p>
                  </div>
                </div>

                <div className="flex items-center justify-between">
                  <span className={`text-sm px-3 py-1 rounded-full ${
                    quiz.level_required <= user.level 
                      ? 'bg-green-100 text-green-600' 
                      : quiz.level_required === user.level + 1
                        ? 'bg-yellow-100 text-yellow-600'
                        : 'bg-gray-100 text-gray-500'
                  }`}>
                    Niveau {quiz.level_required}
                  </span>

                  {isLocked ? (
                    <span className="text-gray-400 font-medium">
                      🔒 Atteins le niveau {quiz.level_required - 1}
                    </span>
                  ) : (
                    <Link
                      to={`/quiz/${quiz.id}`}
                      className="bg-primary text-white px-4 py-2 rounded-xl font-bold hover:bg-secondary transition-colors"
                    >
                      Jouer! 🎮
                    </Link>
                  )}
                </div>
              </div>
            );
          })}
        </div>
      )}

      {filteredQuizzes.length === 0 && !loading && (
        <div className="text-center py-12 bg-white rounded-2xl shadow">
          <div className="text-5xl mb-4">🔍</div>
          <p className="text-gray-600 text-lg">Aucun quiz trouvé dans cette catégorie</p>
          <button 
            onClick={() => setFilter('all')}
            className="mt-4 text-primary font-bold hover:underline"
          >
            Voir tous les quiz
          </button>
        </div>
      )}
    </div>
  );
}

export default QuizList;
