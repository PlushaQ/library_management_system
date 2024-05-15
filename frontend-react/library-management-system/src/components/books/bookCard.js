import React from 'react';
import Card from '@mui/material/Card';
import CardMedia from '@mui/material/CardMedia';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';

const BookCard = ({ book }) => {
  return (
    <Card sx={{ display: 'flex', flexDirection: 'column', height: '100%' }}>
      <Box sx={{ flexGrow: 1 }}>
        <CardMedia
          component="img"
          image={book.cover}
          alt={book.title}
          sx={{ height: 200, objectFit: 'cover' }}
        />
      </Box>
      <CardContent>
        <Typography variant="h6" component="div">
          {book.title}
        </Typography>
        <Typography variant="subtitle1" color="text.secondary" component="div">
          {book.author.name}
        </Typography>
      </CardContent>
    </Card>
  );
};

export default BookCard;