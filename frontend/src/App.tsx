import React, { useState } from 'react';
import {
  Container,
  Typography,
  Box,
  ThemeProvider,
  createTheme,
  CssBaseline,
} from '@mui/material';
import { Database } from 'lucide-react';
import SearchBar from './components/SearchBar';
import FactList from './components/FactList';
import { Fact } from './types/fact';

// Sample data - replace with actual API calls later
const sampleFacts: Fact[] = [
  {
    id: '1',
    statement: 'Water boils at 100 degrees Celsius at sea level.',
    isVerified: true,
    verificationStatus: 'verified',
    category: 'Science',
    dateAdded: '2024-02-20',
    source: 'Physics Textbook',
  },
  {
    id: '2',
    statement: 'The Great Wall of China is visible from space.',
    isVerified: true,
    verificationStatus: 'false',
    category: 'History',
    dateAdded: '2024-02-19',
    source: 'NASA',
  },
];

const theme = createTheme({
  palette: {
    mode: 'light',
    primary: {
      main: '#1976d2',
    },
  },
});

function App() {
  const [facts, setFacts] = useState<Fact[]>(sampleFacts);
  const [searchQuery, setSearchQuery] = useState('');

  const handleSearch = (query: string) => {
    setSearchQuery(query);
    // Filter facts based on search query
    const filteredFacts = sampleFacts.filter((fact) =>
      fact.statement.toLowerCase().includes(query.toLowerCase())
    );
    setFacts(filteredFacts);
  };

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Container maxWidth="md">
        <Box py={4}>
          <Box display="flex" alignItems="center" justifyContent="center" mb={4}>
            <Database size={32} />
            <Typography variant="h4" component="h1" ml={2}>
              Fact Check Hub
            </Typography>
          </Box>
          <SearchBar onSearch={handleSearch} />
          <FactList facts={facts} />
        </Box>
      </Container>
    </ThemeProvider>
  );
}

export default App;