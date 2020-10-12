import React, { useState } from "react";
import { makeStyles, useTheme } from "@material-ui/core/styles"
import ExpandLess from '@material-ui/icons/ExpandLess';
import ExpandMore from '@material-ui/icons/ExpandMore';
import Grid from "@material-ui/core/Grid";
import Paper from "@material-ui/core/Paper";
import Typography from "@material-ui/core/Typography";
import IconButton from "@material-ui/core/IconButton"
import Avatar from "@material-ui/core/Avatar";
import Collapse from "@material-ui/core/Collapse";
import Button from "@material-ui/core/Button";
import Divider from "@material-ui/core/Divider";
import { useMediaQuery } from "@material-ui/core";

const useStyles = makeStyles((theme) => ({
    cell: {
        alignItems: "center",
        justifyItems: "center",
        textAlign: "center",
        paddingTop: theme.spacing(1),
        paddingBottom: theme.spacing(1),
    },
    avatar: {
        margin: "auto"
    },
    cardOpened: {
        borderBottomRightRadius: 0,
        borderBottomLeftRadius: 0
    },
    collapsePaper: {
        backgroundColor: theme.palette.grey[100],
        borderTopRightRadius: 0,
        borderTopLeftRadius: 0
    },
    divider: {
        color: theme.palette.primary.main,
        borderTop: "1px solid",
        marginBottom: theme.spacing(2)
    },
    buttons: {
        display: "flex",
        justifyContent: "flex-end",
        padding: theme.spacing(1),
        paddingTop: theme.spacing(2)
    }
}));

const TreatmentCard = ({ treatment }) => {
    const classes = useStyles();
    const [cardExpanded, setCardExpanded] = useState(false);
    const theme = useTheme();
    const upSm = useMediaQuery(theme.breakpoints.up("sm"));

    const closeCard = () => {
        setCardExpanded(false);
    };

    const openCard = () => {
        setCardExpanded(true);
    }

    return (
        <>
            <Paper className={cardExpanded ? classes.cardOpened : ""}>
                <Grid container className={classes.cell}>
                    <Grid item xs={2}>
                        <Avatar className={classes.avatar}>{treatment.name[0]}</Avatar>
                    </Grid>
                    <Grid item xs={3}>
                        <Typography variant="body1">
                            {treatment.name}
                        </Typography>
                    </Grid>
                    <Grid item xs={3}>
                        <Typography variant="body1">
                            {treatment.device}
                        </Typography>
                    </Grid>
                    <Grid item xs={2} sm={3}>
                        <Typography variant="body1">
                            {treatment.count}
                        </Typography>
                    </Grid>
                    <Grid item xs={2} sm={1}>
                        {cardExpanded ?
                            <IconButton onClick={closeCard}>
                                <ExpandLess />
                            </IconButton>
                            :
                            <IconButton onClick={openCard}>
                                <ExpandMore />
                            </IconButton>
                        }
                    </Grid>
                </Grid>
            </Paper>
            <Collapse in={cardExpanded} timeout="auto" unmountOnExit className={classes.collapse}>
                <Paper className={classes.collapsePaper}>
                    <Grid container className={classes.cell}>
                        <Grid item xs={false} sm={2}/>
                        <Grid item xs={4} sm={3}>
                            <Typography variant={upSm ? "h4" : "subtitle2"} gutterBottom>
                                Medicine
                        </Typography>
                        </Grid>
                        <Grid item xs={4} sm={3}>
                            <Typography variant={upSm ? "h4" : "subtitle2"} gutterBottom noWrap>
                                Day time
                        </Typography>
                        </Grid>
                        <Grid item xs={4} sm={3}>
                            <Typography variant={upSm ? "h4" : "subtitle2"} gutterBottom noWrap>
                                Arrangement
                        </Typography>
                        </Grid>
                        <Grid item xs={false} sm={1}/>
                    </Grid>
                    <Divider variant="middle" className={classes.divider} />
                    {treatment.medicines.map(medicine => (
                        <Grid key={medicine.id} container className={classes.cell}>
                            <Grid item xs={false} sm={2}/>
                            <Grid item xs={4} sm={3}>
                                <Typography variant={upSm ? "body2" : "caption"}>
                                    {medicine.name}
                                </Typography>
                            </Grid>
                            <Grid item xs={4} sm={3}>
                                <Typography variant={upSm ? "body2" : "caption"}>
                                    {medicine.predefTimes.join(", ")}
                                </Typography>
                            </Grid>
                            <Grid item xs={4} sm={3}>
                                <Typography variant={upSm ? "body2" : "caption"}>
                                    {medicine.arrangement}
                                </Typography>
                            </Grid>
                            <Grid item xs={false} sm={1}/>
                        </Grid>
                    ))}
                    <Grid item xs={12} className={classes.buttons}>
                        <Button color="primary" size="large">
                            Show More
                    </Button>
                        <Button color="primary" size="large">
                            Edit
                    </Button>
                        <Button color="primary" size="large">
                            Delete
                    </Button>
                    </Grid>
                </Paper>
            </Collapse>
        </>
    );
};

export default TreatmentCard;