import React, { useState } from "react";
import clsx from "clsx";
import { makeStyles } from "@material-ui/core/styles";
import Paper from "@material-ui/core/Paper";
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import Button from "@material-ui/core/Button"
import Toolbar from "@material-ui/core/Toolbar";
import settingTabs from "../components/settingsTabs";
import { Grid } from "@material-ui/core";
import { useSettings } from "../contexts/settingsProvider";


const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
        display: "flex",
        minHeight: "80vh"
    },
    tabs: {
        borderRight: `1px solid ${theme.palette.divider}`
    },
    tab: {
        padding: theme.spacing(2),
    },
    tabWrapper: {
        alignItems: "flex-start"
    },
    activeTab: {
        color: theme.palette.primary.main
    },
    panel: {
        flex: "auto",
        display: "flex",
        flexDirection: "column",
        justifyContent: "space-between",
        padding: theme.spacing(3),
    },
    buttons: {
        justifyContent: "flex-end"
    }
 }));

const a11yProps = (index) => {
    return {
        id: `vertical-tab-${index}`,
        'aria-controls': `vertical-tabpanel-${index}`,
    };
}


const SettingsView = () => {
    const classes = useStyles();
    const [tab, setTab] = useState(0);
    const [options] = useSettings();

    const handleChange = (event, newTab) => {
        setTab(newTab);
    };

    console.log(options);

    return (
        <Paper className={classes.root}>
            <Tabs
                orientation="vertical"
                variant="scrollable"
                value={tab}
                onChange={handleChange}
                aria-label="Setting tabs"
                className={classes.tabs}
            >
                { settingTabs.map((option, index) => (
                    <Tab 
                        key={option.name} 
                        label={option.name} 
                        {...a11yProps(index)} 
                        className={clsx(classes.tab, tab === index && classes.activeTab)}
                        classes={{wrapper: classes.tabWrapper}}
                    />
                ))}
            </Tabs>
            <div className={classes.panel}>
                <Grid container>
                    <Grid item sm={1} md={2}/>
                    <Grid item sm={10} md={8}>
                        { settingTabs[tab].component }
                    </Grid>
                    <Grid item sm={1} md={2}/>
                </Grid>
                <Toolbar className={classes.buttons}>
                    <Button color="primary">
                        Save
                    </Button>
                    <Button color="primary">
                        Discard changes
                    </Button>
                </Toolbar>
            </div>
        </Paper>
    );
}

export default SettingsView;
