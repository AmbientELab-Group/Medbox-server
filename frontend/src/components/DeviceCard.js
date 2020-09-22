import React from "react";
import { useHistory } from "react-router-dom";
import { makeStyles, withStyles, useTheme } from "@material-ui/core/styles";
import StateIcon from "@material-ui/icons/FiberManualRecord";
import LoopIcon from "@material-ui/icons/Loop";
import Button from "@material-ui/core/Button";
import useMediaQuery from "@material-ui/core/useMediaQuery";
import Card from "@material-ui/core/Card";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent"; 
import Typography from "@material-ui/core/Typography";
import LinearProgress from "@material-ui/core/LinearProgress";

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
    statusIndicator: {
        display: "flex",
        alignSelf: "flex-end",
        alignItems: "center",
    },
    content: {
        display: "flex",
        flexDirection: "column"
    },
    actions: {
        display: "flex",
        justifyContent: "flex-end"
    },
    onIcon: {
        color: theme.palette.success.main,
        marginLeft: 2
    },
    offIcon: {
        color: theme.palette.error.main,
        marginLeft: 2
    },
    pairingIcon: {
        color: theme.palette.text.secondary,
        marginLeft: 2
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

    const ConnectionState = ({ state }) => {
        switch (state) {
            case "on":
                return (
                    <>
                        <Typography color="textSecondary">Connected</Typography>
                        <StateIcon className={classes.onIcon} />
                    </>
                );
            case "connecting":
                return (
                    <>
                        <Typography color="textSecondary">Pairing</Typography>
                        <LoopIcon className={classes.pairingIcon}/>
                    </>
                );
            case "off":
            default:
                return (
                    <>
                        <Typography color="textSecondary">Disconnected</Typography>
                        <StateIcon className={classes.offIcon} />
                    </>
                );
        }
    };


    return (
        <Card>
            <CardContent className={classes.content}>
                <div className={classes.statusIndicator}>
                    <ConnectionState state={device.state}/>
                </div>
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
