import React, { useEffect, useState } from 'react';
import { Card, CardContent, CardMedia, Typography, Box, Grid } from '@mui/material';
import axiosInstance from '../../axios';
import { Link, useParams } from 'react-router-dom';
import LoadingComponent from '../Loading';
import ErrorPage from '../../utils/ErrorPage';

const BookDetail = () => {
    const { id } = useParams();
    const [bookData, setBookData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        axiosInstance.get(`/books/${id}`)
            .then((res) => {
                setBookData(res.data);
                setLoading(false);
            })
            .catch((err) => {
                setError(err.response);
                setLoading(false);
            });
    }, [id]);

    if (loading) {
        return <LoadingComponent />;
    }

    if (error) {
        return <ErrorPage error={error} />;
    }

    return (
        <Card sx={{ maxWidth: 800, margin: '20px auto', boxShadow: 3 }}>
            <Grid container spacing={2}>
                <Grid item xs={12} sm={4} md={3}>
                    <CardMedia
                        component="img"
                        sx={{ width: '100%' }}
                        src={bookData.cover}
                        alt="Book Cover"
                    />
                    <Box sx={{ textAlign: 'center', mt: 2 }}>
                        <Box sx={{ backgroundColor: '#f8f8f8', padding: 2, border: 1, borderColor: '#ddd', mb: 1 }}>
                            <Typography variant="body2" color="text.secondary">
                                Average rating
                            </Typography>
                            <Typography variant="h4" color="error">
                                7.7 / 10
                            </Typography>
                        </Box>
                        <Box>
                            <Typography variant="body2" color="text.secondary">
                                Number of opinions: TO DO
                            </Typography>
                            <Typography variant="body2" color="text.secondary">
                                Number of reviews: TO DO
                            </Typography>
                        </Box>
                    </Box>
                </Grid>
                <Grid item xs={12} sm={8} md={9}>
                    <CardContent>
                        <Typography component="h1" variant="h5">
                            {bookData.title}
                        </Typography>
                        <Typography component="h2" variant="subtitle1" color="text.secondary">
                            <Link
                                to={`/authors/${bookData.author.id}`}
                                style={{ color: 'inherit', textDecoration: 'none' }}
                            >
                                {bookData.author.name}
                            </Link>
                        </Typography>
                        <Box sx={{ mt: 2 }}>
                            <Typography variant="body2" color="text.secondary">
                                <strong>Edition:</strong> {bookData.edition}
                            </Typography>
                            <Typography variant="body2" color="text.secondary">
                                <strong>Series:</strong> {bookData.series.name}
                            </Typography>
                            <Typography variant="body2" color="text.secondary">
                                <strong>Categories:</strong> {bookData.category.map(cat => cat.name).join(', ')}
                            </Typography>
                            <Typography variant="body2" color="text.secondary">
                                <strong>ISBN:</strong> {bookData.isbn}
                            </Typography>
                            <Typography variant="body2" color="text.secondary">
                                <strong>Published Date:</strong> {bookData.publication_date}
                            </Typography>
                        </Box>
                    </CardContent>
                </Grid>
            </Grid>
        </Card>
    );
};

export default BookDetail;
