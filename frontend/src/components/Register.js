import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

function Register({ onLogin }) {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      const response = await axios.post('/auth/register', { 
        username, 
        email, 
        password 
      });
      onLogin(response.data.user, response.data.token);
    } catch (err) {
      setError(err.response?.data?.error || 'Erreur lors de l\'inscription');
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen gradient-bg flex items-center justify-center p-4">
      <div className="bg-white rounded-3xl shadow-2xl p-8 w-full max-w-md">
        {/* Logo */}
        <div className="text-center mb-8">
          <div className="text-6xl mb-4">🎓</div>
          <h1 className="text-3xl font-extrabold text-dark">Rejoins EduQuest!</h1>
          <p className="text-gray-500 mt-2">Crée ton compte et commence l'aventure</p>
        </div>

        {/* Error message */}
        {error && (
          <div className="bg-red-50 text-red-600 p-4 rounded-xl mb-6 text-center font-medium">
            {error}
          </div>
        )}

        {/* Form */}
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label className="block text-gray-700 font-semibold mb-2">
              👤 Pseudo
            </label>
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              className="w-full px-4 py-3 rounded-xl border-2 border-gray-200 focus:border-primary focus:outline-none transition-colors"
              placeholder="SuperLearner42"
              minLength={3}
              required
            />
          </div>

          <div className="mb-4">
            <label className="block text-gray-700 font-semibold mb-2">
              📧 Email
            </label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full px-4 py-3 rounded-xl border-2 border-gray-200 focus:border-primary focus:outline-none transition-colors"
              placeholder="ton.email@ecole.fr"
              required
            />
          </div>

          <div className="mb-6">
            <label className="block text-gray-700 font-semibold mb-2">
              🔒 Mot de passe
            </label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full px-4 py-3 rounded-xl border-2 border-gray-200 focus:border-primary focus:outline-none transition-colors"
              placeholder="Au moins 6 caractères"
              minLength={6}
              required
            />
          </div>

          <button
            type="submit"
            disabled={loading}
            className="w-full gradient-bg text-white font-bold py-4 rounded-xl hover:opacity-90 transition-opacity disabled:opacity-50"
          >
            {loading ? '⏳ Inscription...' : '🎉 Créer mon compte'}
          </button>
        </form>

        {/* Login link */}
        <p className="text-center mt-6 text-gray-600">
          Déjà un compte?{' '}
          <Link to="/login" className="text-primary font-bold hover:underline">
            Connecte-toi! 👋
          </Link>
        </p>
      </div>
    </div>
  );
}

export default Register;
