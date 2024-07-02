import React from "react";
import { Pagination, Box } from "@mui/material";

const Paginator = ({ currentPage, totalPages, onPageChange }) => {
  const handleChange = (event, value) => {
    onPageChange(value);
  };

  return (
    <Box sx={{ width: '80%', margin: '0 auto', maxWidth: 800 }}>
      <Pagination 
        count={totalPages} 
        page={currentPage} 
        onChange={handleChange} 
      />
    </Box>
  );
};

export default Paginator;
