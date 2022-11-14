import React, { useState } from 'react'
import axios from 'axios'
import { Buffer } from 'buffer'

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

    const hostAddress = process.env.REACT_APP_GENERATOR_HOST_ADDRESS
    const port = process.env.REACT_APP_GENERATOR_PORT
    const textMaxLength = 50
    //States
    const [showFilename, setShowFilename] = useState(false)
    const [loading, setLoading] = useState(false)
    const [showError, setShowError] = useState(false)
    const [errorMsg, setErrorMsg] = useState("Default Error")
    const [fileToUpload, setFileToUpload] = useState()
    const [values, setValues] = useState({
        topText: "",
        btmText: "",
        filename: ""
    });
    const [meme, setMeme] = useState()
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
        setFileToUpload(event.target.files[0])
    }

    //Generate Meme
    function handleGenerateMeme() {
        let formData = new FormData();
        formData.append('topText', values.topText);   
        formData.append('btmText', values.btmText);
        formData.append('memeImage', fileToUpload)
        const config = {     
            headers: { 'Content-Type': 'multipart/form-data' } , responseType: 'arraybuffer' 
        }
        let url = "http://" + hostAddress + ":" + port + "/generateMeme"
        

        axios.post(url, formData, config)
        .catch(error => {
            if (!error.response) {
                setErrorMsg("Server is Down!")
            } else {
                setErrorMsg("Meme Generator is Down! Please contact the Administrator")
                console.log(error.response.data)
            }
            setShowError(true)
        })
        .then(response => {
            setShowError(false)
            setShowMeme(true)
          
            let base64ImageString = Buffer.from(response.data, 'binary').toString('base64')
            let srcValue = "data:image/png;base64,"+base64ImageString
        
            
            setMeme(srcValue)
        });
        

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
                    <TextField id="topText" label="Top Text" variant="standard" value={values.topText} onChange={updateTopText}  inputProps={{ maxLength: textMaxLength }} sx={{ margin: 1, width: '18ch' }} />
                </Grid>
                <Grid item xs={12}>
                    <TextField id="bottomText" label="Bottom Text" variant="standard" value={values.btmText} onChange={updateBtmText} inputProps={{ maxLength: textMaxLength }} sx={{ margin: 1, width: '18ch' }} />
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
                        onClick={handleGenerateMeme}
                        loadingIndicator="Generating..."
                        loadingPosition="end"
                        variant="contained">
                        Generate Meme
                    </LoadingButton>
                </Grid>

                <Grid hidden={!showError} item xs={12}>
                    <InputLabel error="true" variant="standard">
                        {errorMsg}
                    </InputLabel>
                </Grid>

                <Grid hidden={!showMeme} item xs={12}>
                    <Box
                        component="img"
                        sx={{
                        height: 266,
                        width: 400,
                        maxHeight: { xs: 266},
                        maxWidth: { xs: 400},
                        }}
                        src={meme}
                    />

                </Grid>


            </Grid>
        </Paper>
    );
}

export default MemeForm;