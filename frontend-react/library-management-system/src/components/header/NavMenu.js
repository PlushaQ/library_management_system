import * as React from 'react';
import Box from '@mui/material/Box';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import Menu from '@mui/material/Menu';
import MenuIcon from '@mui/icons-material/Menu';
import Button from '@mui/material/Button';
import MenuItem from '@mui/material/MenuItem';


function NavMenu() {
  const pages = ['First subpage', 'Second Page', 'Third Page'];
  // State for menu anchor elements
  const [anchorElNav, setAnchorElNav] = React.useState(null);


  // Handlers for opening and closing navigation menu
  const handleOpenNavMenu = (event) => {
    setAnchorElNav(event.currentTarget);
    
  };
  const handleCloseNavMenu = () => {
    setAnchorElNav(null);
  };


    return <>
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
    </>
}

export default NavMenu;