import * as React from 'react';
import Box from '@mui/material/Box'
import Tooltip from '@mui/material/Tooltip';
import Avatar from '@mui/material/Avatar';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';

import { isLoggedIn } from '../../utils/auth';


function UserMenu() {
    const userLoggedIn = isLoggedIn()

    const loggedInSettings = [
        { name: 'Profile', url: '/profile' },
        { name: 'Account', url: '/account' },
        { name: 'Dashboard', url: '/dashboard' },
        { name: 'Logout', url: '/logout' }
    ];
    
    const logoutSettings = [
        { name: 'Login', url: '/login' },
        { name: 'Register', url: '/register' }
    ];

    const settings = userLoggedIn ? loggedInSettings : logoutSettings

    const [anchorElUser, setAnchorElUser] = React.useState(null);

    // Handlers for opening and closing user menu
    const handleOpenUserMenu = (event) => {
        setAnchorElUser(event.currentTarget);
    };

    const handleCloseUserMenu = () => {
        setAnchorElUser(null);
    };

    return <>
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
            sx={{ mt: '45px', }}
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
            key={setting.name}
            href={setting.url}
            component="a"
            onClick={handleCloseUserMenu}
            >
                <Typography textAlign="center">{setting.name}</Typography>
            </MenuItem>
        ))}
        </Menu>
    </Box>
</>
}

export default UserMenu;