import { Container, Typography, Link } from '@mui/material';

export default function About() {
  return (
    <Container maxWidth="md">
      <Typography variant="h4" gutterBottom>
        About Dating Decision Advisor
      </Typography>
      <Typography paragraph>
        This is a fun project that uses fuzzy logic to help you evaluate your relationship.
        It's not meant to be taken seriously - just a lighthearted way to think about your dating situation!
      </Typography>
      <Typography paragraph>
        The algorithm considers 8 factors: trust, kindness, emotional stability, financial stability,
        attention, effort, physical attraction, and princess treatment.
      </Typography>
      <Typography>
        Created with ❤️ for friends to clone and enjoy.
      </Typography>
    </Container>
  );
}