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
import SearchForm from './components/SearchForm';


const theme = createTheme({
  palette: {
    mode: 'light',
    primary: {
      main: '#1976d2',
    },
  },
});

function App() {

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
          <SearchForm/>
        </Box>
      </Container>
    </ThemeProvider>
  );
}

export default App;