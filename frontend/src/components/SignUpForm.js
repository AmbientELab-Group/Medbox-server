import React from "react";
import { Link as RouterLink } from "react-router-dom";
import Link from "@material-ui/core/Link";
import Grid from "@material-ui/core/Grid";
import TextField from "./Forms/TextField";
import PasswordField from "./Forms/PasswordField";
import SubmitMessage from "./Forms/SubmitMessage";
import { useTranslation } from "react-i18next";
import LoadingButton from "./LoadingButton";
import styled from "styled-components";

const StyledForm = styled.form`
    width: 100%;
`;

const SignUpForm = ({ onSubmit, authStateHooks, formStateHooks }) => {
    const { submitSuccess, submitError, isLoading } = authStateHooks;
    const { register, handleSubmit, errors, getValues } = formStateHooks;
    const { t } = useTranslation("account");

    const validationSchemas = {
        first_name: {
            required: t("formValidation.required", {
                field: t("formFields.firstName"),
            }),
            maxLength: {
                value: 30,
                message: t("formValidation.tooLong", {
                    value: 30,
                    field: t("formFields.firstName"),
                }),
            },
        },
        last_name: {
            required: t("formValidation.required", {
                field: t("formFields.lastName"),
            }),
            maxLength: {
                value: 150,
                message: t("formValidation.tooLong", {
                    value: 150,
                    field: t("formFields.lastName"),
                }),
            },
        },
        email: {
            required: t("formValidation.required", {
                field: t("formFields.email"),
            }),
            maxLength: {
                value: 128,
                message: t("formValidation.tooLong", {
                    value: 128,
                    field: t("formFields.email"),
                }),
            },
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
            minLength: {
                value: 8,
                message: t("formValidation.tooShort", {
                    value: 8,
                    field: t("formFields.password"),
                }),
            },
            maxLength: {
                value: 128,
                message: t("formValidation.tooLong", {
                    value: 128,
                    field: t("formFields.password"),
                }),
            },
        },
        password2: {
            required: t("formValidation.required", {
                field: t("formFields.passwordConfirm"),
            }),
            validate: (value) =>
                value === getValues("password") ||
                t("formValidation.passwordMatch"),
        },
    };

    return (
        <StyledForm onSubmit={handleSubmit(onSubmit)}>
            <Grid container spacing={3}>
                <Grid item xs={12} sm={6}>
                    <TextField
                        id="first_name"
                        name="first_name"
                        autoComplete="fname"
                        label={t("formFields.firstName")}
                        inputRef={register(validationSchemas.first_name)}
                        error={errors.first_name !== undefined}
                        helperText={errors?.first_name?.message}
                        required
                    />
                </Grid>
                <Grid item xs={12} sm={6}>
                    <TextField
                        id="last_name"
                        name="last_name"
                        autoComplete="lname"
                        label={t("formFields.lastName")}
                        inputRef={register(validationSchemas.last_name)}
                        error={errors.last_name !== undefined}
                        helperText={errors?.last_name?.message}
                        required
                    />
                </Grid>
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
                        autoComplete="new-password"
                        label={t("formFields.password")}
                        inputRef={register(validationSchemas.password)}
                        error={errors.password !== undefined}
                        helperText={errors?.password?.message}
                        required
                    />
                </Grid>
                <Grid item xs={12}>
                    <PasswordField
                        id="password2"
                        name="password2"
                        autoComplete="new-password"
                        label={t("formFields.passwordConfirm")}
                        inputRef={register(validationSchemas.password2)}
                        error={errors.password2 !== undefined}
                        helperText={errors?.password2?.message}
                        required
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
                        {t("signUp")}
                    </LoadingButton>
                </Grid>
                <Grid item container justify="flex-end">
                    <Grid item>
                        <Link
                            variant="body2"
                            component={RouterLink}
                            to="/signin"
                        >
                            {t("signInLink")}
                        </Link>
                    </Grid>
                </Grid>
            </Grid>
        </StyledForm>
    );
};

export default SignUpForm;
