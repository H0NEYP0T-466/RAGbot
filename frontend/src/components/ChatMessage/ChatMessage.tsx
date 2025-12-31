import ReactMarkdown from 'react-markdown';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import 'katex/dist/katex.min.css';
import type { Components } from 'react-markdown';
import CodeBlock from '../CodeBlock/CodeBlock';
import type { Message } from '../../types';
import './ChatMessage.css';

interface ChatMessageProps {
  message: Message;
}

function ChatMessage({ message }: ChatMessageProps) {
  const isUser = message.role === 'user';

  const formatTime = (date: Date) => {
    return new Date(date).toLocaleTimeString('en-US', {
      hour: '2-digit',
      minute: '2-digit',
    });
  };

  const markdownComponents: Partial<Components> = {
    code({ className, children, ...props }) {
      const match = /language-(\w+)/.exec(className || '');
      const codeString = String(children).replace(/\n$/, '');
      
      // Check if this is inline code (no language specified and short content)
      const isInline = !match && !codeString.includes('\n');
      
      if (isInline) {
        return (
          <code className="inline-code" {...props}>
            {children}
          </code>
        );
      }
      
      return (
        <CodeBlock
          language={match ? match[1] : ''}
          value={codeString}
        />
      );
    },
  };

  return (
    <div className={`chat-message ${isUser ? 'user-message' : 'assistant-message'}`}>
      <div className="message-avatar">
        {isUser ? (
          <div className="avatar user-avatar">
            <svg viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z" />
            </svg>
          </div>
        ) : (
          <div className="avatar bot-avatar">
            <svg viewBox="0 0 24 24" fill="currentColor">
              <path d="M20 9V7c0-1.1-.9-2-2-2h-3c0-1.66-1.34-3-3-3S9 3.34 9 5H6c-1.1 0-2 .9-2 2v2c-1.66 0-3 1.34-3 3s1.34 3 3 3v4c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2v-4c1.66 0 3-1.34 3-3s-1.34-3-3-3zM7.5 11.5c0-.83.67-1.5 1.5-1.5s1.5.67 1.5 1.5S9.83 13 9 13s-1.5-.67-1.5-1.5zM16 17H8v-2h8v2zm-1-4c-.83 0-1.5-.67-1.5-1.5S14.17 10 15 10s1.5.67 1.5 1.5S15.83 13 15 13z" />
            </svg>
          </div>
        )}
      </div>
      <div className="message-content-wrapper">
        <div className="message-content">
          {isUser ? (
            <p>{message.content}</p>
          ) : (
            <ReactMarkdown
              remarkPlugins={[remarkMath]}
              rehypePlugins={[rehypeKatex]}
              components={markdownComponents}
            >
              {message.content}
            </ReactMarkdown>
          )}
        </div>
        <div className="message-meta">
          <span className="message-timestamp">{formatTime(message.timestamp)}</span>
          {message.sources && message.sources.length > 0 && (
            <span className="message-sources">
              Sources: {message.sources.map(s => s.source).join(', ')}
            </span>
          )}
        </div>
      </div>
    </div>
  );
}

export default ChatMessage;
