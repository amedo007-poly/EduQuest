import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axios from 'axios';

function QuizPlay({ user, updateUser }) {
  const { id } = useParams();
  const navigate = useNavigate();
  
  const [quiz, setQuiz] = useState(null);
  const [questions, setQuestions] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [answers, setAnswers] = useState({});
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    loadQuiz();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [id]);

  const loadQuiz = async () => {
    try {
      const response = await axios.get(`/quiz/${id}`);
      setQuiz(response.data.quiz);
      setQuestions(response.data.questions);
    } catch (err) {
      setError(err.response?.data?.error || 'Erreur lors du chargement');
    }
    setLoading(false);
  };

  const handleAnswer = (questionId, option) => {
    setAnswers(prev => ({
      ...prev,
      [questionId]: option
    }));
  };

  const handleNext = () => {
    if (currentIndex < questions.length - 1) {
      setCurrentIndex(prev => prev + 1);
    }
  };

  const handlePrev = () => {
    if (currentIndex > 0) {
      setCurrentIndex(prev => prev - 1);
    }
  };

  const handleSubmit = async () => {
    // Check all answered
    if (Object.keys(answers).length < questions.length) {
      const unanswered = questions.length - Object.keys(answers).length;
      if (!window.confirm(`Tu n'as pas répondu à ${unanswered} question(s). Soumettre quand même?`)) {
        return;
      }
    }

    setSubmitting(true);
    try {
      const response = await axios.post(`/quiz/${id}/submit`, { answers });
      // Update user in parent
      if (response.data.user) {
        updateUser(response.data.user);
      }
      // Navigate to results
      navigate('/result', { state: { result: response.data } });
    } catch (err) {
      setError(err.response?.data?.error || 'Erreur lors de la soumission');
    }
    setSubmitting(false);
  };

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center">
          <div className="text-6xl animate-bounce mb-4">📝</div>
          <p className="text-gray-500 text-lg">Chargement du quiz...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="max-w-2xl mx-auto p-6">
        <div className="bg-red-50 rounded-2xl p-8 text-center">
          <div className="text-5xl mb-4">😕</div>
          <h2 className="text-xl font-bold text-red-600 mb-2">Oups!</h2>
          <p className="text-red-500">{error}</p>
          <button
            onClick={() => navigate('/quizzes')}
            className="mt-4 bg-primary text-white px-6 py-2 rounded-xl font-bold"
          >
            Retour aux quiz
          </button>
        </div>
      </div>
    );
  }

  const currentQuestion = questions[currentIndex];
  const progress = ((currentIndex + 1) / questions.length) * 100;

  return (
    <div className="max-w-3xl mx-auto p-6">
      {/* Header */}
      <div className="mb-6">
        <h1 className="text-2xl font-extrabold text-gray-800">{quiz?.title}</h1>
        <div className="flex items-center gap-4 mt-2">
          <span className="text-gray-500">
            Question {currentIndex + 1} / {questions.length}
          </span>
          <span className="text-gray-500">|</span>
          <span className="text-gray-500">
            {Object.keys(answers).length} répondue(s)
          </span>
        </div>
      </div>

      {/* Progress Bar */}
      <div className="w-full h-3 bg-gray-200 rounded-full mb-8 overflow-hidden">
        <div 
          className="h-full gradient-bg transition-all duration-300"
          style={{ width: `${progress}%` }}
        />
      </div>

      {/* Question Card */}
      <div className="bg-white rounded-3xl shadow-xl p-8 mb-6">
        <h2 className="text-xl font-bold text-gray-800 mb-6">
          {currentQuestion?.question_text}
        </h2>

        {/* Options */}
        <div className="space-y-3">
          {['A', 'B', 'C', 'D'].map((option) => {
            const optionKey = `option_${option.toLowerCase()}`;
            const isSelected = answers[currentQuestion?.id] === option;
            
            return (
              <button
                key={option}
                onClick={() => handleAnswer(currentQuestion.id, option)}
                className={`w-full p-4 rounded-xl text-left transition-all flex items-center gap-4 ${
                  isSelected 
                    ? 'bg-primary text-white shadow-lg' 
                    : 'bg-gray-50 hover:bg-gray-100 text-gray-700'
                }`}
              >
                <span className={`w-10 h-10 rounded-full flex items-center justify-center font-bold ${
                  isSelected ? 'bg-white/20' : 'bg-white'
                }`}>
                  {option}
                </span>
                <span className="flex-1 font-medium">
                  {currentQuestion?.[optionKey]}
                </span>
                {isSelected && <span className="text-2xl">✓</span>}
              </button>
            );
          })}
        </div>
      </div>

      {/* Navigation */}
      <div className="flex justify-between items-center">
        <button
          onClick={handlePrev}
          disabled={currentIndex === 0}
          className="px-6 py-3 rounded-xl font-bold transition-all disabled:opacity-50 disabled:cursor-not-allowed bg-gray-100 text-gray-700 hover:bg-gray-200"
        >
          ← Précédent
        </button>

        {currentIndex === questions.length - 1 ? (
          <button
            onClick={handleSubmit}
            disabled={submitting}
            className="px-8 py-3 rounded-xl font-bold gradient-bg text-white hover:opacity-90 transition-opacity disabled:opacity-50"
          >
            {submitting ? '⏳ Envoi...' : '🚀 Terminer le quiz!'}
          </button>
        ) : (
          <button
            onClick={handleNext}
            className="px-6 py-3 rounded-xl font-bold bg-primary text-white hover:bg-secondary transition-colors"
          >
            Suivant →
          </button>
        )}
      </div>

      {/* Question dots */}
      <div className="flex justify-center gap-2 mt-8 flex-wrap">
        {questions.map((q, index) => (
          <button
            key={q.id}
            onClick={() => setCurrentIndex(index)}
            className={`w-8 h-8 rounded-full font-bold text-sm transition-all ${
              index === currentIndex
                ? 'bg-primary text-white scale-110'
                : answers[q.id]
                  ? 'bg-green-500 text-white'
                  : 'bg-gray-200 text-gray-500 hover:bg-gray-300'
            }`}
          >
            {index + 1}
          </button>
        ))}
      </div>
    </div>
  );
}

export default QuizPlay;
