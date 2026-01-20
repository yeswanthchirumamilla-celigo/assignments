# Quick Setup Guide

## Step 1: Install Dependencies

### Backend
```bash
cd backend
npm install
```

### Frontend
```bash
cd frontend
npm install
```

## Step 2: Configure Environment Variables

Create a `.env` file in the `backend` directory with the following:

```
MONGODB_URI=your_mongodb_atlas_connection_string
JWT_SECRET=your_random_secret_key
PORT=5000
FRONTEND_URL=http://localhost:3000
```

### Getting MongoDB URI:
1. Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Create a free cluster
3. Click "Connect" → "Connect your application"
4. Copy the connection string
5. Replace `<password>` with your database password
6. Replace `<dbname>` with `chat-app` (or any name you prefer)

### Generating JWT Secret:
Run this command to generate a secure random key:
```bash
node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"
```

## Step 3: Run the Application

### Terminal 1 - Backend:
```bash
cd backend
npm start
```

### Terminal 2 - Frontend:
```bash
cd frontend
npm start
```

## Step 4: Access the Application

Open your browser and go to: `http://localhost:3000`

## Features Implemented

✅ Login/Register with email validation (regex)
✅ JWT token authentication (1 hour expiry)
✅ Username displayed at top of chat
✅ Real-time messaging with Socket.io
✅ Messages aligned: your messages on right, others on left
✅ Username on each message ("ME" for your messages)
✅ Cloud MongoDB integration
✅ All preconfigured - just add secrets to .env
