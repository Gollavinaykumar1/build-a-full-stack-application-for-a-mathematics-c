import axios from 'axios';

const api = axios.create({
  baseURL: 'https://build-a-full-stack-application-for-a-mathematics-c.onrender.com',
  headers: { 'Content-Type': 'application/json' },
  timeout: 30000,
});

export default api;
