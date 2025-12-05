import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Leaderboard({ user }) {
  const [leaderboard, setLeaderboard] = useState([]);
  const [streaks, setStreaks] = useState([]);
  const [currentRank, setCurrentRank] = useState(null);
  const [activeTab, setActiveTab] = useState('score');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadLeaderboard();
  }, []);

  const loadLeaderboard = async () => {
    try {
      const [scoreRes, streakRes] = await Promise.all([
        axios.get('/leaderboard/'),
        axios.get('/leaderboard/streaks')
      ]);
      setLeaderboard(scoreRes.data.leaderboard);
      setCurrentRank(scoreRes.data.current_user_rank);
      setStreaks(streakRes.data.streaks);
    } catch (error) {
      console.error('Error loading leaderboard:', error);
    }
    setLoading(false);
  };

  const getMedal = (rank) => {
    switch(rank) {
      case 1: return '🥇';
      case 2: return '🥈';
      case 3: return '🥉';
      default: return rank;
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center">
          <div className="text-6xl animate-bounce mb-4">🏆</div>
          <p className="text-gray-500">Chargement du classement...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-4xl mx-auto p-6">
      {/* Header */}
      <div className="text-center mb-8">
        <h1 className="text-3xl font-extrabold text-gray-800 mb-2">
          🏆 Classement
        </h1>
        {currentRank && (
          <p className="text-gray-500">
            Tu es actuellement à la <span className="font-bold text-primary">#{currentRank}ème</span> place!
          </p>
        )}
      </div>

      {/* Tabs */}
      <div className="flex justify-center gap-4 mb-8">
        <button
          onClick={() => setActiveTab('score')}
          className={`px-6 py-3 rounded-xl font-bold transition-all ${
            activeTab === 'score' 
              ? 'gradient-bg text-white' 
              : 'bg-white text-gray-600 hover:bg-gray-100'
          }`}
        >
          ⭐ Par points
        </button>
        <button
          onClick={() => setActiveTab('streak')}
          className={`px-6 py-3 rounded-xl font-bold transition-all ${
            activeTab === 'streak' 
              ? 'bg-gradient-to-r from-orange-400 to-red-500 text-white' 
              : 'bg-white text-gray-600 hover:bg-gray-100'
          }`}
        >
          🔥 Par streak
        </button>
      </div>

      {/* Podium for top 3 (score tab) */}
      {activeTab === 'score' && leaderboard.length >= 3 && (
        <div className="flex justify-center items-end gap-4 mb-8">
          {/* 2nd place */}
          <div className="bg-white rounded-2xl p-4 shadow-lg text-center w-32">
            <div className="text-4xl mb-2">🥈</div>
            <div className="text-3xl mb-2">{leaderboard[1]?.avatar || '😊'}</div>
            <p className="font-bold text-gray-800 truncate">{leaderboard[1]?.username}</p>
            <p className="text-primary font-bold">⭐ {leaderboard[1]?.score}</p>
          </div>

          {/* 1st place */}
          <div className="bg-gradient-to-br from-yellow-100 to-yellow-200 rounded-2xl p-6 shadow-xl text-center w-40 transform scale-110">
            <div className="text-5xl mb-2">🥇</div>
            <div className="text-4xl mb-2">{leaderboard[0]?.avatar || '😊'}</div>
            <p className="font-bold text-gray-800 truncate text-lg">{leaderboard[0]?.username}</p>
            <p className="text-primary font-bold text-xl">⭐ {leaderboard[0]?.score}</p>
          </div>

          {/* 3rd place */}
          <div className="bg-white rounded-2xl p-4 shadow-lg text-center w-32">
            <div className="text-4xl mb-2">🥉</div>
            <div className="text-3xl mb-2">{leaderboard[2]?.avatar || '😊'}</div>
            <p className="font-bold text-gray-800 truncate">{leaderboard[2]?.username}</p>
            <p className="text-primary font-bold">⭐ {leaderboard[2]?.score}</p>
          </div>
        </div>
      )}

      {/* Leaderboard List */}
      <div className="bg-white rounded-2xl shadow-lg overflow-hidden">
        {activeTab === 'score' ? (
          <div className="divide-y">
            {leaderboard.map((player, index) => (
              <div
                key={index}
                className={`flex items-center gap-4 p-4 transition-colors ${
                  player.is_current_user ? 'bg-primary/10' : 'hover:bg-gray-50'
                }`}
              >
                <div className="w-12 text-center font-bold text-xl">
                  {index < 3 ? getMedal(index + 1) : `#${player.rank}`}
                </div>
                <div className="text-3xl">
                  {player.avatar || '😊'}
                </div>
                <div className="flex-1">
                  <p className={`font-bold ${player.is_current_user ? 'text-primary' : 'text-gray-800'}`}>
                    {player.username}
                    {player.is_current_user && ' (Toi!)'}
                  </p>
                  <p className="text-sm text-gray-500">
                    Niveau {player.level} • 🔥 {player.streak} jours
                  </p>
                </div>
                <div className="text-right">
                  <p className="text-xl font-bold text-primary">⭐ {player.score}</p>
                </div>
              </div>
            ))}
          </div>
        ) : (
          <div className="divide-y">
            {streaks.map((player, index) => (
              <div
                key={index}
                className="flex items-center gap-4 p-4 hover:bg-gray-50 transition-colors"
              >
                <div className="w-12 text-center font-bold text-xl">
                  #{player.rank}
                </div>
                <div className="text-3xl">
                  {player.avatar || '😊'}
                </div>
                <div className="flex-1">
                  <p className="font-bold text-gray-800">{player.username}</p>
                </div>
                <div className="text-right">
                  <p className="text-xl font-bold text-orange-500">
                    🔥 {player.streak} jours
                  </p>
                  <p className="text-sm">{player.fire}</p>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      {(activeTab === 'score' ? leaderboard : streaks).length === 0 && (
        <div className="text-center py-12 bg-white rounded-2xl shadow">
          <div className="text-5xl mb-4">👀</div>
          <p className="text-gray-600">Personne encore dans le classement!</p>
          <p className="text-gray-500">Sois le premier à jouer!</p>
        </div>
      )}
    </div>
  );
}

export default Leaderboard;
