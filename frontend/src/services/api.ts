import type { ChatRequest, ChatResponse, ReindexResponse, HealthResponse, StatsResponse } from '../types';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

class ApiService {
  private baseUrl: string;

  constructor(baseUrl: string = API_BASE_URL) {
    this.baseUrl = baseUrl;
  }

  private async request<T>(
    endpoint: string,
    options: RequestInit = {}
  ): Promise<T> {
    const url = `${this.baseUrl}${endpoint}`;
    
    const defaultHeaders: HeadersInit = {
      'Content-Type': 'application/json',
    };

    const config: RequestInit = {
      ...options,
      headers: {
        ...defaultHeaders,
        ...options.headers,
      },
    };

    try {
      const response = await fetch(url, config);
      
      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail || `HTTP error! status: ${response.status}`);
      }

      return await response.json();
    } catch (error) {
      if (error instanceof Error) {
        throw error;
      }
      throw new Error('An unexpected error occurred');
    }
  }

  async sendMessage(message: string): Promise<ChatResponse> {
    const request: ChatRequest = { message };
    return this.request<ChatResponse>('/chat', {
      method: 'POST',
      body: JSON.stringify(request),
    });
  }

  async reindex(): Promise<ReindexResponse> {
    return this.request<ReindexResponse>('/reindex', {
      method: 'POST',
    });
  }

  async getHealth(): Promise<HealthResponse> {
    return this.request<HealthResponse>('/health', {
      method: 'GET',
    });
  }

  async getStats(): Promise<StatsResponse> {
    return this.request<StatsResponse>('/stats', {
      method: 'GET',
    });
  }
}

export const apiService = new ApiService();
export default apiService;
