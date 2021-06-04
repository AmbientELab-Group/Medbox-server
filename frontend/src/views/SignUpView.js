import React, { useState } from "react";
import { useHistory } from "react-router-dom";
import LockOutlinedIcon from "@material-ui/icons/LockOutlined";
import Grid from "@material-ui/core/Grid";
import Box from "@material-ui/core/Box";
import Typography from "@material-ui/core/Typography";
import Container from "@material-ui/core/Container";
import Paper from "@material-ui/core/Paper";
import Avatar from "../components/Forms/Avatar";
import Copyright from "../components/Copyright";
import ErrorSnack from "../components/ErrorSnack";
import SignUpForm from "../components/SignUpForm";
import { login } from "../contexts/authProvider";
import { publicAccountFetch } from "../api/publicFetch";
import { useForm } from "react-hook-form";
import { useTranslation } from "react-i18next";
import SignUpModal from "../components/Forms/SignUpModal";

const SignUpView = () => {
    const { register, handleSubmit, errors, getValues, setError } = useForm({
        mode: "onBlur",
    });
    const [submitSuccess, setSubmitSuccess] = useState("");
    const [submitError, setSubmitError] = useState("");
    const [isLoading, setLoading] = useState(false);
    const [connectionError, setConnectionError] = useState(false);
    const history = useHistory();
    const { t } = useTranslation("account");

    const [modalOpen, setModalOpen] = useState(true);

    const onSubmit = async (credentials) => {
        try {
            setLoading(true);
            const { data } = await publicAccountFetch.post(
                "/signup",
                credentials
            );

            login({ access: data.access_token, refresh: data.refresh_token });
            setSubmitSuccess(data.response);
            setSubmitError("");
            setTimeout(() => {
                history.push("/dashboard");
            }, 1000);
        } catch (error) {
            setLoading(false);
            if (error.response) {
                const { data } = error.response;
                console.error(data);
                setSubmitError(t("createError"));
                setSubmitSuccess("");
                if (data) {
                    Object.entries(data).forEach((error) => {
                        const [fieldName, errorArray] = error;
                        console.log(fieldName);
                        console.log(errorArray);
                        setError(fieldName, {
                            type: "manual",
                            message:
                                errorArray[0].charAt(0).toUpperCase() +
                                errorArray[0].slice(1),
                        });
                    });
                }
            } else if (error.request) {
                console.error(JSON.stringify(error));
                setConnectionError(true);
            } else {
                setSubmitError(t("fatalError"));
                setSubmitSuccess("");
                console.error("Fatal error:");
                console.error(error);
            }
        }
    };

    return (
        <Container component="main" maxWidth="sm">
            <ErrorSnack error={connectionError} setError={setConnectionError}>
                {t("connectionError")}
            </ErrorSnack>
            <SignUpModal
                open={modalOpen}
                handleClose={() => setModalOpen(false)}
            />
            <Box
                mt={{ xs: 2, sm: 4, md: 8 }}
                mb={{ xs: 2, sm: 4, md: 8 }}
                p={{ xs: 2, sm: 4, md: 8 }}
                component={Paper}
                elevation={6}
            >
                <Grid container spacing={3}>
                    <Grid
                        item
                        container
                        direction="column"
                        alignItems="center"
                        xs={12}
                    >
                        <Avatar>
                            <LockOutlinedIcon />
                        </Avatar>
                        <Typography variant="h2">{t("signUp")}</Typography>
                    </Grid>
                    <Grid item>
                        <SignUpForm
                            onSubmit={() => {
                                console.log("Signing up is turned off.");
                                setModalOpen(true);
                            }}
                            //onSubmit={onSubmit}
                            authStateHooks={{
                                submitSuccess,
                                submitError,
                                isLoading,
                            }}
                            formStateHooks={{
                                register,
                                handleSubmit,
                                errors,
                                getValues,
                            }}
                        />
                    </Grid>
                    <Grid item container justify="center">
                        <Copyright />
                    </Grid>
                </Grid>
            </Box>
        </Container>
    );
};

export default SignUpView;
