import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import Menu from '@mui/material/Menu';
import MenuIcon from '@mui/icons-material/Menu';
import Container from '@mui/material/Container';
import Button from '@mui/material/Button';
import MenuItem from '@mui/material/MenuItem';
import { styled } from '@mui/system';

import UserMenu from './UserMenu';
import Logo from './Logo';
import NavMenu from './NavMenu';




function Header() {
  // Styling the AppBar
  const StyledAppBar = styled(AppBar)({
    backgroundColor: '#522E46',
  });

  return (
    <StyledAppBar position="static">
      <Container maxWidth="xl">
        <Toolbar disableGutters>
          <Logo />
          <NavMenu />
          <UserMenu />
        </Toolbar>
      </Container>
    </StyledAppBar>
  );
}
export default Header;
