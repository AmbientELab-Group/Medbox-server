import React from "react";
import { useRouteMatch } from "react-router-dom";
import { makeStyles, useTheme, withStyles } from "@material-ui/core/styles";
import Zoom from "@material-ui/core/Zoom";
import Fab from "@material-ui/core/Fab";
import Tooltip from "@material-ui/core/Tooltip";
import AddIcon from "@material-ui/icons/Add";
import EditIcon from '@material-ui/icons/Edit';


const StyledTooltip = withStyles((theme) => ({
    tooltip: {
        [theme.breakpoints.down("sm")]: {
            fontSize: "0.7rem",
        },
        padding: theme.spacing(1)
    }
}))(Tooltip);

const useStyles = makeStyles((theme) => ({
    fab: {
        position: "fixed",
        right: "5vw",
        bottom: "5vh"
    },
}));

const CustomFab = () => {
    const classes = useStyles();
    const theme = useTheme();
    const matchDevices = useRouteMatch({exact: true, path: "/dashboard/devices"});
    const matchTreatments = useRouteMatch({exact: true, path: "/dashboard/treatments"});
    const matchSingleDevice = useRouteMatch("/dashboard/devices/:id");
    const matchSingleTreatment = useRouteMatch("/dashboard/treatments/:id");

    const transitionDuration = {
        enter: theme.transitions.duration.enteringScreen,
        exit: theme.transitions.duration.leavingScreen,
    };

    const descriptions = [
        {
            match: matchDevices,
            title: "Add device",
            icon: <AddIcon/>
        },
        {
            match: matchTreatments,
            title: "Add treatment",
            icon: <AddIcon/>
        },
        {
            match: matchSingleDevice,
            title: "Modify device",
            icon: <EditIcon/>
        },
        {
            match: matchSingleTreatment,
            title: "Modify treatment",
            icon: <EditIcon/>
        }
    ];

    return (
        <>
        { descriptions.map((desc) => (
            <Zoom 
                in={!!desc.match} 
                key={desc.title} 
                timeout={transitionDuration} 
                style={{
                    transitionDelay: `${!!desc.match ? transitionDuration.exit : 0}ms`,
                }}
                unmountOnExit
            >
                <StyledTooltip title={desc.title} aria-label={desc.title} placement="left" onClick={()=>console.log("tooltip")}>
                    <Fab className={classes.fab} color="secondary">
                        {desc.icon}
                    </Fab>
                </StyledTooltip>
            </Zoom>
        ))}
        </>
    );
}

export default CustomFab;
