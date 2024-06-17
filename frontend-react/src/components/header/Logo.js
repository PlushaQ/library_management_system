import * as React from 'react';
import Typography from '@mui/material/Typography';
import { Hidden } from '@mui/material';

function Logo() {
    return <>
    {/* Logo */}
    <Hidden mdDown> {/* Hide on screens smaller than medium */}
      <img src="/logo500x500.png" alt="logo" style={{ height: 50 }} />
    </Hidden>

    {/* Logo text */}
    <Typography
      variant="h6"
      noWrap
      component="a"
      href="/"
      sx={{
        mr: 2,
        display: { xs: 'none', md: 'flex' },
        fontFamily: 'monospace',
        fontWeight: 700,
        letterSpacing: '.3rem',
        color: 'inherit',
        textDecoration: 'none',
      }}
    >
      LibraSage
    </Typography>
    
    </>
}

export default Logo;