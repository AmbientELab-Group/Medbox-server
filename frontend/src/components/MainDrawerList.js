import React, { useState } from "react";
import { Link as RouterLink, useRouteMatch } from "react-router-dom";
import DashboardIcon from "@material-ui/icons/Dashboard";
import AllInboxIcon from "@material-ui/icons/AllInbox";
import ExpandLess from "@material-ui/icons/ExpandLess";
import SettingsIcon from "@material-ui/icons/Settings";
import ExpandMore from "@material-ui/icons/ExpandMore";
import LocalHospitalIcon from "@material-ui/icons/LocalHospital";
import StateIcon from "@material-ui/icons/FiberManualRecord";
import LoopIcon from "@material-ui/icons/Loop";
import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import ListItemIcon from "@material-ui/core/ListItemIcon";
import ListItemText from "@material-ui/core/ListItemText";
import { makeStyles } from "@material-ui/core/styles";
import Collapse from "@material-ui/core/Collapse"; 
import IconButton from "@material-ui/core/IconButton";
import ListItemSecondaryAction from "@material-ui/core/ListItemSecondaryAction";
import ContextMenu from "./ContextMenu";
import { useTranslation } from "react-i18next";

import CropDinIcon from '@material-ui/icons/CropDin';

const boxes = [
    {
        id: "1",
        name: "Dozownik Janiny",
        state: "on"
    },
    {   
        id: "2",
        name: "Dozownik Henryka",
        state: "off"
    },
    {
        id: "3",
        name: "Dozownik Stefanii",
        state: "connecting"
    }
];

const treatments = [
    {
        id: "1",
        name: "Janina"
    },
    {
        id: "2",
        name: "Henryk"
    },
    {
        id: "3",
        name: "Stefania"
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

const MainDrawerList = ({drawerState}) => {
    const classes = useStyles();
    const [devicesExpanded, setDevicesExpanded] = useState(false);
    const [treatmentsExpanded, setTreatmentsExpanded] = useState(false);
    const matchDashboard = useRouteMatch({
        path: "/dashboard",
        exact: true
    });
    const matchDevices = useRouteMatch("/dashboard/devices");
    const matchTreatments = useRouteMatch("/dashboard/treatments");
    const matchSettings = useRouteMatch("/dashboard/settings");
    const { t } = useTranslation("translation");

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
                    <DashboardIcon color={!!matchDashboard ? "primary" : "inherit"}/>
                </ListItemIcon>
                <ListItemText primary={t("Dashboard")} />
            </ListItem>
            <ListItem button component={RouterLink} to="/dashboard/devices">
                <ListItemIcon>
                    <CropDinIcon color={!!matchDevices ? "primary" : "inherit"}/>
                </ListItemIcon>
                <ListItemText primary={t("Devices")} />
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
            <Collapse in={drawerState && devicesExpanded} timeout="auto" unmountOnExit>
                <List component="div" disablePadding>
                    { boxes.slice(0, 6).map((box) => (
                        <ListItem 
                            key={box.id} 
                            button 
                            className={classes.nested}
                            component={RouterLink} 
                            to={`/dashboard/devices/${box.id}`}
                        >
                            <ListItemText 
                                primary={box.name} 
                                primaryTypographyProps={{noWrap: true}} 
                                className={classes.collapsedText}
                            />
                            <ListItemSecondaryAction className={classes.secondaryAction}>
                                <span className={classes.drawerIcon}>
                                    { getStateIcon(box) }
                                </span>
                                <ContextMenu editUrl={`/dashboard/devices/${box.id}/edit`}/>
                            </ListItemSecondaryAction>
                        </ListItem>
                    ))}
                </List>
            </Collapse>
            <ListItem button component={RouterLink} to="/dashboard/treatments">
                <ListItemIcon>
                    <LocalHospitalIcon color={!!matchTreatments ? "primary" : "inherit"}/>
                </ListItemIcon>
                <ListItemText primary={t("Treatments")} />
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
            <Collapse in={drawerState && treatmentsExpanded} timeout="auto" unmountOnExit>
                <List component="div" disablePadding>
                    { treatments.slice(0, 6).map((treatment) => (
                        <ListItem 
                            key={treatment.id} 
                            button 
                            className={classes.nested}
                            component={RouterLink} 
                            to={`/dashboard/treatments/${treatment.id}`}
                        >
                            <ListItemText 
                                primary={treatment.name} 
                                primaryTypographyProps={{noWrap: true}} 
                                className={classes.collapsedText}
                            />
                            <ListItemSecondaryAction className={classes.secondaryAction}>
                                <ContextMenu editUrl={`/dashboard/treatments/${treatment.id}/edit`}/>
                            </ListItemSecondaryAction>
                        </ListItem>
                    ))}
                </List>
            </Collapse>
            <ListItem button component={RouterLink} to="/dashboard/settings">
                <ListItemIcon>
                    <SettingsIcon color={!!matchSettings ? "primary" : "inherit"}/>
                </ListItemIcon>
                <ListItemText primary={t("Settings")} />
            </ListItem>
        </List>
    );
}

export default MainDrawerList;
