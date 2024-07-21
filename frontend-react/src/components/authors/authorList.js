import React, { useEffect, useState } from 'react';
import Box from '@mui/material/Box';
import { List, ListItem } from '@mui/material';
import axiosInstance from '../../axios';
import AuthorCard from './authorCard';
import Paginator from '../pagination/Paginator';

const AuthorList = () => {
  const [data, setData] = useState({ authors: [] });
  const [pageData, setPageData] = useState({ next: null, previous: null, total_pages: 1, current_page: 1 });

  useEffect(() => {
    fetchData(pageData.current_page);
  }, [pageData.current_page]);

  const fetchData = (page) => {
    axiosInstance.get(`/authors?page=${page}`).then((res) => {
      setData({ authors: res.data.results });
      console.log(res)
      setPageData({
        next: res.data.next,
        previous: res.data.previous,
        total_pages: Math.ceil(res.data.count / res.data.page_size),
        current_page: page
      });
    });
  };

  const handlePageChange = (page) => {
    window.scrollTo({top: 0, behavior: 'smooth'});
    setPageData((prev) => ({ ...prev, current_page: page }));
  };

  return (
    <Box sx={{ flexGrow: 1, padding: 2, textAlign: 'center' }}>
      <List>
        {data.authors.map((author, index) => (
          <ListItem key={index} sx={{ padding: 0, mb: 2 }}>
            <AuthorCard author={author} />
          </ListItem>
        ))}
        <Paginator
          currentPage={pageData.current_page}
          totalPages={pageData.total_pages}
          onPageChange={handlePageChange}
        />
      </List>
    </Box>
  );
};

export default AuthorList;
