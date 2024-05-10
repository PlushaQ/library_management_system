import * as React from 'react';
import { styled } from '@mui/material/styles';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Unstable_Grid2';

const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: 'green',
  padding: theme.spacing(1),
  textAlign: 'center',
}));

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
 ]

function Footer() {

    return <>
    <Grid container spacing={2}>
        { navbarItems.map((navPart) => (
            <Grid item xs={11} sm={4} key={navPart.title}>
                <Item>{navPart.title}</Item>
                <ul>
                    {navPart.description.map((desc) => (
                        <li key={desc}>
                            {desc}
                        </li>
                    ))}
                </ul>
            </Grid>
        ))}
    </Grid>
    </>
}

export default Footer;