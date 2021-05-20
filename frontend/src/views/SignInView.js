import React, { useState } from "react";
import { useHistory } from "react-router-dom";
import styled from "styled-components";
import LockOutlinedIcon from "@material-ui/icons/LockOutlined";
import Box from "@material-ui/core/Box";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import Paper from "@material-ui/core/Paper";
import Copyright from "../components/Copyright";
import ErrorSnack from "../components/ErrorSnack";
import SignInForm from "../components/SignInForm";
import Avatar from "../components/Forms/Avatar";
import { login } from "../contexts/authProvider";
import { useForm } from "react-hook-form";
import { useTranslation } from "react-i18next";
import { publicAccountFetch } from "../api/publicFetch";
import background from "../assets/img/Sign_in.png";

const MainContainer = styled.main`
    height: 100vh;
`;

const ImageWrapper = styled(Grid)`
    background-image: url(${background});
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;

    ${({ theme }) => theme.breakpoints.up("md")} {
        background-size: contain;
    }
`;

const SignInView = () => {
    const { register, handleSubmit, errors, setError } = useForm({
        mode: "onBlur",
    });
    const [submitSuccess, setSubmitSuccess] = useState("");
    const [submitError, setSubmitError] = useState("");
    const [isLoading, setLoading] = useState(false);
    const [connectionError, setConnectionError] = useState(false);
    const history = useHistory();
    const { t } = useTranslation("account");

    const onSubmit = async (credentials) => {
        try {
            setLoading(true);
            const { data } = await publicAccountFetch.post(
                "/signin",
                credentials
            );

            login(data);
            setSubmitSuccess(t("successMessage"));
            setSubmitError("");
            setTimeout(async () => {
                history.push("/dashboard");
            }, 1000);
        } catch (error) {
            setLoading(false);

            if (error.response) {
                const { data } = error.response;
                console.error(data.detail);
                setSubmitError(data.detail);
                setSubmitSuccess("");
                setError("email", {
                    type: "manual",
                    message: t("authError"),
                });
            } else if (error.request) {
                console.log("Request error:");
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
        <Grid container component={MainContainer}>
            <ErrorSnack error={connectionError} setError={setConnectionError}>
                {t("connectionError")}
            </ErrorSnack>
            <ImageWrapper item xs={false} sm={4} md={7} />
            <Grid
                item
                xs={12}
                sm={8}
                md={5}
                component={Paper}
                elevation={6}
                square
            >
                <Box p={4}>
                    <Grid
                        container
                        spacing={3}
                        direction="column"
                        justify="flex-start"
                        alignItems="center"
                    >
                        <Grid
                            item
                            container
                            direction="column"
                            alignItems="center"
                        >
                            <Avatar>
                                <LockOutlinedIcon />
                            </Avatar>
                            <Typography variant="h2">{t("signIn")}</Typography>
                        </Grid>
                        <Grid item>
                            <SignInForm
                                onSubmit={onSubmit}
                                authStateHooks={{
                                    submitSuccess,
                                    submitError,
                                    isLoading,
                                }}
                                formStateHooks={{
                                    register,
                                    handleSubmit,
                                    errors,
                                }}
                            />
                        </Grid>
                        <Grid item container justify="center">
                            <Copyright />
                        </Grid>
                    </Grid>
                </Box>
            </Grid>
        </Grid>
    );
};

export default SignInView;
