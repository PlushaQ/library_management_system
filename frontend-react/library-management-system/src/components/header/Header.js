import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import Menu from '@mui/material/Menu';
import MenuIcon from '@mui/icons-material/Menu';
import Container from '@mui/material/Container';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import Tooltip from '@mui/material/Tooltip';
import MenuItem from '@mui/material/MenuItem';
import { styled } from '@mui/system';
import { Hidden } from '@mui/material';

const pages = ['First subpage', 'Second Page', 'Third Page'];
const settings = ['Profile', 'Account', 'Dashboard', 'Logout'];


function Header() {
  // State for menu anchor elements
  const [anchorElNav, setAnchorElNav] = React.useState(null);
  const [anchorElUser, setAnchorElUser] = React.useState(null);

  // Handlers for opening and closing navigation menu
  const handleOpenNavMenu = (event) => {
    setAnchorElNav(event.currentTarget);
    
  };
  const handleCloseNavMenu = () => {
    setAnchorElNav(null);
  };

  // Handlers for opening and closing user menu
  const handleOpenUserMenu = (event) => {
    setAnchorElUser(event.currentTarget);
  };

  const handleCloseUserMenu = () => {
    setAnchorElUser(null);
  };

  // Styling the AppBar
  const StyledAppBar = styled(AppBar)({
    backgroundColor: '#522E46',
  });

  return (
    <StyledAppBar position="static">
      <Container maxWidth="xl">
        <Toolbar disableGutters>
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

          {/* Navigation menu icon */}
          <Box sx={{ flexGrow: 1, display: { xs: 'flex', md: 'none' } }}>
            <IconButton
              size="large"
              aria-label="account of current user"
              aria-controls="menu-appbar"
              aria-haspopup="true"
              onClick={handleOpenNavMenu}
              color="inherit"
            >
              <MenuIcon />
            </IconButton>
            {/* Navigation menu */}
            <Menu
              id="menu-appbar"
              anchorEl={anchorElNav}
              anchorOrigin={{
                vertical: 'bottom',
                horizontal: 'left',
              }}
              keepMounted
              transformOrigin={{
                vertical: 'top',
                horizontal: 'left',
              }}
              open={Boolean(anchorElNav)}
              onClose={handleCloseNavMenu}
              sx={{
                display: { xs: 'block', md: 'none' },
              }}
            >
              {/* Navigation menu items */}
              {pages.map((page) => (
                <MenuItem
                  key={page}
                  href="/"
                  component="a"
                  onClick={handleCloseNavMenu}
                >
                  <Typography textAlign="center">{page}</Typography>
                </MenuItem>
              ))}
            </Menu>
          </Box>

          {/* Logo text for smaller screens */}
          <Typography
            variant="h5"
            noWrap
            component="a"
            href="#app-bar-with-responsive-menu"
            sx={{
              mr: 2,
              display: { xs: 'flex', md: 'none' },
              flexGrow: 1,
              fontFamily: 'monospace',
              fontWeight: 700,
              letterSpacing: '.3rem',
              color: 'inherit',
              textDecoration: 'none',
            }}
          >
            LibraSage
          </Typography>

          {/* Desktop nav menu */}
          <Box sx={{ flexGrow: 1, display: { xs: 'none', md: 'flex' } }}>
            {/* Desktop navigation menu items */}
            {pages.map((page) => (
              <Button
                key={page}
                href="test"
                component="a"
                onClick={handleCloseNavMenu}
                sx={{ my: 2, color: 'white', display: 'block' }}
              >
                {page}
              </Button>
            ))}
          </Box>

          {/* User settings menu */}
          <Box sx={{ flexGrow: 0 }}>
            {/* Avatar button */}
            <Tooltip title="Open settings">
              <IconButton onClick={handleOpenUserMenu}>
                <Avatar alt="User avatar" src="/logo192.png" />
              </IconButton>
            </Tooltip>
            {/* User settings menu */}
            <Menu
              sx={{ mt: '0', }}
              id="menu-user-appbar"
              anchorEl={anchorElUser}
              anchorOrigin={{
                vertical: 'top',
                horizontal: 'right',
              }}
              keepMounted
              transformOrigin={{
                vertical: 'top',
                horizontal: 'right',
              }}
              open={Boolean(anchorElUser)}
              onClose={handleCloseUserMenu}
            >
              
              {/* User settings menu items */}
              {settings.map((setting) => (
                <MenuItem
                  key={setting}
                  href="#"
                  component="a"
                  onClick={handleCloseUserMenu}
                >
                  <Typography textAlign="center">{setting}</Typography>
                </MenuItem>
              ))}
            </Menu>
          </Box>
        </Toolbar>
      </Container>
    </StyledAppBar>
  );
}
export default Header;
