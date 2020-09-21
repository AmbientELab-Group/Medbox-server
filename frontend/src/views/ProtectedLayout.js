import React, { useEffect } from "react";
import { makeStyles } from "@material-ui/core/styles";
import Box from "@material-ui/core/Box";
import Container from "@material-ui/core/Container";
import Copyright from "../components/Copyright"
import { Redirect, Route, Switch, useRouteMatch } from "react-router-dom";
import DashboardView from "./DashboardView";
import { checkAuth } from "../contexts/authProvider";
import CustomAppBar from "../components/CustomAppBar";
import CustomDrawer from "../components/CustomDrawer";
import DevicesView from "./DevicesView";
import SingleDeviceView from "./SingleDeviceView";


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
    },
}));

const ProtectedLayout = () => {
    const classes = useStyles();
    const routeMatch = useRouteMatch();
    const [openDrawer, setDrawerOpen] = React.useState(true);

    useEffect(() => {
        checkAuth();
    }, []);


    return (
        <div className={classes.root}>
            <CustomAppBar drawerHook={{openDrawer, setDrawerOpen}}/>
            <CustomDrawer drawerHook={{openDrawer, setDrawerOpen}}/>
            <main className={classes.content}>
                <div className={classes.appBarSpacer} />
                <Container maxWidth="lg" className={classes.container}>
                    <Switch>
                        <Route exact path={`${routeMatch.path}`}>
                           <DashboardView/>
                        </Route>
                        <Route exact path={`${routeMatch.path}/devices`}>
                            <DevicesView/>
                        </Route>
                        <Route path={`${routeMatch.path}/devices/:id`}>
                            <SingleDeviceView/>
                        </Route>
                        <Route path={`${routeMatch.path}/treatments`}>
                            <h1>Tretments</h1>
                        </Route>
                        <Route path={`${routeMatch.path}/settings`}>
                            <h1>Settings</h1>
                        </Route>
                        <Route path={`${routeMatch.path}/*`}>
                            <Redirect to={`${routeMatch.url}`}/>
                        </Route>
                    </Switch>
                    <Box pt={4}>
                        <Copyright />
                    </Box>
                </Container>
            </main>
        </div>
    );
}

export default ProtectedLayout;