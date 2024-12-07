import React from 'react';
import { Box, Typography } from '@mui/material';
import FactCard from './FactCard';
import { Fact } from '../types/fact';

interface FactListProps {
  facts: Fact[];
}

const FactList: React.FC<FactListProps> = ({ facts }) => {
  if (facts.length === 0) {
    return (
      <Box textAlign="center" py={4}>
        <Typography variant="h6" color="text.secondary">
          No facts available
        </Typography>
      </Box>
    );
  }

  return (
    <Box>
      {facts.map((fact) => (
        <FactCard key={fact.id} fact={fact} />
      ))}
    </Box>
  );
};

export default FactList;