import React, { lazy, Suspense } from "react";
import {
    Switch,
    Route,
    BrowserRouter as Router,
    Redirect,
} from "react-router-dom";
import { makeStyles } from "@material-ui/core/styles";
import CircularProgress from "@material-ui/core/CircularProgress";
import SignInView from "./views/SignInView";
import SignUpView from "./views/SignUpView";
import ProtectedRoute from "./components/ProtectedRoute";

const ProtectedLayout = lazy(async () => {
    const [moduleExports] = await Promise.all([
        import("./views/ProtectedLayout"),
        new Promise((resolve) => setTimeout(resolve, 500)),
    ]);
    return moduleExports;
});

const useStyles = makeStyles((theme) => ({
    suspenseWrapper: {
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        height: "100vh",
    },
}));

const App = () => {
    const classes = useStyles();
    return (
        <Router>
            <Suspense
                fallback={
                    <div className={classes.suspenseWrapper}>
                        <CircularProgress
                            variant="indeterminate"
                            size={80}
                            thickness={4}
                        />
                    </div>
                }
            >
                <Switch>
                    <Route exact path="/">
                        <Redirect to="/dashboard" />
                    </Route>
                    <ProtectedRoute path="/dashboard" redirectPath="/signin">
                        <ProtectedLayout />
                    </ProtectedRoute>
                    <Route path="/signin" component={SignInView} />
                    <Route path="/signup" component={SignUpView} />
                    <Route path="*">
                        <Redirect to="/" />
                    </Route>
                </Switch>
            </Suspense>
        </Router>
    );
};

export default App;
