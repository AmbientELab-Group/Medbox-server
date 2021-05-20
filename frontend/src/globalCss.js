import { createMuiTheme } from "@material-ui/core";
import "@fontsource/montserrat/300.css";
import "@fontsource/montserrat/400.css";
import "@fontsource/montserrat/500.css";
import "@fontsource/montserrat/600.css";
import "@fontsource/montserrat/700.css";
import "@fontsource/montserrat/800.css";

const CustomTheme = createMuiTheme({
    palette: {
        primary: {
            light: "#93F0F7",
            main: "#34C5D0",
            dark: "#10c8d5",
            gradient: "linear-gradient(180deg, #93F0F7 0%, #34C3CD 100%)",
        },
        secondary: {
            light: "#C6E0F8",
            main: "#3586D0",
        },
        background: {
            paper: "#FDFDFD",
            transparentPaper: "rgba(255, 255, 255, 0.6)",
            transparentPaperGradient:
                "linear-gradient(180deg, rgba(255, 255, 255, 0.6) 0%, rgba(255, 255, 255, 0.2) 100%)",
            default: "#FDFDFD",
            // glass: "linear-gradient(180deg, rgba(255, 255, 255, 0.6) 0%, rgba(255, 255, 255, 0.2) 100%)",
        },
    },
    typography: {
        fontFamily: ["Montserrat"],
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
    spacing: (factor) => `${8 * factor}px`,
    overrides: {
        MuiBackdrop: {
            root: {
                backgroundColor: "rgba(255, 255, 255, 0.5)",
            },
        },
    },
});

export default CustomTheme;
