import React, { useState } from "react";
import { Link as RouterLink } from "react-router-dom";
import { makeStyles } from "@material-ui/core/styles";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
import Link from "@material-ui/core/Link";
import Grid from "@material-ui/core/Grid";
import CircularProgress from "@material-ui/core/CircularProgress";
import IconButton from "@material-ui/core/IconButton";
import Typography from "@material-ui/core/Typography";
import InputAdornment from "@material-ui/core/InputAdornment";
import Visibility from "@material-ui/icons/Visibility";
import VisibilityOff from "@material-ui/icons/VisibilityOff";
import { useTranslation } from "react-i18next";

const useStyles = makeStyles((theme) => ({
    form: {
        width: "100%", // Fix IE 11 issue.
        marginTop: theme.spacing(3),
    },
    submit: {
        margin: theme.spacing(2, 0, 2),
    },
    submitErrorMessage: {
        color: theme.palette.error.main,
        textAlign: "center",
    },
    successMessage: {
        color: theme.palette.success.main,
        textAlign: "center",
    },
    wrapper: {
        position: "relative",
    },
    buttonProgress: {
        position: "absolute",
        top: "50%",
        left: "50%",
        marginTop: "-12px",
        marginLeft: "-12px",
    },
}));

const SignUpForm = ({ onSubmit, authStateHooks, formStateHooks }) => {
    const { submitSuccess, submitError, isLoading } = authStateHooks;
    const { register, handleSubmit, errors, getValues } = formStateHooks;
    const classes = useStyles();
    const [isPasswordHidden, setPasswordHidden] = useState(true);
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
        <form className={classes.form} onSubmit={handleSubmit(onSubmit)}>
            <Grid container spacing={2}>
                <Grid item xs={12} sm={6}>
                    <TextField
                        autoComplete="fname"
                        name="first_name"
                        variant="outlined"
                        required
                        fullWidth
                        id="first_name"
                        label={t("formFields.firstName")}
                        autoFocus
                        inputRef={register(validationSchemas.first_name)}
                        error={errors.first_name !== undefined}
                        helperText={errors?.first_name?.message}
                    />
                </Grid>
                <Grid item xs={12} sm={6}>
                    <TextField
                        variant="outlined"
                        required
                        fullWidth
                        id="last_name"
                        label={t("formFields.lastName")}
                        name="last_name"
                        autoComplete="lname"
                        inputRef={register(validationSchemas.last_name)}
                        error={errors.last_name !== undefined}
                        helperText={errors?.last_name?.message}
                    />
                </Grid>
                <Grid item xs={12}>
                    <TextField
                        variant="outlined"
                        required
                        fullWidth
                        id="email"
                        label={t("formFields.email")}
                        name="email"
                        autoComplete="email"
                        inputRef={register(validationSchemas.email)}
                        error={errors.email !== undefined}
                        helperText={errors?.email?.message}
                    />
                </Grid>
                <Grid item xs={12}>
                    <TextField
                        variant="outlined"
                        required
                        fullWidth
                        name="password"
                        label={t("formFields.password")}
                        type={isPasswordHidden ? "password" : "text"}
                        id="password"
                        autoComplete="new-password"
                        inputRef={register(validationSchemas.password)}
                        error={errors.password !== undefined}
                        helperText={errors?.password?.message}
                        InputProps={{
                            endAdornment: (
                                <InputAdornment position="end">
                                    <IconButton
                                        aria-label={t(
                                            "aria.passwordVisibilityToggle"
                                        )}
                                        onClick={() =>
                                            setPasswordHidden(!isPasswordHidden)
                                        }
                                        onMouseDown={(e) => e.preventDefault()}
                                    >
                                        {isPasswordHidden ? (
                                            <VisibilityOff />
                                        ) : (
                                            <Visibility />
                                        )}
                                    </IconButton>
                                </InputAdornment>
                            ),
                        }}
                    />
                </Grid>
                <Grid item xs={12}>
                    <TextField
                        variant="outlined"
                        required
                        fullWidth
                        name="password2"
                        label={t("formFields.passwordConfirm")}
                        type={isPasswordHidden ? "password" : "text"}
                        id="password2"
                        autoComplete="new-password"
                        inputRef={register(validationSchemas.password2)}
                        error={errors.password2 !== undefined}
                        helperText={errors?.password2?.message}
                        InputProps={{
                            endAdornment: (
                                <InputAdornment position="end">
                                    <IconButton
                                        aria-label={t(
                                            "aria.passwordVisibilityToggle"
                                        )}
                                        onClick={() =>
                                            setPasswordHidden(!isPasswordHidden)
                                        }
                                        onMouseDown={(e) => e.preventDefault()}
                                    >
                                        {isPasswordHidden ? (
                                            <VisibilityOff />
                                        ) : (
                                            <Visibility />
                                        )}
                                    </IconButton>
                                </InputAdornment>
                            ),
                        }}
                    />
                </Grid>
            </Grid>
            {submitError && (
                <Typography className={classes.submitErrorMessage}>
                    {submitError}
                </Typography>
            )}
            {submitSuccess && (
                <Typography className={classes.successMessage}>
                    {submitSuccess}
                </Typography>
            )}
            <div className={classes.wrapper}>
                <Button
                    type="submit"
                    fullWidth
                    variant="contained"
                    color="primary"
                    className={classes.submit}
                >
                    {t("signUp")}
                </Button>
                {isLoading && (
                    <CircularProgress
                        size={24}
                        className={classes.buttonProgress}
                    />
                )}
            </div>
            <Grid container justify="flex-end">
                <Grid item>
                    <Link variant="body2" component={RouterLink} to="/signin">
                        {t("signInLink")}
                    </Link>
                </Grid>
            </Grid>
        </form>
    );
};

export default SignUpForm;
