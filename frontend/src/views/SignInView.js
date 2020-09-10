import React, { useState } from "react";
import Avatar from "@material-ui/core/Avatar";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import Checkbox from "@material-ui/core/Checkbox";
import Link from "@material-ui/core/Link";
import Paper from "@material-ui/core/Paper";
import Box from "@material-ui/core/Box";
import Grid from "@material-ui/core/Grid";
import CircularProgress from "@material-ui/core/CircularProgress";
import IconButton from "@material-ui/core/IconButton";
import InputAdornment from "@material-ui/core/InputAdornment";
import LockOutlinedIcon from "@material-ui/icons/LockOutlined";
import Visibility from "@material-ui/icons/Visibility";
import VisibilityOff from "@material-ui/icons/VisibilityOff";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core/styles";
import {
  Link as RouterLink,
  Redirect
} from "react-router-dom";
import { useForm } from "react-hook-form";
import jwt_decode from "jwt-decode";
import Copyright from "../components/Copyright";
import { publicAccountFetch } from "../api/publicFetch";
import ErrorSnack from "../components/ErrorSnack";

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
  form: {
    width: "100%", // Fix IE 11 issue.
    marginTop: theme.spacing(1),
  },
  submit: {
    margin: theme.spacing(1, 0, 2),
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
    margin: theme.spacing(1),
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



const SignInView = () => {
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

  const classes = useStyles();
  const {register, handleSubmit, errors} = useForm({mode: "onBlur"});
  const [ submitSuccess, setSubmitSuccess ] = useState();
  const [ submitError, setSubmitError ] = useState();
  const [ isLoading, setLoading ] = useState(false);
  const [ redirectOnLogin, setRedirectOnLogin ] = useState(false);
  const [ connectionError, setConnectionError ] = useState(false);
  const [ isPasswordHidden, setPasswordHidden ] = useState(true);

  const onSubmit = async credentials => {
    try {
      setLoading(true);
      const { data } = await publicAccountFetch.post(
        "/signin",
        credentials
      );

      setSubmitSuccess("Authentication successful!");
      setSubmitError("");
      
      console.log(data);
      console.log(jwt_decode(data.access));
      console.log(jwt_decode(data.refresh));

      setTimeout(() => {
        setRedirectOnLogin(true);
      }, 1000);
    } catch (error) {
      setLoading(false);
      if (error.response) {
        const { data } = error.response;
        console.error(data.detail);
        setSubmitError(data.detail);
        setSubmitSuccess("");
        // if (data.errorList) {
        //     data.errorList.forEach((error) => {
        //         setError(error.field, "manual", error.message);
        //     }); 
        // }
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
      {redirectOnLogin && <Redirect to="/dashboard" />}
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
                    {isPasswordHidden ? <VisibilityOff /> : <Visibility />}
                  </IconButton>
                </InputAdornment>
                )
            }}
            />
            <FormControlLabel
              control={<Checkbox value="remember" color="primary" />}
              label="Remember me"
            />
            {submitError && <Typography className={classes.submitErrorMessage}>{submitError}</Typography>}
            {submitSuccess && <Typography className={classes.successMessage}>{submitSuccess}</Typography>}
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
              {isLoading && <CircularProgress size={24} className={classes.buttonProgress} />}
            </div>
            <Grid container>
              <Grid item xs>
                <Link href="#" variant="body2">
                  Forgot password?
                </Link>
              </Grid>
              <Grid item>
                <Link variant="body2" component={RouterLink} to="/signup">
                  {"Don't have an account? Sign Up"}
                </Link>
              </Grid>
            </Grid>
            <Box mt={5}>
              <Copyright />
            </Box>
          </form>
        </div>
      </Grid>
    </Grid>
  );
}

export default SignInView;