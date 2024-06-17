import React, { useState } from 'react';
import axiosInstance from '../../axios';
import { useNavigate } from 'react-router-dom';
//MaterialUI
import { Alert, Avatar } from '@mui/material';
import { Button } from '@mui/material';
import { CssBaseline } from '@mui/material';
import { TextField } from '@mui/material';
import { FormControlLabel } from '@mui/material';
import { Checkbox } from '@mui/material';
import { Link } from '@mui/material';
import { Grid } from '@mui/material';
import { Typography } from '@mui/material';
import styled from '@emotion/styled';
import { Container } from '@mui/material';



const StyledPaper = styled('div')(({theme}) => ({
    marginTop: theme.spacing(8),
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center'
}));

const StyledAvatar = styled(Avatar)(({theme}) => ({
    margin: theme.spacing(1),
    backgroundColor: theme.palette.secondary.main,
}));

const StyledForm = styled('form')(({theme}) => ({
        width: '100%',
        marginTop: theme.spacing(3),
}));

const StyledButton = styled(Button)(({theme}) => ({
            margin: theme.spacing(3, 0, 2),
}));



export default function SignUp() {
	const navigate = useNavigate();
	const initialFormData = Object.freeze({
		email: '',
		username: '',
		password: '',
	});

	const [formData, updateFormData] = useState(initialFormData);
	const [errorMessages, setErrorMessages] = useState({});

	const handleChange = (e) => {
		updateFormData({
			...formData,
			// Trimming any whitespace
			[e.target.name]: e.target.value.trim(),
		});
	};

	const handleSubmit = (e) => {
		e.preventDefault();
		console.log(formData);

		axiosInstance
			.post(`user/register/`, {
				email: formData.email,
				user_name: formData.username,
				password: formData.password,
			})
			.then((res) => {
				navigate('/login');
				console.log(res.data);
			}).catch((err) => {
				if (err.response && err.response.data) {
					setErrorMessages(err.response.data);
				} else {
					setErrorMessages({ general: ['An unexpected error occurred'] });
				}
			});
	};


	return (
		<Container component="main" maxWidth="xs" style={{marginBottom: '60px'}}>
			<CssBaseline />
			<StyledPaper>
				<StyledAvatar></StyledAvatar>
				<Typography component="h1" variant="h5">
					Sign up
				</Typography>
				{Object.keys(errorMessages).length > 0 && (
					<Grid container spacing={2}>
						{Object.entries(errorMessages).map(([key, messages]) => (
							<Grid item xs={12} key={key}>
								{messages.map((message, index) => (
									<Alert severity="error" key={index}>
										{message}
									</Alert>
								))}
							</Grid>
						))}
					</Grid>
				)}
				<StyledForm noValidate>
					<Grid container spacing={2}>
						<Grid item xs={12}>
							<TextField
								variant="outlined"
								required
								fullWidth
								id="email"
								label="Email Address"
								name="email"
								autoComplete="email"
								onChange={handleChange}
							/>
						</Grid>
						<Grid item xs={12}>
							<TextField
								variant="outlined"
								required
								fullWidth
								id="username"
								label="Username"
								name="username"
								autoComplete="username"
								onChange={handleChange}
							/>
						</Grid>
						<Grid item xs={12}>
							<TextField
								variant="outlined"
								required
								fullWidth
								name="password"
								label="Password"
								type="password"
								id="password"
								autoComplete="current-password"
								onChange={handleChange}
							/>
						</Grid>
						<Grid item xs={12}>
							<FormControlLabel
								control={<Checkbox value="allowExtraEmails" color="primary" />}
								label="I want to receive inspiration, marketing promotions and updates via email."
							/>
						</Grid>
					</Grid>
                        <StyledButton
                            type="submit"
                            fullWidth
                            variant="contained"
                            color="primary"
                            onClick={handleSubmit}
                        >
                            Sign Up
                        </StyledButton>
					<Grid container justify="flex-end">
						<Grid item>
							<Link href="/login" variant="body2">
								Already have an account? Sign in
							</Link>
						</Grid>
					</Grid>
				</StyledForm>
			</StyledPaper>
		</Container>
	);
}
