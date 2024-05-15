import { Box, Container, Typography } from '@mui/material';
import react from 'react'


function Homepage() {
    return <>
    <Container maxWidth='xl'>
        <Box>
            <Typography variant='h1'>
                {'Welcome to LibraSage'}
            </Typography>
        </Box>
    </Container>
    </>
}

export default Homepage;