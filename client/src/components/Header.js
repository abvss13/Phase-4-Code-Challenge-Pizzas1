import React from 'react';
import { AppBar } from '@mui/material';
import PizzaImage from './pizza image.jpg'; // Replace with the actual path to your pizza image

function Header() {
  return (
    <AppBar
      position="static"
      sx={{
        backgroundColor: "skyblue",
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '20px',
        flexDirection: 'row', // Align items in a row
      }}
    >
      <h1 style={{ margin: 0, color: 'white', marginRight: '20px' }}>The Pizza Joint</h1>
      <img src={PizzaImage} alt="Pizza" style={{ width: '80px', height: '80px', objectFit: 'cover' }} />
    </AppBar>
  );
}

export default Header;


