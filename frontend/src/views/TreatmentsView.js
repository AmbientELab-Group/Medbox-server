import React from "react";
import { makeStyles, useTheme } from "@material-ui/core/styles";
import useMediaQuery from "@material-ui/core/useMediaQuery";
import Paper from "@material-ui/core/Paper";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import TreatmentCard from "../components/TreatmentCard";

const treatments = [
    {
        id: "1",
        name: "Bob",
        device: "Box1",
        count: "2",
        medicines: [
            {
                id: "sdawd",
                name: "Medicine X",
                predefTimes: [
                    "Morning",
                    "Evening"
                ],
                arrangement: "Container 1"
            },
            {
                id: "vflr",
                name: "Medicine Y",
                predefTimes: [
                    "Afternoon"
                ],
                arrangement: "Container 2"
            },
            {
                id: "ssadwr",
                name: "Medicine Z",
                predefTimes: [
                    "Morning",
                    "Evening"
                ],
                arrangement: "Container 3"
            },
        ]
    },
    {
        id: "2",
        name: "John",
        device: "Box2",
        count: "1",
        medicines: [
            {
                id: "sdawd",
                name: "Medicine X",
                predefTimes: [
                    "Morning",
                    "Evening"
                ],
                arrangement: "Container 1"
            },
            {
                id: "vflr",
                name: "Medicine Y",
                predefTimes: [
                    "Afternoon"
                ],
                arrangement: "Container 2"
            },
            {
                id: "ssadwr",
                name: "Medicine Z",
                predefTimes: [
                    "Morning",
                    "Evening"
                ],
                arrangement: "Container 3"
            },
        ]
    },
    {
        id: "3",
        name: "Marry",
        device: "Box3",
        count: "5",
        medicines: [
            {
                id: "sdawd",
                name: "Medicine X",
                predefTimes: [
                    "Morning",
                    "Evening"
                ],
                arrangement: "Container 1"
            },
            {
                id: "vflr",
                name: "Medicine Y",
                predefTimes: [
                    "Afternoon"
                ],
                arrangement: "Container 2"
            },
            {
                id: "ssadwr",
                name: "Medicine Z",
                predefTimes: [
                    "Morning",
                    "Evening"
                ],
                arrangement: "Container 3"
            },
        ]
    }
];

const useStyles = makeStyles((theme) => ({
    container: {
        paddingTop: theme.spacing(4),
        paddingBottom: theme.spacing(4),
    },
    cells: {
        textAlign: "center",
        paddingTop: theme.spacing(2),
        paddingBottom: theme.spacing(2),
    }
}));

const TreatmentView = () => {
    const classes = useStyles();
    const theme = useTheme();
    const upSm = useMediaQuery(theme.breakpoints.up("sm"));
    const upMd = useMediaQuery(theme.breakpoints.up("md"));

    return (
        <Grid container spacing={3}>
            <Grid item xs={12}>
                <Paper>
                    <Grid container className={classes.cells}>
                        <Grid item xs={2}/>
                        <Grid item xs={3}>
                            <Typography variant={upMd ? "h2" : upSm ? "h3" : "h4"} color="primary">
                                Name
                            </Typography>
                        </Grid>
                        <Grid item xs={3}>
                            <Typography variant={upMd ? "h2" : upSm ? "h3" : "h4"} color="primary">
                                Device
                            </Typography>
                        </Grid>
                        <Grid item xs={3}>
                            <Typography variant={upMd ? "h2" : upSm ? "h3" : "h4"} color="primary" >
                                Treatments
                            </Typography>
                        </Grid>
                        <Grid item xs={1}/>
                    </Grid>
                </Paper>
            </Grid>
            { treatments.map(treatment => (
                <Grid key={treatment.id} item xs={12}>
                    <TreatmentCard treatment={treatment}/>
                </Grid>
            )) }
        </Grid>
    );
};

export default TreatmentView;
