import { AppBar, Toolbar, Typography, Button } from '@mui/material';
import FavoriteIcon from '@mui/icons-material/Favorite';

export default function Navbar() {
  return (
    <AppBar position="static" color="secondary">
      <Toolbar>
        <FavoriteIcon sx={{ mr: 2 }} />
        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
          Dating Decision Advisor
        </Typography>
        <Button color="inherit" href="/about">About</Button>
      </Toolbar>
    </AppBar>
  );
}