import React from 'react';
import Card from '@mui/material/Card';
import CardMedia from '@mui/material/CardMedia';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import { Link } from '@mui/material';

const BookCard = ({ book }) => {
  return (
    <Box sx={{ width: '80%', margin: '0 auto' }}>
      <Card sx={{ display: 'flex', flexDirection: 'column', height: '100%', width: '100%' }}>
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
            <Link
              href={`/book-detail/${book.id}`}
              color='inherit'
              underline='hover'
            >
              {book.title}
            </Link>
          </Typography>
          <Typography variant="subtitle1" color="text.secondary" component="div">
            <Link
              href={`/authors/${book.author.id}`}
              color='inherit'
              underline='hover'
            >
              {book.author.name}
            </Link>
          </Typography>
        </CardContent>
      </Card>
    </Box>
  );
};

export default BookCard;
