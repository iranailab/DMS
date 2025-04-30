import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000', // یا هر پورتی که بک‌اندت روش ران شده
        changeOrigin: true,
        secure: false,
      }
    }
  }
})