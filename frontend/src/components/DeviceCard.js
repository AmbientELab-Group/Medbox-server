import React from "react";
import { useHistory } from "react-router-dom";
import { makeStyles, withStyles, useTheme } from "@material-ui/core/styles";
import Button from "@material-ui/core/Button";
import useMediaQuery from "@material-ui/core/useMediaQuery";
import Card from "@material-ui/core/Card";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent"; 
import Typography from "@material-ui/core/Typography";
import LinearProgress from "@material-ui/core/LinearProgress";
import ConnectionState from "./ConnectionState";

const FillBar = withStyles((theme) => ({
    root: {
        height: 10,
        borderRadius: 5,
      },
      colorPrimary: {
        backgroundColor: theme.palette.grey[theme.palette.type === 'light' ? 200 : 700],
      },
      bar: {
        borderRadius: 5,
      },
}))(LinearProgress);

const useStyles = makeStyles((theme) => ({
    content: {
        display: "flex",
        flexDirection: "column"
    },
    actions: {
        display: "flex",
        justifyContent: "flex-end"
    },
    barFull: {
        backgroundColor: theme.palette.primary.light
    },
    barMedium: {
        backgroundColor: theme.palette.primary.main
    },
    barLow: {
        backgroundColor: theme.palette.primary.dark
    },
    fill: {
        marginTop: theme.spacing(3)
    }
}));


const DeviceCard = ({ device }) => {
    const classes = useStyles();
    const history = useHistory();
    const theme = useTheme();
    const sm = useMediaQuery(theme.breakpoints.up("sm"));

    return (
        <Card>
            <CardContent className={classes.content}>
                <ConnectionState state={device.state}/>
                <Typography variant="h3" noWrap>
                    {device.name}
                </Typography>
                <Typography variant="body2" color="textSecondary">
                    Owner: {device.owner}
                </Typography>
                <Typography className={classes.fill}>
                    Device fill: {device.fill}%
                </Typography>
                <FillBar
                    variant="determinate" 
                    value={device.fill}
                    classes={{
                        bar: device.fill > 70 ? 
                            classes.barFull :
                            device.fill > 30 ?
                            classes.barMedium :
                            classes.barLow
                    }}/>
            </CardContent>
            <CardActions className={classes.actions}>
                <Button size={sm ? "large" : "small"} color="primary" onClick={()=>history.push(`/dashboard/devices/${device.id}`)}>
                    Show more
                </Button>
                <Button size={sm ? "large" : "small"} color="primary" onClick={()=>history.push(`/dashboard/devices/${device.id}`)}>
                    Edit
                </Button>
                <Button size={sm ? "large" : "small"} color="primary">
                    Delete
                </Button>
            </CardActions>
        </Card>
    );
};

export default DeviceCard;
