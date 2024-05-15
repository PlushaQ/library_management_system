import { Box, Container, Typography } from '@mui/material';
import react from 'react'


function Homepage() {
    return <>
    <Container maxWidth='xl' style={{marginTop: '10vh', marginBottom: '50vh'}}>
        <Box>
            <Typography variant='h1' textAlign={'center'}>
                {'Welcome to LibraSage'}
            </Typography>
        </Box>
    </Container>
    </>
}

export default Homepage;