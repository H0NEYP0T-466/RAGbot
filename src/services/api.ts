import type { ChatResponse, HealthResponse, ReindexResponse, StatsResponse } from '../types';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

class ApiService {
  private baseUrl: string;
  private retryAttempts: number;
  private retryDelay: number;

  constructor(baseUrl: string = API_BASE_URL) {
    this.baseUrl = baseUrl;
    this.retryAttempts = 3;
    this.retryDelay = 1000;
  }

  private async fetchWithRetry<T>(
    url: string,
    options: RequestInit,
    attempts: number = this.retryAttempts
  ): Promise<T> {
    for (let i = 0; i < attempts; i++) {
      try {
        const response = await fetch(url, options);
        if (!response.ok) {
          const errorData = await response.json().catch(() => ({}));
          throw new Error(errorData.detail || `HTTP error! status: ${response.status}`);
        }
        return await response.json();
      } catch (error) {
        if (i === attempts - 1) {
          throw error;
        }
        // Exponential backoff: 1s, 2s, 4s
        await new Promise(resolve => setTimeout(resolve, this.retryDelay * Math.pow(2, i)));
      }
    }
    throw new Error('Failed after all retry attempts');
  }

  async sendMessage(message: string): Promise<ChatResponse> {
    if (!message.trim()) {
      throw new Error('Message cannot be empty');
    }

    return this.fetchWithRetry<ChatResponse>(`${this.baseUrl}/chat`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message }),
    });
  }

  async reindex(): Promise<ReindexResponse> {
    return this.fetchWithRetry<ReindexResponse>(`${this.baseUrl}/reindex`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
    });
  }

  async getHealth(): Promise<HealthResponse> {
    return this.fetchWithRetry<HealthResponse>(`${this.baseUrl}/health`, {
      method: 'GET',
    });
  }

  async getStats(): Promise<StatsResponse> {
    return this.fetchWithRetry<StatsResponse>(`${this.baseUrl}/stats`, {
      method: 'GET',
    });
  }
}

export const apiService = new ApiService();
export default apiService;
