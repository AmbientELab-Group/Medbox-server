import React, { useState } from "react";
import { Link as RouterLink } from "react-router-dom";
import { makeStyles } from "@material-ui/core/styles";
import Grid from "@material-ui/core/Grid";
import TextField from "@material-ui/core/TextField";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import Checkbox from "@material-ui/core/Checkbox";
import Link from "@material-ui/core/Link";
import CircularProgress from "@material-ui/core/CircularProgress";
import IconButton from "@material-ui/core/IconButton";
import Typography from "@material-ui/core/Typography";
import InputAdornment from "@material-ui/core/InputAdornment";
import Visibility from "@material-ui/icons/Visibility";
import VisibilityOff from "@material-ui/icons/VisibilityOff";
import PrimaryButton from "./PrimaryButton";
import { useTranslation } from "react-i18next";

const useStyles = makeStyles((theme) => ({
    form: {
        width: "100%", // Fix IE 11 issue.
        marginTop: theme.spacing(1),
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

const SignInForm = ({ onSubmit, authStateHooks, formStateHooks }) => {
    const { submitSuccess, submitError, isLoading } = authStateHooks;
    const { register, handleSubmit, errors } = formStateHooks;
    const classes = useStyles();
    const [isPasswordHidden, setPasswordHidden] = useState(true);
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
        <form className={classes.form} onSubmit={handleSubmit(onSubmit)}>
            <TextField
                variant="outlined"
                margin="normal"
                required
                fullWidth
                id="email"
                label={t("formFields.email")}
                name="email"
                autoComplete="email"
                autoFocus
                inputRef={register(validationSchemas.email)}
                error={errors.email !== undefined}
                helperText={errors?.email?.message}
            />
            <TextField
                variant="outlined"
                margin="normal"
                required
                fullWidth
                name="password"
                label={t("formFields.password")}
                type={isPasswordHidden ? "password" : "text"}
                id="password"
                autoComplete="current-password"
                inputRef={register(validationSchemas.password)}
                error={errors.password !== undefined}
                helperText={errors?.password?.message}
                InputProps={{
                    endAdornment: (
                        <InputAdornment position="end">
                            <IconButton
                                aria-label={t("aria.passwordVisibilityToggle")}
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
            <FormControlLabel
                control={<Checkbox value="remember" color="primary" />}
                label={t("rememberMe")}
            />
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
                <PrimaryButton
                    type="submit"
                    fullWidth
                    variant="contained"
                    className={classes.submit}
                    disabled={isLoading}
                >
                    {t("signIn")}
                </PrimaryButton>
                {isLoading && (
                    <CircularProgress
                        size={24}
                        className={classes.buttonProgress}
                    />
                )}
            </div>
            <Grid container>
                <Grid item xs>
                    <Link href="#" variant="body2">
                        {t("passwordRecoveryLink")}
                    </Link>
                </Grid>
                <Grid item>
                    <Link variant="body2" component={RouterLink} to="/signup">
                        {t("signUpLink")}
                    </Link>
                </Grid>
            </Grid>
        </form>
    );
};

export default SignInForm;
