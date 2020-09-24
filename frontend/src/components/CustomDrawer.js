import React from "react";
import clsx from "clsx";
import { makeStyles, useTheme } from "@material-ui/core/styles";
import useMediaQuery from "@material-ui/core/useMediaQuery";
import Drawer from "@material-ui/core/Drawer";
import Divider from "@material-ui/core/Divider";
import IconButton from "@material-ui/core/IconButton";
import ChevronLeftIcon from "@material-ui/icons/ChevronLeft";
import MainDrawerList from "./MainDrawerList";
import logo from "../assets/img/Logo_medBox@2x.png";


const useStyles = makeStyles((theme) => ({
    toolbarIcon: {
        display: "flex",
        alignItems: "center",
        justifyContent: "flex-end",
        padding: "0 8px",
        ...theme.mixins.toolbar,
    },
    drawerPaper: {
        position: "relative",
        whiteSpace: "nowrap",
        width: theme.drawerWidth,
        transition: theme.transitions.create("width", {
            easing: theme.transitions.easing.sharp,
            duration: theme.transitions.duration.enteringScreen,
        }),
    },
    drawerPaperClose: {
        overflowX: "hidden",
        transition: theme.transitions.create("width", {
            easing: theme.transitions.easing.sharp,
            duration: theme.transitions.duration.leavingScreen,
        }),
        width: theme.spacing(7),
        [theme.breakpoints.up("sm")]: {
            width: theme.spacing(9),
        },
    },
}));

const CustomDrawer = ({drawerHook, ...rest}) => {
    const classes = useStyles();
    const theme = useTheme();
    const upMd = useMediaQuery(theme.breakpoints.up("md"));
    const { openDrawer, setDrawerOpen } = drawerHook;

    const handleDrawerClose = () => {
        setDrawerOpen(false);
    };
    
    return (
        <Drawer
            variant={upMd ? "permanent" : "temporary"}
            classes={{
                paper: clsx(classes.drawerPaper, !openDrawer && classes.drawerPaperClose),
            }}
            open={openDrawer}
            onClose={handleDrawerClose}
        >
            <div className={classes.toolbarIcon}>
                <img src={logo} width={170} alt="Logo"/>
                <IconButton onClick={handleDrawerClose}>
                    <ChevronLeftIcon />
                </IconButton>
            </div>
            <Divider />
            <MainDrawerList/>
        </Drawer>
    )
}

export default CustomDrawer;
