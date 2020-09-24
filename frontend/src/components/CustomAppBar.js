import React from "react";
import clsx from "clsx";
import { makeStyles, useTheme } from "@material-ui/core/styles";
import { useMediaQuery } from '@material-ui/core';
import AppBar from "@material-ui/core/AppBar";
import Typography from "@material-ui/core/Typography";
import Badge from "@material-ui/core/Badge";
import IconButton from "@material-ui/core/IconButton";
import Toolbar from "@material-ui/core/Toolbar";
import MenuIcon from "@material-ui/icons/Menu";
import MeetingRoomIcon from "@material-ui/icons/MeetingRoom";
import NotificationsIcon from "@material-ui/icons/Notifications";
import { logout } from "../contexts/authProvider";
import { useLocation } from "react-router-dom";


const useStyles = makeStyles((theme) => ({
    toolbar: {
        paddingRight: 24, // keep right padding when drawer closed
    },
    appBar: {
        color: "white",
        zIndex: theme.zIndex.drawer + 1,
        transition: theme.transitions.create(["width", "margin"], {
            easing: theme.transitions.easing.sharp,
            duration: theme.transitions.duration.leavingScreen,
        }),
    },
    appBarShift: {
        marginLeft: theme.drawerWidth,
        width: `calc(100% - ${theme.drawerWidth}px)`,
        transition: theme.transitions.create(["width", "margin"], {
            easing: theme.transitions.easing.sharp,
            duration: theme.transitions.duration.enteringScreen,
        }),
    },
    menuButton: {
        [theme.breakpoints.up("sm")]: {
            marginRight: 36,
        }
    },
    menuButtonHidden: {
        display: "none",
    },
    title: {
        flexGrow: 1,
        textTransform: "capitalize"
    },
    logoutIcon: {
        paddingRight: 0
    }
}));

const CustomAppBar = ({ drawerHook, ...rest }) => {
    const classes = useStyles();
    const { openDrawer, setDrawerOpen } = drawerHook;
    const location = useLocation();
    const theme = useTheme();
    const upSm = useMediaQuery(theme.breakpoints.up("sm"));

    const handleDrawerOpen = () => {
        setDrawerOpen(true);
    };

    const handleLogout = () => {
        logout();
    };

    const getTitle = () => {
        const tokens = location.pathname.split("/");
        const title = tokens[2] || tokens[1];
        return title;
    };

    return (
        <AppBar position="absolute" className={clsx(classes.appBar, openDrawer && upSm && classes.appBarShift)}>
            <Toolbar className={classes.toolbar}>
                <IconButton
                    edge="start"
                    color="inherit"
                    aria-label="open drawer"
                    onClick={handleDrawerOpen}
                    className={clsx(classes.menuButton, openDrawer && classes.menuButtonHidden)}
                >
                    <MenuIcon />
                </IconButton>
                <Typography component="h1" variant="h3" color="inherit" noWrap className={classes.title}>
                    {getTitle()}
                </Typography>
                <IconButton color="inherit">
                    <Badge badgeContent={4} color="secondary">
                        <NotificationsIcon />
                    </Badge>
                </IconButton>
                <IconButton color="inherit" onClick={handleLogout} aria-label="log out" >
                    <MeetingRoomIcon className={classes.logoutIcon} />
                </IconButton>
            </Toolbar>
        </AppBar>
    )
}

export default CustomAppBar
