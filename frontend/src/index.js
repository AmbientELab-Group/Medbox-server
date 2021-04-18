import React, { Suspense } from "react";
import ReactDOM from "react-dom";
import App from "./App";
import * as serviceWorker from "./serviceWorker";
import CssBaseline from "@material-ui/core/CssBaseline";
import { createMuiTheme, ThemeProvider } from "@material-ui/core";

import "./i18n";

const theme = createMuiTheme({
    palette: {
        // primary: {
        //     light: "#34c5d0",
        //     main: "#358184",
        //     dark: "#1f4a4c"
        // },
        primary: {
            light: "#b7f6fa",
            main: "#2be2f0",
            dark: "#10c8d5",
        },
        background: {
            paper: "#fdfdfd",
            default: "#f0f0f0",
        },
    },
    typography: {
        h1: {
            fontSize: "3rem",
        },
        h2: {
            fontSize: "1.625rem",
        },
        h3: {
            fontSize: "1.2rem",
        },
        h4: {
            fontSize: "1.0625rem",
        },
        h5: {
            fontSize: "0.75rem",
        },
        h6: {
            fontSize: "0.625rem",
        },
    },
    shape: {
        borderRadius: 20,
    },
    drawerWidth: 240,
});

ReactDOM.render(
    <React.StrictMode>
        <ThemeProvider theme={theme}>
            <CssBaseline />
            <Suspense fallback={<h1>...Loading</h1>}>
                <App />
            </Suspense>
        </ThemeProvider>
    </React.StrictMode>,
    document.getElementById("root")
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
