import React, { useState, useEffect, useRef } from 'react';
import io from 'socket.io-client';
import api from '../utils/api';
import { getUser, removeToken, removeUser } from '../utils/auth';
import './Chat.css';

const Chat = ({ setIsAuthenticated }) => {
  const [messages, setMessages] = useState([]);
  const [newMessage, setNewMessage] = useState('');
  const [socket, setSocket] = useState(null);
  const [user, setUser] = useState(null);
  const messagesEndRef = useRef(null);
  const token = localStorage.getItem('token');
  const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

  useEffect(() => {
    const currentUser = getUser();
    setUser(currentUser);

    // Initialize socket connection
    const newSocket = io(API_URL, {
      auth: {
        token: token
      }
    });

    newSocket.on('connect', () => {
      console.log('Connected to server');
    });

    newSocket.on('receiveMessage', (message) => {
      setMessages((prev) => [...prev, message]);
    });

    setSocket(newSocket);

    // Fetch previous messages
    const fetchMessages = async () => {
      try {
        const response = await api.get('/chat/messages');
        setMessages(response.data);
      } catch (error) {
        console.error('Error fetching messages:', error);
      }
    };

    fetchMessages();

    return () => {
      newSocket.close();
    };
  }, [token, API_URL]);

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const handleSendMessage = (e) => {
    e.preventDefault();
    if (newMessage.trim() && socket) {
      socket.emit('sendMessage', { text: newMessage.trim() });
      setNewMessage('');
    }
  };

  const handleLogout = () => {
    removeToken();
    removeUser();
    setIsAuthenticated(false);
    if (socket) {
      socket.close();
    }
  };

  const isMyMessage = (message) => {
    if (!user) return false;
    // Convert both to strings for comparison
    const messageUserId = String(message.user);
    const currentUserId = String(user.id);
    return messageUserId === currentUserId;
  };

  return (
    <div className="chat-container">
      <div className="chat-header">
        <h2>Welcome, {user?.username || 'User'}!</h2>
        <button onClick={handleLogout} className="logout-btn">
          Logout
        </button>
      </div>
      <div className="messages-container">
        {messages.map((message) => (
          <div
            key={message._id}
            className={`message ${isMyMessage(message) ? 'my-message' : 'other-message'}`}
          >
            <div className="message-username">
              {isMyMessage(message) ? 'ME' : message.username}
            </div>
            <div className="message-text">{message.text}</div>
            <div className="message-time">
              {new Date(message.timestamp).toLocaleTimeString()}
            </div>
          </div>
        ))}
        <div ref={messagesEndRef} />
      </div>
      <form onSubmit={handleSendMessage} className="message-form">
        <input
          type="text"
          value={newMessage}
          onChange={(e) => setNewMessage(e.target.value)}
          placeholder="Type a message..."
          className="message-input"
        />
        <button type="submit" className="send-btn">
          Send
        </button>
      </form>
    </div>
  );
};

export default Chat;
