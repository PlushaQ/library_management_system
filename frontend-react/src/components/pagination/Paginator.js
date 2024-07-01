import React from "react"
import { Pagination, Box } from "@mui/material"

const Paginator = (pageInfo) =>
{
    return (
        <>
          <Box sx={{ width: '80%', margin: '0 auto', maxWidth: 800 }}>
            <Pagination count={11} defaultPage={6} /> 
          </Box>
        </>
    )
}


export default Paginator;