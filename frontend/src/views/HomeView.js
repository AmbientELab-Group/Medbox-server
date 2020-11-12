import React from "react";
import { makeStyles } from '@material-ui/core/styles';
import { Link } from "react-router-dom";

import {
    AppBar, 
    Toolbar,
    Container,
    Typography,
    Button
} from "@material-ui/core";

const useStyles = makeStyles(() => ({
    title: {
      flexGrow: 1,
    },
}));

const HomeView = props => {
    const classes = useStyles();

    return (
        <>
        <AppBar>
            <Toolbar>
                <Typography className={classes.title} variant="h3">
                    Medbox
                </Typography>
                <Button 
                    color="inherit" 
                    component={Link}
                    to="/signin"
                >
                    Sign in
                </Button>
                <Button 
                    color="inherit" 
                    component={Link}
                    to="/signup"
                >
                    Sing up
                </Button>
            </Toolbar>
        </AppBar>
        <Toolbar />
        <Container>
            <h1>
                Home page
            </h1>
        </Container>
        </>
    )
};

export default HomeView;