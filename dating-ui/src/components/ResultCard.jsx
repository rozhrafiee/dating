import { Card, CardContent, Typography } from '@mui/material';
import FavoriteIcon from '@mui/icons-material/Favorite';
import HeartBrokenIcon from '@mui/icons-material/HeartBroken';
import HelpIcon from '@mui/icons-material/Help';

export default function ResultCard({ decision }) {
  const getIcon = () => {
    if (decision.includes('Keep')) return <FavoriteIcon color="success" sx={{ fontSize: 60 }} />;
    if (decision.includes('Dump')) return <HeartBrokenIcon color="error" sx={{ fontSize: 60 }} />;
    return <HelpIcon color="warning" sx={{ fontSize: 60 }} />;
  };

  return (
    <Card sx={{ minWidth: 275, mt: 4, textAlign: 'center' }}>
      <CardContent>
        {getIcon()}
        <Typography variant="h4" component="div">
          {decision}
        </Typography>
      </CardContent>
    </Card>
  );
}