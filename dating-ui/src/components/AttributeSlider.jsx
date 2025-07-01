import { Slider, Typography, Stack } from '@mui/material';

export default function AttributeSlider({ label, value, onChange }) {
  return (
    <Stack spacing={2} sx={{ width: '100%', mb: 3 }}>
      <Typography gutterBottom>
        {label}: {value}
      </Typography>
      <Slider
        value={value}
        onChange={onChange}
        aria-label={label}
        min={0}
        max={10}
        marks
        valueLabelDisplay="auto"
      />
    </Stack>
  );
}