import React, { useState } from "react";
import Avatar from "@material-ui/core/Avatar";
import Box from "@material-ui/core/Box";
import LockOutlinedIcon from "@material-ui/icons/LockOutlined";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core/styles";
import Container from "@material-ui/core/Container";
import Copyright from "../components/Copyright";
import { useHistory } from "react-router-dom";
import jwt_decode from "jwt-decode";
import { publicAccountFetch } from "../api/publicFetch";
import { useForm } from "react-hook-form";
import ErrorSnack from "../components/ErrorSnack";
import { useAuth } from "../contexts/AuthContext";
import SignUpForm from "../components/SignUpForm";

const useStyles = makeStyles((theme) => ({
    paper: {
        marginTop: theme.spacing(8),
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
    },
    avatar: {
        margin: theme.spacing(1),
        backgroundColor: theme.palette.secondary.main,
    },
}));

const SignUpView = () => {
    const classes = useStyles();
    const { register, handleSubmit, errors, getValues, setError } = useForm({mode: "onBlur"});
    const [ , setAuthState ] = useAuth();
    const [ submitSuccess, setSubmitSuccess ] = useState("");
    const [ submitError, setSubmitError ] = useState("");
    const [ isLoading, setLoading ] = useState(false);
    const [ connectionError, setConnectionError ] = useState(false);
    const history = useHistory();

    const onSubmit = async credentials => {
        try {
            setLoading(true);
            const { data } = await publicAccountFetch.post(
            "/signup",
            credentials
            );

            const accessDecoded = jwt_decode(data.access_token);
            const refreshDecoded = jwt_decode(data.refresh_token);

            const stateData = {
                access: {
                    token: data.access_token,
                    expiresAt: accessDecoded.exp,
                },
                refresh: {
                    token: data.refresh_token,
                    expiresAt: refreshDecoded.exp,
                },
                userInfo: {
                    id: accessDecoded.user_id,
                    email: data.email,
                    firstName: data.first_name,
                    lastName: data.last_name
                }
            };

            setAuthState(stateData);
            setSubmitSuccess(data.response);
            setSubmitError("");

            setTimeout(() => {
                history.push('/dashboard');
            }, 1000);
        } catch (error) {
            setLoading(false);
            if (error.response) {
            const { data } = error.response;
            console.error(data);
            setSubmitError("Cannot create account.");
            setSubmitSuccess("");
            if (data) {
                Object.entries(data).forEach((error) => {
                    const [ fieldName, errorArray ] = error;
                    console.log(fieldName);
                    console.log(errorArray);
                    setError(fieldName, { 
                        type: "manual", 
                        message: errorArray[0].charAt(0).toUpperCase() + errorArray[0].slice(1)
                    });
                }); 
            }
            }
            else if (error.request) {
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
        <Container component="main" maxWidth="xs">
            <ErrorSnack error={connectionError} setError={setConnectionError}>
                Please check your internet connection and try again...
            </ErrorSnack>
            <div className={classes.paper}>
                <Avatar className={classes.avatar}>
                    <LockOutlinedIcon />
                </Avatar>
                <Typography component="h1" variant="h5">
                    Sign up
                </Typography>
                <SignUpForm
                    onSubmit={onSubmit} 
                    authStateHooks={{submitSuccess, submitError, isLoading}}
                    formStateHooks={{register, handleSubmit, errors, getValues}}
                />
            </div>
            <Box mt={5}>
                <Copyright />
            </Box>
        </Container>
    );
}

export default SignUpView;
