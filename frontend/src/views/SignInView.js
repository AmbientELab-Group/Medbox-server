import React, { useState } from "react";
import { useHistory } from "react-router-dom";
import LockOutlinedIcon from "@material-ui/icons/LockOutlined";
import { makeStyles } from "@material-ui/core/styles";
import Avatar from "@material-ui/core/Avatar";
import Paper from "@material-ui/core/Paper";
import Box from "@material-ui/core/Box";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import Copyright from "../components/Copyright";
import ErrorSnack from "../components/ErrorSnack";
import SignInForm from "../components/SignInForm";
import { useForm } from "react-hook-form";
import { login } from "../contexts/authProvider";
import { publicAccountFetch } from "../api/publicFetch";
 

const useStyles = makeStyles((theme) => ({
    root: {
        height: "100vh",
    },
    image: {
        backgroundImage: "url(https://source.unsplash.com/random)",
        backgroundRepeat: "no-repeat",
        backgroundColor:
        theme.palette.type === "light" ? theme.palette.grey[50] : theme.palette.grey[900],
        backgroundSize: "cover",
        backgroundPosition: "center",
    },
    paper: {
        margin: theme.spacing(8, 4),
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
    },
    avatar: {
        margin: theme.spacing(1),
        backgroundColor: theme.palette.secondary.main,
    },
}));

const SignInView = () => {
    const classes = useStyles();
    const { register, handleSubmit, errors } = useForm({mode: "onBlur"});
    const [ submitSuccess, setSubmitSuccess ] = useState("");
    const [ submitError, setSubmitError ] = useState("");
    const [ isLoading, setLoading ] = useState(false);
    const [ connectionError, setConnectionError ] = useState(false);
    const history = useHistory();

    const onSubmit = async credentials => {
        try {
            setLoading(true);
            const { data } = await publicAccountFetch.post(
                "/signin",
                credentials
            );
            
            login(data);
            setSubmitSuccess("Authentication successful!");
            setSubmitError("");
            setTimeout(async () => {
                history.push('/dashboard');
            }, 1000);

        } catch (error) {
            setLoading(false);

            if (error.response) {
                const { data } = error.response;
                console.error(data.detail);
                setSubmitError(data.detail);
                setSubmitSuccess("");
            }
            else if (error.request) {
                console.log("error request");
                console.error(JSON.stringify(error));
                setConnectionError(true);
            }
            else {
                console.error("Uhh ohh! Something went a bit sideways...");
                console.error(error);
            }
        } 
    }

    return (
        <Grid container component="main" className={classes.root}>
        <ErrorSnack error={connectionError} setError={setConnectionError}>
            Please check your internet connection and try again...
        </ErrorSnack>
        <Grid item xs={false} sm={4} md={7} className={classes.image} />
        <Grid item xs={12} sm={8} md={5} component={Paper} elevation={6} square>
            <div className={classes.paper}>
            <Avatar className={classes.avatar}>
                <LockOutlinedIcon />
            </Avatar>
            <Typography component="h1" variant="h5">
                Sign in
            </Typography>
            <SignInForm 
                onSubmit={onSubmit} 
                authStateHooks={{submitSuccess, submitError, isLoading}}
                formStateHooks={{register, handleSubmit, errors}}
            />
            <Box mt={5}>
                <Copyright />
            </Box>
            </div>
        </Grid>
        </Grid>
    );
}

export default SignInView;