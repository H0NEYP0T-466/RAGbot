import { useState, useCallback } from 'react';
import { v4 as uuidv4 } from 'uuid';
import ChatWindow from './components/ChatWindow/ChatWindow';
import ChatInput from './components/ChatInput/ChatInput';
import apiService from './services/api';
import type { Message } from './types';
import 'katex/dist/katex.min.css';
import './App.css';

function App() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSendMessage = useCallback(async (content: string) => {
    const userMessage: Message = {
      id: uuidv4(),
      role: 'user',
      content,
      timestamp: new Date(),
    };

    setMessages(prev => [...prev, userMessage]);
    setIsLoading(true);
    setError(null);

    try {
      const response = await apiService.sendMessage(content);
      
      const assistantMessage: Message = {
        id: uuidv4(),
        role: 'assistant',
        content: response.response,
        timestamp: new Date(),
        sources: response.sources,
        tokens: response.tokens,
      };

      setMessages(prev => [...prev, assistantMessage]);
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'An unexpected error occurred';
      setError(errorMessage);
      
      const errorAssistantMessage: Message = {
        id: uuidv4(),
        role: 'assistant',
        content: `Sorry, I encountered an error: ${errorMessage}. Please try again.`,
        timestamp: new Date(),
      };

      setMessages(prev => [...prev, errorAssistantMessage]);
    } finally {
      setIsLoading(false);
    }
  }, []);

  const handleClearChat = useCallback(() => {
    setMessages([]);
    setError(null);
  }, []);

  return (
    <div className="app">
      {error && (
        <div className="error-banner">
          <span>{error}</span>
          <button onClick={() => setError(null)}>×</button>
        </div>
      )}
      <ChatWindow
        messages={messages}
        isLoading={isLoading}
        onClearChat={handleClearChat}
      />
      <ChatInput
        onSendMessage={handleSendMessage}
        disabled={isLoading}
      />
    </div>
  );
}

export default App;
