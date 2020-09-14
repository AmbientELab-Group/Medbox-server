import React, { useState } from "react";
import { makeStyles } from "@material-ui/core/styles";
import Grid from "@material-ui/core/Grid";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import Checkbox from "@material-ui/core/Checkbox";
import Link from "@material-ui/core/Link";
import CircularProgress from "@material-ui/core/CircularProgress";
import IconButton from "@material-ui/core/IconButton";
import InputAdornment from "@material-ui/core/InputAdornment";
import Visibility from "@material-ui/icons/Visibility";
import VisibilityOff from "@material-ui/icons/VisibilityOff";
import Typography from "@material-ui/core/Typography";
import { Link as RouterLink } from "react-router-dom";


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
        textAlign: "center"
    },
    successMessage: {
        color: theme.palette.success.main,
        textAlign: "center"
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

const SignInForm = ({onSubmit, authStateHooks, formStateHooks}) => {
    const { submitSuccess, submitError, isLoading } = authStateHooks;
    const { register, handleSubmit, errors } = formStateHooks;
    const classes = useStyles();
    const [ isPasswordHidden, setPasswordHidden ] = useState(true);

    const validationSchemas = {
        email: {
          required: "Email is required.",
          maxLength: {
            value: 128,
            message: "Email can not be over 128 letters long."
          },
          pattern: {
            value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i,
            message: "Please enter a valid email address"
          }
        },
        password: {
          required: "Password is required.",
          minLength: {
            value: 8,
            message: "Password can not be shorter than 8 letters."
          },
          maxLength: {
            value: 128,
            message: "Password can not be over 128 letters long."
          }
        }
      };

    return (
        <form className={classes.form} onSubmit={handleSubmit(onSubmit)}>
            <TextField
                variant="outlined"
                margin="normal"
                required
                fullWidth
                id="email"
                label="Email Address"
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
                label="Password"
                type={isPasswordHidden ? "password" : "text"}
                id="password"
                autoComplete="current-password"
                inputRef={register(validationSchemas.password)}
                error={errors.password !== undefined}
                helperText={errors?.password?.message}
                InputProps={{ endAdornment: (
                    <InputAdornment position="end">
                        <IconButton
                            aria-label="toggle password visibility"
                            onClick={() => setPasswordHidden(!isPasswordHidden)}
                            onMouseDown={e => e.preventDefault()}
                        >
                        {isPasswordHidden ? <VisibilityOff/> : <Visibility/>}
                        </IconButton>
                    </InputAdornment>
                    )
                }}
            />
            <FormControlLabel
                control={<Checkbox value="remember" color="primary"/>}
                label="Remember me"
            />
            { submitError && 
                <Typography className={classes.submitErrorMessage}>
                    {submitError}
                </Typography>
            }
            { submitSuccess && 
                <Typography className={classes.successMessage}>
                    {submitSuccess}
                </Typography>
            }
            <div className={classes.wrapper}>
                <Button
                    type="submit"
                    fullWidth
                    variant="contained"
                    color="primary"
                    className={classes.submit}
                    disabled={isLoading}
                >
                    Sign In
                </Button>
                { isLoading && 
                    <CircularProgress size={24} className={classes.buttonProgress}/>
                }
            </div>
            <Grid container>
              <Grid item xs>
                <Link href="#" variant="body2">
                      Forgot password?
                </Link>
              </Grid>
                <Grid item>
                    <Link variant="body2" component={RouterLink} to="/signup">
                        Don't have an account? Sign Up
                    </Link>
                </Grid>
            </Grid> 
        </form>
    );
};

export default SignInForm;
