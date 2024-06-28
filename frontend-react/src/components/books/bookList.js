import React, { useEffect, useState } from 'react';
import Box from '@mui/material/Box';
import { List, ListItem } from '@mui/material';

import axiosInstance from '../../axios';
import BookCard from './bookCard';
import Paginator from '../pagination/Paginator';

const BookList = () => {
  const [data, setData] = useState({books: []})

  useEffect(() => {
    axiosInstance.get('/books').then((res) => {
      setData({books: res.data});
      console.log(res.data);
    });
  }, [setData]);

  return (<>
    <Box sx={{ flexGrow: 1, padding: 2, textAlign: 'center' }}>
      <List>
        {data.books.map((book, index) => (
          <ListItem key={index} sx={{ padding: 0, mb: 2 }}>
            <BookCard book={book} />
          </ListItem>
        ))}
      </List>
      <Box mt={2}>
          <Paginator/>
        </Box>
    </Box>
    </>
  );
};

export default BookList;