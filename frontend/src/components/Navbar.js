import React from 'react';
import { Link } from 'react-router-dom';

function Navbar({ user, onLogout }) {
  return (
    <nav className="bg-white shadow-lg sticky top-0 z-50">
      <div className="max-w-6xl mx-auto px-4">
        <div className="flex justify-between items-center py-4">
          {/* Logo */}
          <Link to="/dashboard" className="flex items-center space-x-2">
            <span className="text-3xl">🎓</span>
            <span className="text-xl font-extrabold text-dark">EduQuest</span>
          </Link>

          {/* Navigation Links */}
          <div className="hidden md:flex items-center space-x-6">
            <Link 
              to="/dashboard" 
              className="text-gray-600 hover:text-primary font-semibold transition-colors"
            >
              🏠 Accueil
            </Link>
            <Link 
              to="/quizzes" 
              className="text-gray-600 hover:text-primary font-semibold transition-colors"
            >
              📚 Quiz
            </Link>
            <Link 
              to="/leaderboard" 
              className="text-gray-600 hover:text-primary font-semibold transition-colors"
            >
              🏆 Classement
            </Link>
            <Link 
              to="/tutor" 
              className="text-gray-600 hover:text-primary font-semibold transition-colors"
            >
              🤖 Tuteur IA
            </Link>
          </div>

          {/* User Stats */}
          <div className="flex items-center space-x-4">
            {/* Streak */}
            {user.streak > 0 && (
              <div className="flex items-center bg-orange-100 px-3 py-1 rounded-full">
                <span className="streak-fire text-xl">🔥</span>
                <span className="ml-1 font-bold text-orange-600">{user.streak}</span>
              </div>
            )}

            {/* Level */}
            <div className="level-badge px-3 py-1 rounded-full">
              <span className="text-white font-bold">Niv. {user.level}</span>
            </div>

            {/* Score */}
            <div className="bg-primary/10 px-3 py-1 rounded-full">
              <span className="text-primary font-bold">⭐ {user.score}</span>
            </div>

            {/* User Menu */}
            <div className="flex items-center space-x-2">
              <span className="text-2xl">{user.avatar || '😊'}</span>
              <span className="font-semibold text-gray-700 hidden lg:block">
                {user.username}
              </span>
            </div>

            {/* Logout */}
            <button
              onClick={onLogout}
              className="text-gray-400 hover:text-red-500 transition-colors"
              title="Déconnexion"
            >
              🚪
            </button>
          </div>
        </div>

        {/* Mobile Navigation */}
        <div className="md:hidden flex justify-around py-2 border-t">
          <Link to="/dashboard" className="text-2xl">🏠</Link>
          <Link to="/quizzes" className="text-2xl">📚</Link>
          <Link to="/leaderboard" className="text-2xl">🏆</Link>
          <Link to="/tutor" className="text-2xl">🤖</Link>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
