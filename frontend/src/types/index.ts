export interface Message {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  timestamp: Date;
  sources?: Source[];
  tokens?: TokenUsage;
}

export interface Source {
  source: string;
  page?: number;
  score: number;
}

export interface TokenUsage {
  prompt: number;
  completion: number;
  total: number;
}

export interface ChatRequest {
  message: string;
}

export interface ChatResponse {
  response: string;
  sources: Source[];
  tokens: TokenUsage;
}

export interface ReindexResponse {
  status: string;
  message: string;
}

export interface HealthResponse {
  status: string;
  vector_db: string;
  documents_indexed: number;
  total_chunks: number;
}

export interface StatsResponse {
  total_documents: number;
  total_chunks: number;
  vector_db_size: string;
  last_indexed: string;
}
