import * as React from 'react';
import Box from '@mui/material/Box'
import Tooltip from '@mui/material/Tooltip';
import Avatar from '@mui/material/Avatar';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';

function UserMenu() {
    const settings = ['Profile', 'Account', 'Dashboard', 'Logout'];

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
</>
}

export default UserMenu;