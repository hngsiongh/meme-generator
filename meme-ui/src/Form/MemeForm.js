import React, { useState } from 'react'

import {
    TextField,
    Paper,
    Grid,
    Button,
    InputLabel,
    Box
} from '@mui/material'
import LoadingButton from '@mui/lab/LoadingButton';

function MemeForm() {

    //States
    const [showFilename, setShowFilename] = useState(false)
    const [loading, setLoading] = useState(false);
    const [values, setValues] = useState({
        topText: "",
        btmText: "",
        filename: ""
    });
    const [meme, setMeme] = useState("https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&w=350&dpr=2")
    const [showMeme, setShowMeme] = useState(false);

    //Set Top Text for Meme (Can be Empty String)
    function updateTopText(event) {
        setValues( prevValues => {
            return {...prevValues,topText: event.target.value}
        })
        
    }

    //Set Bottom Text for Meme (Can be Empty String)
    function updateBtmText(event) {
        setValues( prevValues => {
            return {...prevValues,btmText: event.target.value}
        })
    }

    //Ensure File Upload 
    function handleFileUpdateSubmit(event) {
        var file = event.target.files[0]
        var filename = file.name
        setShowFilename(true)
        setValues( prevValues => {
            return {...prevValues,filename: filename}
        })
    }

    return (
        <Paper>
            <Grid
                container
                padding={7}
                spacing={2}
                direction="column"
                alignItems="center"
            >
                <Grid item xs={12}>
                    <h1>Meme Generator</h1>
                </Grid>
                <Grid item xs={12}>
                    <TextField id="topText" label="Top Text" variant="standard" value={values.topText} onChange={updateTopText} sx={{ margin: 1, width: '18ch' }} />
                </Grid>
                <Grid item xs={12}>
                    <TextField id="bottomText" label="Bottom Text" variant="standard" value={values.btmText} onChange={updateBtmText} sx={{ margin: 1, width: '18ch' }} />
                </Grid>
                <Grid item xs={12}>
                    <Button variant="contained" component="label">
                        Upload Image
                        <input hidden accept="image/jpeg, image/png" type="file" onChange={handleFileUpdateSubmit}/>
                    </Button>       
                </Grid>
                <Grid hidden={!showFilename} item xs={12}>
                    <InputLabel variant="standard">
                        {values.filename}
                    </InputLabel>
                </Grid>

                <Grid item xs={12}>
                    <LoadingButton
                        loading={loading}
                        disabled={!showFilename}
                        loadingIndicator="Generating..."
                        loadingPosition="end"
                        variant="contained">
                        Generate Meme
                    </LoadingButton>
                </Grid>

                <Grid hidden={showMeme} item xs={12}>
                    <Box
                        component="img"
                        sx={{
                        height: 233,
                        width: 350,
                        maxHeight: { xs: 233, md: 167 },
                        maxWidth: { xs: 350, md: 250 },
                        }}
                        src={meme}
                    />
                </Grid>


            </Grid>
        </Paper>
    );
}

export default MemeForm;