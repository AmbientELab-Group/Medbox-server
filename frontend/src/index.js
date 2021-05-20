import * as serviceWorker from "./serviceWorker";
import React, { Suspense } from "react";
import ReactDOM from "react-dom";
import {
    ThemeProvider as MuiThemeProvider,
    StylesProvider,
} from "@material-ui/core/styles";
import { ThemeProvider as StyledComponentsThemeProvider } from "styled-components";
import CssBaseline from "@material-ui/core/CssBaseline";
import App from "./App";
import CustomTheme from "./globalCss";
import "./i18n";

ReactDOM.render(
    <React.StrictMode>
        <MuiThemeProvider theme={CustomTheme}>
            <StyledComponentsThemeProvider theme={CustomTheme}>
                <StylesProvider injectFirst>
                    <CssBaseline />
                    <Suspense fallback={<h1>...Loading</h1>}>
                        <App />
                    </Suspense>
                </StylesProvider>
            </StyledComponentsThemeProvider>
        </MuiThemeProvider>
    </React.StrictMode>,
    document.getElementById("root")
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
