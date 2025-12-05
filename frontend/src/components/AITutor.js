import React, { useState, useRef, useEffect } from 'react';
import axios from 'axios';

function AITutor({ user }) {
  const [messages, setMessages] = useState([
    {
      role: 'assistant',
      content: `Salut ${user.username}! 👋 Je suis EduBot, ton tuteur IA personnel!\n\nJe suis là pour t'aider à comprendre tes erreurs et t'expliquer les concepts. Pose-moi toutes tes questions! 🎓`
    }
  ]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const sendMessage = async (e) => {
    e.preventDefault();
    if (!input.trim() || loading) return;

    const userMessage = input.trim();
    setInput('');
    setMessages(prev => [...prev, { role: 'user', content: userMessage }]);
    setLoading(true);

    try {
      const response = await axios.post('/ai/chat', { message: userMessage });
      setMessages(prev => [...prev, { 
        role: 'assistant', 
        content: response.data.response 
      }]);
    } catch (error) {
      console.error('AI Chat error:', error.response?.data || error.message);
      setMessages(prev => [...prev, { 
        role: 'assistant', 
        content: "Oups! J'ai eu un petit souci. Réessaie! 🔧" 
      }]);
    }
    setLoading(false);
  };

  const quickQuestions = [
    "Comment résoudre une équation?",
    "Explique-moi les fractions",
    "C'est quoi un adverbe?",
    "Aide-moi avec mes erreurs"
  ];

  return (
    <div className="max-w-3xl mx-auto p-6 h-[calc(100vh-120px)] flex flex-col">
      {/* Header */}
      <div className="flex items-center gap-4 mb-6">
        <div className="text-5xl">🤖</div>
        <div>
          <h1 className="text-2xl font-extrabold text-gray-800">EduBot</h1>
          <p className="text-gray-500">Ton tuteur IA personnel</p>
        </div>
      </div>

      {/* Chat Container */}
      <div className="flex-1 bg-white rounded-2xl shadow-lg overflow-hidden flex flex-col">
        {/* Messages */}
        <div className="flex-1 overflow-y-auto p-4 space-y-4">
          {messages.map((msg, index) => (
            <div
              key={index}
              className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}
            >
              <div
                className={`max-w-[80%] p-4 rounded-2xl ${
                  msg.role === 'user'
                    ? 'bg-primary text-white rounded-br-md'
                    : 'bg-gray-100 text-gray-800 rounded-bl-md'
                }`}
              >
                {msg.role === 'assistant' && (
                  <span className="text-2xl mr-2">🤖</span>
                )}
                <span className="whitespace-pre-wrap">{msg.content}</span>
              </div>
            </div>
          ))}

          {loading && (
            <div className="flex justify-start">
              <div className="bg-gray-100 p-4 rounded-2xl rounded-bl-md">
                <span className="text-2xl mr-2">🤖</span>
                <span className="animate-pulse">Je réfléchis...</span>
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        {/* Quick Questions */}
        {messages.length <= 1 && (
          <div className="p-4 border-t bg-gray-50">
            <p className="text-sm text-gray-500 mb-2">💡 Suggestions:</p>
            <div className="flex flex-wrap gap-2">
              {quickQuestions.map((q, i) => (
                <button
                  key={i}
                  onClick={() => setInput(q)}
                  className="text-sm bg-white border border-gray-200 px-3 py-1 rounded-full hover:border-primary hover:text-primary transition-colors"
                >
                  {q}
                </button>
              ))}
            </div>
          </div>
        )}

        {/* Input */}
        <form onSubmit={sendMessage} className="p-4 border-t bg-white">
          <div className="flex gap-2">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Pose ta question..."
              className="flex-1 px-4 py-3 rounded-xl border-2 border-gray-200 focus:border-primary focus:outline-none transition-colors"
              disabled={loading}
              maxLength={1000}
            />
            <button
              type="submit"
              disabled={loading || !input.trim()}
              className="px-6 py-3 rounded-xl font-bold gradient-bg text-white hover:opacity-90 transition-opacity disabled:opacity-50"
            >
              {loading ? '⏳' : '📤'}
            </button>
          </div>
        </form>
      </div>

      {/* Stats reminder */}
      <div className="mt-4 flex justify-center gap-4 text-sm text-gray-500">
        <span>📊 Niveau {user.level}</span>
        <span>•</span>
        <span>⭐ {user.score} points</span>
        <span>•</span>
        <span>🔥 {user.streak} jours</span>
      </div>
    </div>
  );
}

export default AITutor;
