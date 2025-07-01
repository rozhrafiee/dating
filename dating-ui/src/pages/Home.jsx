import { useState } from 'react';
import { Container, Button, Box, Typography } from '@mui/material';
import AttributeSlider from '../components/AttributeSlider';
import ResultCard from '../components/ResultCard';

export default function Home() {
  const [values, setValues] = useState({
    trust: 5,
    kindness: 5,
    emotional_stability: 5,
    financial_stability: 5,
    attention: 5,
    effort: 5,
    physical_attraction: 5,
    princess_treatment: 5
  });
  
  const [decision, setDecision] = useState(null);

  const handleChange = (key) => (e, newValue) => {
    setValues(prev => ({ ...prev, [key]: newValue }));
  };

  const calculateDecision = () => {
    // Mock decision for frontend testing
    const total = Object.values(values).reduce((sum, val) => sum + val, 0);
    if (total > 60) setDecision("Keep Him 💖");
    else if (total < 40) setDecision("Dump Him 💔");
    else setDecision("Maybe 🤔");
  };

  return (
    <Container maxWidth="md">
      <Box sx={{ my: 4 }}>
        <Typography variant="h4" gutterBottom>
          Rate Your Partner
        </Typography>
        
        {Object.entries(values).map(([key, value]) => (
          <AttributeSlider 
            key={key}
            label={key.replace('_', ' ')}
            value={value}
            onChange={handleChange(key)}
          />
        ))}
        
        <Button 
          variant="contained" 
          size="large" 
          fullWidth
          onClick={calculateDecision}
          sx={{ mt: 2 }}
        >
          Should I Stay or Should I Go?
        </Button>
        
        {decision && <ResultCard decision={decision} />}
      </Box>
    </Container>
  );
}