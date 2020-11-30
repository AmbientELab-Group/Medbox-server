import React from "react";
import Button from "@material-ui/core/Button";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles(theme => ({
    button: {
        color: theme.palette.primary.dark,
        fontWeight: 600
    }
}));

const FatTextButton = ({children, ...props}) => {
    const classes = useStyles();

    return (
        <Button className={classes.button} {...props}>
            {children}
        </Button>
    )
};

export default FatTextButton;