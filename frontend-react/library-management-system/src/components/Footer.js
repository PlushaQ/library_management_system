import * as React from 'react';
import Container from '@mui/material/Container';
import { styled } from '@mui/system';
import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import Link from '@mui/material/Link';
import Typography from '@mui/material/Typography'


const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: '#894658',
  padding: theme.spacing(1),
  textAlign: 'center',
  color: 'white',
}));

const LiItem = styled('li')({
    color: 'white',
})

const StyledLink = styled(Link)(({theme}) => ({
  textDecoration: 'none',
  color: 'inherit',
}))

const navbarItems = [
  {
    title: 'First',
    description: ['a', 'b', 'c', 'd'],
  },
  {
    title: 'Second',
    description: ['a', 'b', 'c', 'd'],
  },
  {
    title: 'Third',
    description: ['a', 'b', 'c', 'd'],
  },
  {title: 'Fourth',
    description: [1, 2, 3]}
];


const StyledContainer = styled(Container)(({ theme }) => ({
    padding: theme.spacing(4),
    backgroundColor: '#522E46',
    marginTop: 'auto',

}))

function Copyright() {
  return (
    <Typography variant="body2" color="white" align="center">
      {'Copyright © '}
      <Link color="inherit" href="/">
        LibraSage
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

function Footer() {
  return (
    <>
      <StyledContainer maxWidth="false">
          <Grid container spacing={2}>
            {navbarItems.map((navPart) => (
              <Grid item xs={12} sm={3} key={navPart.title}>
                <Item elevation={0}>{navPart.title}</Item>
                <ul>
                  {navPart.description.map((desc) => (
                    <LiItem key={desc}>
                      <StyledLink href='#'>{desc}</StyledLink>
                    </LiItem>
                  ))}
                </ul>
              </Grid>
            ))}
          </Grid>
          <br></br>
          <Copyright/>
      
      </StyledContainer>
      </>
  );
}

export default Footer;
