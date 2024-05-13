import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Container from '@mui/material/Container';
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
