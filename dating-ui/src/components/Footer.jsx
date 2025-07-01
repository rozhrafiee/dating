import { Box, Typography } from '@mui/material';

export default function Footer() {
  return (
    <Box sx={{ bgcolor: 'background.paper', p: 2, mt: 4 }}>
      <Typography variant="body2" color="text.secondary" align="center">
        For entertainment purposes only! ❤️
      </Typography>
    </Box>
  );
}