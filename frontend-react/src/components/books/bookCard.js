import React from 'react';
import Card from '@mui/material/Card';
import CardMedia from '@mui/material/CardMedia';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import { Link } from '@mui/material';

const BookCard = ({ book }) => {
  return (
    <Box sx={{ width: '80%', margin: '0 auto' }}>
      <Card sx={{ display: 'flex', flexDirection: 'row', height: '100%', width: '100%' }}>
        <CardMedia
          component="img"
          image={book.cover}
          alt={book.title}
          sx={{ width: 200, objectFit: 'cover' }}
        />
        <Box sx={{ display: 'flex', flexDirection: 'column', flexGrow: 1, padding: 2 }}>
          <CardContent sx={{ flex: '1 0 auto' }}>
            <Typography variant="h4" component="div">
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
        </Box>
        <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'center', padding: 2 }}>
          <Card sx={{ width: 100, height: 100, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            <Typography variant="body1">
              Rating: {book.rating}
            </Typography>
          </Card>
        </Box>
      </Card>
    </Box>
  );
};

export default BookCard;
