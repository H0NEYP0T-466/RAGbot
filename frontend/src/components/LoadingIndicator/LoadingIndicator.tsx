import './LoadingIndicator.css';

function LoadingIndicator() {
  return (
    <div className="loading-indicator">
      <div className="loading-dots">
        <span className="dot"></span>
        <span className="dot"></span>
        <span className="dot"></span>
      </div>
    </div>
  );
}

export default LoadingIndicator;
