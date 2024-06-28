import React, { useEffect, useState } from 'react';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import BookCard from './bookCard';

import axiosInstance from '../../axios';
import { List, ListItem } from '@mui/material';

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
      <List>
        {data.books.map((book, index) => (
          <ListItem key={index} sx={{ padding: 0, mb: 2 }}>
            <BookCard book={book} />
          </ListItem>
        ))}
      </List>
    </Box>
  );
};

export default BookList;