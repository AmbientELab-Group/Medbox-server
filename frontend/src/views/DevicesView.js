import React from "react";
import Container from "@material-ui/core/Container";
import Grid from "@material-ui/core/Grid";
import DeviceCard from "../components/DeviceCard";
import { makeStyles } from "@material-ui/core/styles";

const boxes = [
    {
        id: 1,
        name: "Box123456789qwertyuiop",
        state: "on",
        owner: "Bob",
        fill: 20
    },
    {   
        id: 2,
        name: "Box2",
        state: "off",
        owner: "Jack",
        fill: 50
    },
    {
        id: 3,
        name: "Box3",
        state: "connecting",
        owner: "Karen",
        fill: 80
    }
];

const useStyles = makeStyles((theme) => ({
    container: {
        paddingTop: theme.spacing(4),
        paddingBottom: theme.spacing(4),
    },
    paper: {
        padding: theme.spacing(2),
        display: "flex",
        overflow: "auto",
        flexDirection: "column",
    },
    fixedHeight: {
        height: 240,
    },
}));

const DevicesView = () => {
    const classes = useStyles();

    return (
        <Container maxWidth="lg" className={classes.container}>
            <Grid container spacing={3}>
                { boxes.map(box => (
                    <Grid key={box.id} item xs={12}>
                        <DeviceCard device={box}/>
                    </Grid>
                )) }
            </Grid>
        </Container>
    );
};

export default DevicesView;
