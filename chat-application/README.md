# Chat Application

A real-time chat application built with MERN stack (MongoDB, Express, React, Node.js) with Socket.io for real-time messaging.

## Features

- User authentication (Login/Register)
- Email validation using regex
- JWT token-based authentication (expires in 1 hour)
- Real-time messaging using Socket.io
- Common chat room for all users
- Message alignment: your messages on the right, others on the left
- Username display on messages (shows "ME" for your messages)
- Username displayed at the top of the chat

## Setup Instructions

### Prerequisites

- Node.js (v14 or higher)
- MongoDB Atlas account (or local MongoDB)
- npm or yarn

### Installation

1. **Clone or navigate to the project directory**

2. **Backend Setup**
   ```bash
   cd backend
   npm install
   ```

3. **Frontend Setup**
   ```bash
   cd ../frontend
   npm install
   ```

4. **Environment Configuration**

   - Copy `.env.example` to `.env` in the backend directory:
     ```bash
     cd backend
     cp .env.example .env
     ```

   - Edit the `.env` file and add your secrets:
     ```
     MONGODB_URI=your_mongodb_atlas_connection_string
     JWT_SECRET=your_random_secret_key_here
     PORT=5000
     FRONTEND_URL=http://localhost:3000
     ```

   - For MongoDB Atlas:
     - Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
     - Create a free cluster
     - Get your connection string
     - Replace `<password>` with your database password
     - Replace `<dbname>` with your database name (e.g., `chat-app`)

   - For JWT_SECRET, use a strong random string (you can generate one using Node.js):
     ```bash
     node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"
     ```

### Running the Application

1. **Start the Backend Server**
   ```bash
   cd backend
   npm start
   # or for development with auto-reload:
   npm run dev
   ```
   The backend will run on `http://localhost:5000`

2. **Start the Frontend**
   ```bash
   cd frontend
   npm start
   ```
   The frontend will run on `http://localhost:3000`

3. **Open your browser**
   Navigate to `http://localhost:3000`

## Usage

1. **Register/Login**: Create an account or login with existing credentials
2. **Chat**: Once logged in, you'll see the chat interface with your username at the top
3. **Send Messages**: Type messages in the input field and press Send
4. **View Messages**: 
   - Your messages appear on the right side with "ME" as the username
   - Other users' messages appear on the left side with their usernames

## Project Structure

```
chat-application/
├── backend/
│   ├── models/
│   │   ├── User.js
│   │   └── Message.js
│   ├── routes/
│   │   ├── auth.js
│   │   └── chat.js
│   ├── middleware/
│   │   └── auth.js
│   ├── server.js
│   ├── package.json
│   └── .env (create this from .env.example)
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── Login.js
│   │   │   ├── Login.css
│   │   │   ├── Chat.js
│   │   │   └── Chat.css
│   │   ├── utils/
│   │   │   ├── auth.js
│   │   │   └── api.js
│   │   ├── App.js
│   │   ├── index.js
│   │   └── index.css
│   └── package.json
├── .env.example
└── README.md
```

## Technologies Used

- **Backend**: Node.js, Express.js, MongoDB (Mongoose), Socket.io, JWT, bcryptjs
- **Frontend**: React, React Router, Socket.io-client, Axios
- **Authentication**: JWT tokens (1 hour expiry)
- **Real-time**: Socket.io for bidirectional communication

## Notes

- Tokens expire after 1 hour - users will need to login again
- Email validation uses regex pattern: `/^[^\s@]+@[^\s@]+\.[^\s@]+$/`
- All messages are stored in MongoDB
- The application uses cloud MongoDB (MongoDB Atlas) by default
