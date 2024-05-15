import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

import { Route, BrowserRouter as Router, Routes } from 'react-router-dom';
import reportWebVitals from './reportWebVitals';
import { ThemeProvider, createTheme } from '@mui/material';

import Header from './components/header/Header'
import Footer from './components/Footer';
import Homepage from './components/homepage/homepage';
import BookList from './components/books/bookList';
import Login from './components/auth/Login'
import Register from './components/auth/Register'
import Logout from './components/auth/Logout';

const theme = createTheme()

const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
  <Router>
    <React.StrictMode>
      <ThemeProvider theme={theme}>
        <Header />
        <Routes>
          <Route exact path="/" element={<Homepage />} />
          <Route path="/books" element={<BookList />} />
          {/* Auth routes */}
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/logout" element={<Logout />} />
        </Routes>
        <Footer />
      </ThemeProvider>
    </React.StrictMode>
  </Router>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
