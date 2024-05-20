import React, { useEffect, useState } from 'react';
import { Card, CardContent, CardMedia, Typography, Box } from '@mui/material';
import axiosInstance from '../../axios';
import { useParams } from 'react-router-dom';
import LoadingComponent from '../Loading';

const BookDetail = () => {
    const { id } = useParams()
    const [bookData, setBookData] = useState(null)
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);


    useEffect(() => { 
        axiosInstance.get(`/books/${id}`)
        .then((res) => {
            setBookData(res.data);
            console.log(res.data)
            setLoading(false);
        })
        .catch((err) => {
            setError(err);
            setLoading(false);
        });
    }, [id]);

    if (loading) {
        return <LoadingComponent />;
    }

  return (
    <>
    <Card sx={{ display: 'flex', maxWidth: 800, margin: '20px auto', boxShadow: 3 }}>
      <CardMedia
        component="img"
        sx={{ width: 151 }}
        src={bookData.cover}
        alt="Book Cover"
      />
      <Box sx={{ display: 'flex', flexDirection: 'column', flex: 1 }}>
        <CardContent>
          <Typography component="h1" variant="h5">
          {bookData.title}
          </Typography>
          <Typography component="h2" variant="subtitle1" color="text.secondary">
          {bookData.author.name}
          </Typography>
          <Typography variant="body2" color="text.secondary">
            <strong>Edition:</strong> {bookData.edition}
          </Typography>
          <Typography variant="body2" color="text.secondary">
            <strong>Series:</strong> {bookData.series.name}
          </Typography>
          <Typography variant="body2" color="text.secondary">
            <strong>Categories: </strong> {bookData.category.map(cat => cat.name).join(', ')}
          </Typography>
          <Typography variant="body2" color="text.secondary">
                <strong>ISBN:</strong> {bookData.isbn}
          </Typography>
          <Typography variant="body2" color="text.secondary">
                <strong>Published Date:</strong> {bookData.publication_date}
          </Typography>
        </CardContent>
      </Box>
      <Box sx={{ textAlign: 'center', margin: 'auto 20px' }}>
        <Box sx={{ backgroundColor: '#f8f8f8', padding: 2, border: 1, borderColor: '#ddd', mb: 1 }}>
          <Typography variant="body2" color="text.secondary">
            Average rating
          </Typography>
          <Typography variant="h4" color="error">
            7,7 / 10
          </Typography>
        </Box>
        <Box>
          <Typography variant="body2" color="text.secondary">
            TO DO - Number of opinions
          </Typography>
          <Typography variant="body2" color="text.secondary">
            TO DO - Number of ratings
          </Typography>
        </Box>
      </Box>
    </Card>
</> 
  );
};

export default BookDetail;
