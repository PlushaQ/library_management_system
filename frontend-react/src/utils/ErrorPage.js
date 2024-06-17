import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Button, Typography, Container } from '@mui/material';

const ErrorPage = ({ error }) => {
  const navigate = useNavigate();

  const handleBackToHome = () => {
    navigate('/');
  };

  return (
    <Container sx={{ display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
      <Typography variant="h1" color="error" gutterBottom>
        {error.status}
      </Typography>
      <Typography variant="h5" color="text.secondary" gutterBottom>
        {error.data.detail}
      </Typography>
      <Button variant="contained" color="primary" onClick={handleBackToHome}>
        Back to Home
      </Button>
    </Container>
  );
};

export default ErrorPage;
