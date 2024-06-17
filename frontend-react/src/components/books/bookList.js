import React, { useEffect, useState } from 'react';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import BookCard from './bookCard';

import axiosInstance from '../../axios';

const BookList = () => {
  const [data, setData] = useState({books: []})

  useEffect(() => {
    axiosInstance.get('/books').then((res) => {
      setData({books: res.data});
      console.log(res.data);
    });
  }, [setData]);

  return (
    <Box sx={{ flexGrow: 1, padding: 2 }}>
      <Grid container spacing={2}>
        {data.books.map((book, index) => (
          <Grid item xs={12} sm={6} md={4} lg={3} key={index}>
            <BookCard book={book} />
          </Grid>
        ))}
      </Grid>
    </Box>
  );
};

export default BookList;