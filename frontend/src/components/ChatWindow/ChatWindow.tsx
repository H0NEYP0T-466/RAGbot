import { useRef, useEffect } from 'react';
import ChatMessage from '../ChatMessage/ChatMessage';
import LoadingIndicator from '../LoadingIndicator/LoadingIndicator';
import type { Message } from '../../types';
import './ChatWindow.css';

interface ChatWindowProps {
  messages: Message[];
  isLoading: boolean;
}

function ChatWindow({ messages, isLoading }: ChatWindowProps) {
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isLoading]);

  return (
    <div className="chat-window">
      {messages.length === 0 ? (
        <div className="chat-window-empty">
          <div className="empty-icon">
            <svg viewBox="0 0 24 24" fill="currentColor">
              <path d="M20 9V7c0-1.1-.9-2-2-2h-3c0-1.66-1.34-3-3-3S9 3.34 9 5H6c-1.1 0-2 .9-2 2v2c-1.66 0-3 1.34-3 3s1.34 3 3 3v4c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2v-4c1.66 0 3-1.34 3-3s-1.34-3-3-3zM7.5 11.5c0-.83.67-1.5 1.5-1.5s1.5.67 1.5 1.5S9.83 13 9 13s-1.5-.67-1.5-1.5zM16 17H8v-2h8v2zm-1-4c-.83 0-1.5-.67-1.5-1.5S14.17 10 15 10s1.5.67 1.5 1.5S15.83 13 15 13z" />
            </svg>
          </div>
          <h2>Welcome to RAG Chatbot</h2>
          <p>Ask me anything about the documents in the knowledge base!</p>
          <div className="empty-features">
            <div className="feature">
              <span className="feature-icon">📚</span>
              <span>Document-based answers</span>
            </div>
            <div className="feature">
              <span className="feature-icon">🔍</span>
              <span>Semantic search</span>
            </div>
            <div className="feature">
              <span className="feature-icon">✨</span>
              <span>AI-powered responses</span>
            </div>
          </div>
        </div>
      ) : (
        <div className="chat-messages">
          {messages.map((message) => (
            <ChatMessage key={message.id} message={message} />
          ))}
          {isLoading && (
            <div className="loading-wrapper">
              <div className="message-avatar">
                <div className="avatar bot-avatar">
                  <svg viewBox="0 0 24 24" fill="currentColor">
                    <path d="M20 9V7c0-1.1-.9-2-2-2h-3c0-1.66-1.34-3-3-3S9 3.34 9 5H6c-1.1 0-2 .9-2 2v2c-1.66 0-3 1.34-3 3s1.34 3 3 3v4c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2v-4c1.66 0 3-1.34 3-3s-1.34-3-3-3zM7.5 11.5c0-.83.67-1.5 1.5-1.5s1.5.67 1.5 1.5S9.83 13 9 13s-1.5-.67-1.5-1.5zM16 17H8v-2h8v2zm-1-4c-.83 0-1.5-.67-1.5-1.5S14.17 10 15 10s1.5.67 1.5 1.5S15.83 13 15 13z" />
                  </svg>
                </div>
              </div>
              <LoadingIndicator />
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>
      )}
    </div>
  );
}

export default ChatWindow;
