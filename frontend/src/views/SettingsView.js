import React, { useState } from "react";
import clsx from "clsx";
import { makeStyles } from "@material-ui/core/styles";
import Paper from "@material-ui/core/Paper";
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import { Button, Toolbar } from "@material-ui/core";


const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
        display: "flex",
        minHeight: "80vh"
    },
    tabs: {
        borderRight: `1px solid ${theme.palette.divider}`,
    },
    tab: {
        padding: theme.spacing(2)
    },
    activeTab: {
        color: theme.palette.primary.main
    },
    panel: {
        flex: "auto",
        display: "flex",
        flexDirection: "column",
        justifyContent: "space-between",
        padding: theme.spacing(3)
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

const tabs = [
    {
        name: "Profile",
    },
    {
        name: "Devices"
    },
    {
        name: "Notifications"
    },
    {
        name: "Time"
    },
    {
        name: "Dashboard"
    },
    {
        name: "Language"
    },
    {
        name: "Help"
    }
]


const SettingsView = () => {
    const classes = useStyles();
    const [tab, setTab] = useState(0);

    const handleChange = (event, newTab) => {
        setTab(newTab);
    };

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
                { tabs.map((option, index) => (
                    <Tab 
                        key={option.name} 
                        label={option.name} 
                        {...a11yProps(index)} 
                        className={clsx(classes.tab, tab === index && classes.activeTab)}
                    />
                ))}
            </Tabs>
            <div className={classes.panel}>
                <div>
                    Settings
                </div>
                <Toolbar className={classes.buttons}>
                    <Button color="primary">
                        Save
                    </Button>
                    <Button color="primary">
                        Discard changes
                    </Button>
                </Toolbar>
            </div>
            {/* <TabPanel value={value} index={0}>
                Item One
            </TabPanel>
            <TabPanel value={value} index={1}>
                Item Two
            </TabPanel>
            <TabPanel value={value} index={2}>
                Item Three
            </TabPanel>
            <TabPanel value={value} index={3}>
                Item Four
            </TabPanel>
            <TabPanel value={value} index={4}>
                Item Five
            </TabPanel>
            <TabPanel value={value} index={5}>
                Item Six
            </TabPanel>
            <TabPanel value={value} index={6}>
                Item Seven
            </TabPanel> */}
        </Paper>
    );
}

export default SettingsView;
