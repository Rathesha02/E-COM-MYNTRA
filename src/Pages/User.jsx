import React, { useState } from 'react';
import axios from 'axios';
import './User.css';

const API_REGISTER = 'http://localhost:5000/api/users';
const API_LOGIN = 'http://localhost:5000/api/users/login';


const User = () => {
  const [isRegister, setIsRegister] = useState(true);
  const [form, setForm] = useState({
    emailid: '',
    password: '',
    username: ''
  });
  const [message, setMessage] = useState('');
  const [userData, setUserData] = useState(null);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage('');
    setUserData(null);

    try {
      const endpoint = isRegister ? API_REGISTER : API_LOGIN;
      const payload = isRegister
        ? form
        : { emailid: form.emailid, password: form.password };

      const res = await axios.post(endpoint, payload, { withCredentials: true });

      setMessage(res.data.message);
      if (res.data.user) {
        setUserData(res.data.user);
      }

      setForm({ emailid: '', password: '', username: '' });
    } catch (err) {
      setMessage(err.response?.data?.message || 'Something went wrong.');
    }
  };

  return (
    <div className="user-page">
      <div className="user-card">
        <h2>{isRegister ? 'Register' : 'Login'}</h2>

        <form onSubmit={handleSubmit}>
          {isRegister && (
            <div>
              <label>Username</label>
              <input
                type="text"
                name="username"
                value={form.username}
                onChange={handleChange}
                required
              />
            </div>
          )}

          <div>
            <label>Email</label>
            <input
              type="email"
              name="emailid"
              value={form.emailid}
              onChange={handleChange}
              required
            />
          </div>

          <div>
            <label>Password</label>
            <input
              type="password"
              name="password"
              value={form.password}
              onChange={handleChange}
              required
            />
          </div>

          <button type="submit">
            {isRegister ? 'Register' : 'Login'}
          </button>
        </form>

        <p>
          {isRegister ? 'Already have an account?' : "Don't have an account?"}{' '}
          <span
            style={{ color: 'blue', cursor: 'pointer' }}
            onClick={() => {
              setIsRegister(!isRegister);
              setMessage('');
              setUserData(null);
            }}
          >
            {isRegister ? 'Login' : 'Register'}
          </span>
        </p>

        {message && <p><b>{message}</b></p>}

        {userData && (
          <div className="user-info">
            <h3>Welcome, User!</h3>
            <p>Email: {userData.emailid}</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default User;
