import React, { useState } from "react";
import Avatar from "@material-ui/core/Avatar";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
import Link from "@material-ui/core/Link";
import Grid from "@material-ui/core/Grid";
import Box from "@material-ui/core/Box";
import CircularProgress from "@material-ui/core/CircularProgress";
import IconButton from "@material-ui/core/IconButton";
import InputAdornment from "@material-ui/core/InputAdornment";
import LockOutlinedIcon from "@material-ui/icons/LockOutlined";
import Visibility from "@material-ui/icons/Visibility";
import VisibilityOff from "@material-ui/icons/VisibilityOff";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core/styles";
import Container from "@material-ui/core/Container";
import Copyright from "../components/Copyright";
import { 
  Link as RouterLink,
  Redirect
} from "react-router-dom";
import jwt_decode from "jwt-decode";
import { publicAccountFetch } from "../api/publicFetch";
import { useForm } from "react-hook-form";
import ErrorSnack from "../components/ErrorSnack";
import { useAuth } from "../contexts/AuthContext";


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
  form: {
    width: "100%", // Fix IE 11 issue.
    marginTop: theme.spacing(3),
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

const SignUpView = () => {
  const classes = useStyles();
  const {register, handleSubmit, errors, getValues, setError} = useForm({mode: "onBlur"});
  const [ , setAuthState ] = useAuth();
  const [ submitSuccess, setSubmitSuccess ] = useState();
  const [ submitError, setSubmitError ] = useState();
  const [ isLoading, setLoading ] = useState(false);
  const [ redirectOnLogin, setRedirectOnLogin ] = useState(false);
  const [ connectionError, setConnectionError ] = useState(false);
  const [ isPasswordHidden, setPasswordHidden ] = useState(true);

  const validationSchemas = {
    first_name: {
      required: "First name is required.",
      maxLength: {
        value: 30,
        message: "First name can not be over 30 letters long."
      },
    },
    last_name: {
      required: "Last name is required.",
      maxLength: {
        value: 150,
        message: "Last name can not be over 150 letters long."
      },
    },
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
    },
    password2: {
      required: "Confirmation is required.",
      validate: value => (value === getValues("password") || "Passwords must match.")
    }
  };

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
        setRedirectOnLogin(true);
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
    <>
    {redirectOnLogin && <Redirect to="/dashboard"/>}
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
                label="First Name"
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
                label="Last Name"
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
                label="Email Address"
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
                label="Password"
                type={isPasswordHidden ? "password" : "text"}
                id="password"
                autoComplete="new-password"
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
                      {isPasswordHidden ? <VisibilityOff /> : <Visibility />}
                    </IconButton>
                  </InputAdornment>
                  )
                }}
              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                variant="outlined"
                required
                fullWidth
                name="password2"
                label="Confirm Password"
                type={isPasswordHidden ? "password" : "text"}
                id="password2"
                autoComplete="new-password"
                inputRef={register(validationSchemas.password2)}
                error={errors.password2 !== undefined}
                helperText={errors?.password2?.message}
                InputProps={{ endAdornment: (
                  <InputAdornment position="end">
                    <IconButton
                      aria-label="toggle password visibility"
                      onClick={() => setPasswordHidden(!isPasswordHidden)}
                      onMouseDown={e => e.preventDefault()}
                    >
                      {isPasswordHidden ? <VisibilityOff /> : <Visibility />}
                    </IconButton>
                  </InputAdornment>
                  )
                }}
              />
            </Grid>
          </Grid>
          {submitError && <Typography className={classes.submitErrorMessage}>{submitError}</Typography>}
          {submitSuccess && <Typography className={classes.successMessage}>{submitSuccess}</Typography>}
          <div className={classes.wrapper}>
            <Button
              type="submit"
              fullWidth
              variant="contained"
              color="primary"
              className={classes.submit}
            >
              Sign Up
            </Button>
            {isLoading && <CircularProgress size={24} className={classes.buttonProgress} />}
          </div>
          <Grid container justify="flex-end">
            <Grid item>
              <Link variant="body2" component={RouterLink} to="/signin">
                Already have an account? Sign in
              </Link>
            </Grid>
          </Grid>
        </form>
      </div>
      <Box mt={5}>
        <Copyright />
      </Box>
    </Container>
    </>
  );
}

export default SignUpView;
