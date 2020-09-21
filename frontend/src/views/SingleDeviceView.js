import React from "react";
import Container from "@material-ui/core/Container";
import Grid from "@material-ui/core/Grid";
import DeviceInfoCard from "../components/DeviceInfoCard";
import { makeStyles } from "@material-ui/core/styles";
import { useParams } from "react-router-dom";

const boxes = [
    {
        id: "1",
        name: "Box123456789qwertyuiop",
        state: "on",
        owner: "Bob",
        fill: 20
    },
    {   
        id: "2",
        name: "Box2",
        state: "off",
        owner: "Jack",
        fill: 50
    },
    {
        id: "3",
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
}));

const SingleDeviceView = () => {
    const classes = useStyles();
    const { id } = useParams();

    return (
        <Container maxWidth="lg" className={classes.container}>
            <Grid container spacing={3}>
                <Grid item xs={12} md={6} lg={6}>
                    <DeviceInfoCard device={boxes.find((box)=>box.id===id)}/>
                </Grid>
            </Grid>
        </Container>
    );
};

export default SingleDeviceView;
