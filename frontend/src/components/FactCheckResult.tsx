import React from 'react';
import { Paper, Typography, Box } from '@mui/material';
import { CheckCircle, XCircle } from 'lucide-react';

interface FactCheckResultProps {
  result: string;
}

const FactCheckResult: React.FC<FactCheckResultProps> = ({ result }) => {
  const isVerified = !result.includes("incorrect");


  return (
    <Paper 
      elevation={3}
      sx={{
        p: 3,
        mt: 3,
        backgroundColor: isVerified ? 'rgba(46, 125, 50, 0.1)' : 'rgba(211, 47, 47, 0.1)',
        borderRadius: 2
      }}
    >
      <Box sx={{ display: 'flex', alignItems: 'center', gap: 2, mb: 2 }}>
        {isVerified ? (
          <CheckCircle color="#2e7d32" size={24} />
        ) : (
          <XCircle color="#d32f2f" size={24} />
        )}
        <Typography 
          variant="h6" 
          color={isVerified ? 'success.main' : 'error.main'}
        >
          {isVerified ? 'Statement Verified' : 'Statement Incorrect'}
        </Typography>
      </Box>
      
      <Typography variant="body1" sx={{ ml: 4 }}>
        {result}
      </Typography>

     
    </Paper>
  );
}

export default FactCheckResult;
