import React, { useState } from 'react';
import List from "@material-ui/core/List";
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import DashboardIcon from '@material-ui/icons/Dashboard';
import AllInboxIcon from '@material-ui/icons/AllInbox';
import LocalHospitalIcon from '@material-ui/icons/LocalHospital';
import ExpandLess from '@material-ui/icons/ExpandLess';
import ExpandMore from '@material-ui/icons/ExpandMore';
import SettingsIcon from '@material-ui/icons/Settings';
import StateIcon from '@material-ui/icons/FiberManualRecord';
import MoreHorizIcon from '@material-ui/icons/MoreHoriz';
import LoopIcon from '@material-ui/icons/Loop';
import { Link as RouterLink } from "react-router-dom";
import { Collapse, IconButton, ListItemSecondaryAction, makeStyles } from '@material-ui/core';

const boxes = [
    {
        id: 1,
        name: "Box123456789qwertyuiop",
        state: "on"
    },
    {   
        id: 2,
        name: "Box2",
        state: "off"
    },
    {
        id: 3,
        name: "Box3",
        state: "connecting"
    }
];

const treatments = [
    {
        id: 1,
        name: "Bob"
    },
    {
        id: 2,
        name: "John"
    },
    {
        id: 3,
        name: "Marry"
    }
];

const useStyles = makeStyles((theme) => ({
    nested: {
        paddingLeft: theme.spacing(4),
    },
    drawerIcon: {
        display: "flex",
        alignItems: "inherit",
        justifyContent: "inherit",
        paddingTop: 12
    },
    secondaryAction: {
        display: "flex"
    },
    collapsedText: {
        maxWidth: 120,
        paddingRight: 12
    },
    onIcon: {
        color: theme.palette.success.main
    },
    offIcon: {
        color: theme.palette.error.main
    }
}));

const MainDrawerList = () => {
    const classes = useStyles();
    const [devicesExpanded, setDevicesExpanded] = useState(false);
    const [treatmentsExpanded, setTreatmentsExpanded] = useState(false);

    const getStateIcon = ({state}) => {
        switch (state) {
            case "on":
                return <StateIcon className={classes.onIcon}/>;
            case "off":
                return <StateIcon className={classes.offIcon}/>;
            case "connecting":
                return <LoopIcon/>;
            default:
                return <StateIcon className={classes.offIcon}/>;
        }
    };

    const openDevices = (e) => {
        e.preventDefault();
        e.stopPropagation();

        if (treatmentsExpanded) {
            setTreatmentsExpanded(false);
        }

        setDevicesExpanded(true);
    };

    const openTreatments = (e) => {
        e.preventDefault();
        e.stopPropagation();

        if (devicesExpanded) {
            setDevicesExpanded(false);
        }

        setTreatmentsExpanded(true);
    };

    const closeDevices = (e) => {
        e.preventDefault();
        e.stopPropagation();
        setDevicesExpanded(false);
    };

    const closeTreatments = (e) => {
        e.preventDefault();
        e.stopPropagation();
        setTreatmentsExpanded(false);
    };

    return (
        <List component="nav">
            <ListItem button component={RouterLink} to="/dashboard">
                <ListItemIcon >
                    <DashboardIcon />
                </ListItemIcon>
                <ListItemText primary="Dashboard" />
            </ListItem>
            <ListItem button component={RouterLink} to="/dashboard/devices">
                <ListItemIcon>
                    <AllInboxIcon />
                </ListItemIcon>
                <ListItemText primary="Devices" />
                { devicesExpanded ? 
                    <IconButton onClick={closeDevices}>
                        <ExpandLess/>
                    </IconButton>
                    : 
                    <IconButton onClick={openDevices}>
                        <ExpandMore/>
                    </IconButton>
                }
            </ListItem>
            <Collapse in={devicesExpanded} timeout="auto" unmountOnExit>
                <List component="div" disablePadding>
                    { boxes.slice(0, 6).map((box) => (
                        <ListItem key={box.id} button className={classes.nested}>
                            <ListItemText 
                                primary={box.name} 
                                primaryTypographyProps={{noWrap: true}} 
                                className={classes.collapsedText}
                            />
                            <ListItemSecondaryAction className={classes.secondaryAction}>
                                <span className={classes.drawerIcon}>
                                    { getStateIcon(box) }
                                </span>
                                <IconButton>
                                    <MoreHorizIcon/>
                                </IconButton>
                            </ListItemSecondaryAction>
                        </ListItem>
                    ))}
                </List>
            </Collapse>
            <ListItem button component={RouterLink} to="/dashboard/treatments">
                <ListItemIcon>
                    <LocalHospitalIcon />
                </ListItemIcon>
                <ListItemText primary="Treatments" />
                { treatmentsExpanded ? 
                    <IconButton onClick={closeTreatments}>
                        <ExpandLess/>
                    </IconButton>
                    : 
                    <IconButton onClick={openTreatments}>
                        <ExpandMore/>
                    </IconButton>
                }
            </ListItem>
            <Collapse in={treatmentsExpanded} timeout="auto" unmountOnExit>
                <List component="div" disablePadding>
                    { treatments.slice(0, 6).map((treatment) => (
                        <ListItem key={treatment.id} button className={classes.nested}>
                            <ListItemText 
                                primary={treatment.name} 
                                primaryTypographyProps={{noWrap: true}} 
                                className={classes.collapsedText}
                            />
                            <ListItemSecondaryAction className={classes.secondaryAction}>
                                <IconButton>
                                    <MoreHorizIcon/>
                                </IconButton>
                            </ListItemSecondaryAction>
                        </ListItem>
                    ))}
                </List>
            </Collapse>
            <ListItem button component={RouterLink} to="/dashboard/settings">
                <ListItemIcon>
                    <SettingsIcon />
                </ListItemIcon>
                <ListItemText primary="Settings" />
            </ListItem>
        </List>
    );
}

export default MainDrawerList;
