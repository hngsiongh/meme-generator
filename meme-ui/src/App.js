import React , { useState } from 'react'
import Box from '@mui/material/Box';
import MemeForm from './Form/MemeForm';

function App() {

  const [values, setvalues] = useState({
    topText: "",
    btmText: "",
    filename: ""
  });

  return (
    <div>
      <Box
          display="flex"
          justifyContent="center"
          alignItems="center"
          minHeight="100vh"
        >
          <MemeForm />
      </Box>
         
    </div>
  );
}

export default App;
