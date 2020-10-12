import React, { useEffect } from "react";
import { Redirect, Route, Switch, useRouteMatch } from "react-router-dom";
import { checkAuth } from "../contexts/authProvider";
import { makeStyles } from "@material-ui/core/styles";
import Box from "@material-ui/core/Box";
import Container from "@material-ui/core/Container";
import DashboardView from "./DashboardView";
import DevicesView from "./DevicesView";
import SingleDeviceView from "./SingleDeviceView";
import TreatmentsView from "./TreatmentsView";
import Copyright from "../components/Copyright"
import CustomAppBar from "../components/CustomAppBar";
import CustomDrawer from "../components/CustomDrawer";
import CustomFab from "../components/CustomFab";
import SettingsView from "./SettingsView";
import { SettingsProvider } from "../contexts/settingsProvider";
import useDevicesData from "../hooks/useDevicesData";


const useStyles = makeStyles((theme) => ({
    root: {
        display: "flex",
    },
    appBarSpacer: theme.mixins.toolbar,
    content: {
        flexGrow: 1,
        height: "100vh",
        overflow: "auto",
    },
    container: {
        paddingTop: theme.spacing(4),
        paddingBottom: theme.spacing(4),
        minHeight: "calc(100vh - 140px)",
        position:"relative"
    },
    copyright: {
        padding: theme.spacing(2)
    }
}));

const ProtectedLayout = () => {
    const classes = useStyles();
    const routeMatch = useRouteMatch();
    const [openDrawer, setDrawerOpen] = React.useState(false);
    const devicesHook = useDevicesData();
    

    useEffect(() => {
        checkAuth();
    }, []);


    return (
        <div className={classes.root}>
            <CustomAppBar drawerHook={{openDrawer, setDrawerOpen}}/>
            <CustomDrawer drawerHook={{openDrawer, setDrawerOpen}}/>
            <main className={classes.content}>
                <div className={classes.appBarSpacer}/>
                <Container maxWidth="lg" className={classes.container}>
                    <Switch>
                        <Route exact path={`${routeMatch.path}`}>
                            <DashboardView/>
                        </Route>
                        <Route exact path={`${routeMatch.path}/devices`}>
                            <DevicesView devices={devicesHook}/>
                        </Route>
                        <Route path={`${routeMatch.path}/devices/:id`}>
                            <SingleDeviceView/>
                        </Route>
                        <Route exact path={`${routeMatch.path}/treatments`}>
                            <TreatmentsView/>
                        </Route>
                        <Route path={`${routeMatch.path}/treatments/:id`}>
                            <SingleDeviceView/>
                        </Route>
                        <Route path={`${routeMatch.path}/settings`}>
                            <SettingsProvider>
                                <SettingsView/>
                            </SettingsProvider>
                        </Route>
                        <Route path={`${routeMatch.path}/*`}>
                            <Redirect to={`${routeMatch.url}`}/>
                        </Route>
                    </Switch>
                    <CustomFab/>
                </Container>
                <Box className={classes.copyright}>
                    <Copyright />
                </Box>
            </main>
        </div>
    );
}

export default ProtectedLayout;