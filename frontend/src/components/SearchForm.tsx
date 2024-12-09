import React, { useState } from 'react';
import { Button, TextField, Box, Typography } from '@mui/material';
import axios from 'axios';
import FactCheckResult from './FactCheckResult';

const SearchForm = () => {
  // State to handle the search input and the API response
  const [searchQuery, setSearchQuery] = useState('');
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  // Function to handle the API request
  const handleSearch = async () => {
    if (!searchQuery) return; // Don't send empty search queries

    setLoading(true);
    setError('');
    try {
      const response = await axios.post('http://0.0.0.0:8001/v1/fact-check', {
        bucket_name: "fact-check-hub",
        s3_key: "sample-political-facts.txt",
        statement: searchQuery,
        openai_api_key: "",
      });

      setResponse(response.data); // Handle API response
    } catch (err) {
      setError('Failed to fetch data'); // Handle error
    } finally {
      setLoading(false); // Reset loading state
    }
  };

  return (
    <Box
      sx={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        maxWidth: '400px',
        margin: '0 auto',
        padding: '20px',
      }}
    >
      <Typography variant="h5" gutterBottom>Fact-Check Search</Typography>

      {/* Search Textbox */}
      <TextField
        label="Enter statement to check"
        variant="outlined"
        fullWidth
        value={searchQuery}
        onChange={(e) => setSearchQuery(e.target.value)}
        sx={{ marginBottom: '16px' }}
      />

      {/* Search Button */}
      <Button
        variant="contained"
        onClick={handleSearch}
        disabled={loading}
        sx={{ marginBottom: '16px' }}
      >
        {loading ? 'Searching...' : 'Search'}
      </Button>

      {/* Error Handling */}
      {error && <Typography color="error">{error}</Typography>}

      {/* API Response */}
      {response && (
            <FactCheckResult result={response['validation_result']} />
          )}
    </Box>
  );
};

export default SearchForm;
