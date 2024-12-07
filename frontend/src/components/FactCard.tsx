import React from 'react';
import { Card, CardContent, Typography, Chip, Box } from '@mui/material';
import { CheckCircle, XCircle, Clock } from 'lucide-react';
import { Fact } from '../types/fact';

interface FactCardProps {
  fact: Fact;
}

const FactCard: React.FC<FactCardProps> = ({ fact }) => {
  const getStatusIcon = () => {
    switch (fact.verificationStatus) {
      case 'verified':
        return <CheckCircle color="green" size={20} />;
      case 'false':
        return <XCircle color="red" size={20} />;
      default:
        return <Clock color="orange" size={20} />;
    }
  };

  return (
    <Card sx={{ mb: 2, boxShadow: 2 }}>
      <CardContent>
        <Box display="flex" justifyContent="space-between" alignItems="center" mb={1}>
          <Chip label={fact.category} size="small" color="primary" />
          {getStatusIcon()}
        </Box>
        <Typography variant="body1" gutterBottom>
          {fact.statement}
        </Typography>
        {fact.source && (
          <Typography variant="caption" color="text.secondary">
            Source: {fact.source}
          </Typography>
        )}
        <Typography variant="caption" color="text.secondary" display="block">
          Added: {new Date(fact.dateAdded).toLocaleDateString()}
        </Typography>
      </CardContent>
    </Card>
  );
};

export default FactCard;