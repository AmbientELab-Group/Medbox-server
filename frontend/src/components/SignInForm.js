import React from "react";
import { Link as RouterLink } from "react-router-dom";
import Grid from "@material-ui/core/Grid";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import Checkbox from "@material-ui/core/Checkbox";
import Link from "@material-ui/core/Link";
import SubmitMessage from "./Forms/SubmitMessage";
import TextField from "./Forms/TextField";
import PasswordField from "./Forms/PasswordField";
import LoadingButton from "./LoadingButton";
import styled from "styled-components";
import { useTranslation } from "react-i18next";

const StyledForm = styled.form`
    width: 100%;
`;

const SignInForm = ({ onSubmit, authStateHooks, formStateHooks }) => {
    const { submitSuccess, submitError, isLoading } = authStateHooks;
    const { register, handleSubmit, errors } = formStateHooks;
    const { t } = useTranslation("account");

    const validationSchemas = {
        email: {
            required: t("formValidation.required", {
                field: t("formFields.email"),
            }),
            pattern: {
                value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i,
                message: t("formValidation.invalid", {
                    field: t("formFields.email"),
                }),
            },
        },
        password: {
            required: t("formValidation.required", {
                field: t("formFields.password"),
            }),
        },
    };

    return (
        <StyledForm onSubmit={handleSubmit(onSubmit)}>
            <Grid container spacing={3}>
                <Grid item xs={12}>
                    <TextField
                        id="email"
                        name="email"
                        autoComplete="email"
                        label={t("formFields.email")}
                        inputRef={register(validationSchemas.email)}
                        error={errors.email !== undefined}
                        helperText={errors?.email?.message}
                        required
                    />
                </Grid>
                <Grid item xs={12}>
                    <PasswordField
                        id="password"
                        name="password"
                        autoComplete="current-password"
                        label={t("formFields.password")}
                        inputRef={register(validationSchemas.password)}
                        error={errors.password !== undefined}
                        helperText={errors?.password?.message}
                        required
                    />
                </Grid>
                <Grid item xs={12}>
                    <FormControlLabel
                        control={<Checkbox value="remember" color="primary" />}
                        label={t("rememberMe")}
                    />
                </Grid>
                <Grid item xs={12}>
                    <SubmitMessage $error={!!submitError}>
                        {submitError}
                    </SubmitMessage>
                    <SubmitMessage $success={!!submitSuccess}>
                        {submitSuccess}
                    </SubmitMessage>
                </Grid>
                <Grid item xs={12}>
                    <LoadingButton
                        type="submit"
                        fullWidth
                        isLoading={isLoading}
                    >
                        {t("signIn")}
                    </LoadingButton>
                </Grid>
                <Grid
                    container
                    item
                    direction="column"
                    alignItems="flex-end"
                    spacing={2}
                >
                    <Grid item>
                        <Link href="#" variant="body2">
                            {t("passwordRecoveryLink")}
                        </Link>
                    </Grid>
                    <Grid item>
                        <Link
                            variant="body2"
                            component={RouterLink}
                            to="/signup"
                        >
                            {t("signUpLink")}
                        </Link>
                    </Grid>
                </Grid>
            </Grid>
        </StyledForm>
    );
};

export default SignInForm;
