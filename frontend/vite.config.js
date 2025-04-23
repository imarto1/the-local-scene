import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import fs from 'fs'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    host: "0.0.0.0",
    port: 3000,
    open: true,
    cors: true,
    https: {
      key: fs.readFileSync('cert/localhost-key.pem'),
      cert: fs.readFileSync('cert/localhost-cert.pem'),
    },
  },
})
