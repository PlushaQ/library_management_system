import * as React from 'react';
import Container from '@mui/material/Container';
import { styled } from '@mui/system';
import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';


const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: '#894658',
  padding: theme.spacing(1),
  textAlign: 'center',
  color: 'white',
}));

const LiItem = styled('li')({
    color: 'white',
})

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

}))

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
                    <LiItem key={desc}>{desc}</LiItem>
                  ))}
                </ul>
              </Grid>
            ))}
          </Grid>
      </StyledContainer>
      </>
  );
}

export default Footer;
