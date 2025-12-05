import React from 'react';
import { useLocation, useNavigate, Link } from 'react-router-dom';

function QuizResult({ user }) {
  const location = useLocation();
  const navigate = useNavigate();
  const result = location.state?.result;

  if (!result) {
    return (
      <div className="max-w-2xl mx-auto p-6 text-center">
        <div className="text-5xl mb-4">🤔</div>
        <p className="text-gray-600">Pas de résultat à afficher</p>
        <Link 
          to="/quizzes" 
          className="inline-block mt-4 bg-primary text-white px-6 py-3 rounded-xl font-bold"
        >
          Aller aux quiz
        </Link>
      </div>
    );
  }

  const { passed, percentage, correct_answers, total_questions, score_gained, results, special_message, changes } = result;

  return (
    <div className="max-w-3xl mx-auto p-6">
      {/* Result Header */}
      <div className={`rounded-3xl p-8 mb-8 text-center text-white ${
        passed ? 'bg-gradient-to-br from-green-400 to-green-600' : 'bg-gradient-to-br from-red-400 to-red-600'
      }`}>
        <div className="text-7xl mb-4">
          {passed ? '🎉' : '😢'}
        </div>
        <h1 className="text-3xl font-extrabold mb-2">
          {passed ? 'Bravo!' : 'Pas cette fois...'}
        </h1>
        <p className="text-white/80 text-lg mb-4">{special_message}</p>

        {/* Score */}
        <div className="flex justify-center gap-6 mt-6">
          <div className="bg-white/20 backdrop-blur rounded-2xl p-4">
            <div className="text-4xl font-extrabold">{percentage}%</div>
            <div className="text-white/80 text-sm">Score</div>
          </div>
          <div className="bg-white/20 backdrop-blur rounded-2xl p-4">
            <div className="text-4xl font-extrabold">{correct_answers}/{total_questions}</div>
            <div className="text-white/80 text-sm">Bonnes réponses</div>
          </div>
          {passed && (
            <div className="bg-white/20 backdrop-blur rounded-2xl p-4">
              <div className="text-4xl font-extrabold">+{score_gained}</div>
              <div className="text-white/80 text-sm">Points gagnés</div>
            </div>
          )}
        </div>

        {/* Level up message */}
        {changes?.level_change > 0 && (
          <div className="mt-6 bg-yellow-400 text-yellow-900 rounded-xl p-4 font-bold animate-pulse">
            🌟 LEVEL UP! Tu passes au niveau {user.level}! 🌟
          </div>
        )}

        {/* Reset warning */}
        {changes?.reset_triggered && (
          <div className="mt-6 bg-black/30 rounded-xl p-4">
            ⚠️ 3 échecs... Tu repars à zéro mais ne t'inquiète pas, c'est l'occasion de tout reprendre!
          </div>
        )}
      </div>

      {/* Detailed Results */}
      <h2 className="text-2xl font-extrabold text-gray-800 mb-4">
        📋 Détail des réponses
      </h2>

      <div className="space-y-4 mb-8">
        {results.map((r, index) => (
          <div
            key={r.question_id}
            className={`bg-white rounded-2xl p-5 shadow-lg border-l-4 ${
              r.is_correct ? 'border-green-500' : 'border-red-500'
            }`}
          >
            <div className="flex items-start gap-3">
              <span className="text-2xl">
                {r.is_correct ? '✅' : '❌'}
              </span>
              <div className="flex-1">
                <p className="font-semibold text-gray-800 mb-2">
                  {index + 1}. {r.question_text}
                </p>
                <div className="text-sm space-y-1">
                  <p className={r.is_correct ? 'text-green-600' : 'text-red-500'}>
                    Ta réponse: <span className="font-bold">{r.options[r.user_answer] || 'Non répondu'}</span>
                  </p>
                  {!r.is_correct && (
                    <p className="text-green-600">
                      Bonne réponse: <span className="font-bold">{r.options[r.correct_answer]}</span>
                    </p>
                  )}
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Actions */}
      <div className="flex flex-wrap justify-center gap-4">
        <button
          onClick={() => navigate(-1)}
          className="px-6 py-3 rounded-xl font-bold bg-gray-100 text-gray-700 hover:bg-gray-200 transition-colors"
        >
          🔄 Réessayer
        </button>
        <Link
          to="/tutor"
          className="px-6 py-3 rounded-xl font-bold bg-secondary text-white hover:opacity-90 transition-opacity"
        >
          🤖 Demander de l'aide à l'IA
        </Link>
        <Link
          to="/quizzes"
          className="px-6 py-3 rounded-xl font-bold gradient-bg text-white hover:opacity-90 transition-opacity"
        >
          📚 Autres quiz
        </Link>
      </div>
    </div>
  );
}

export default QuizResult;
