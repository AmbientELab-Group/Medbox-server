import React from "react";
import clsx from "clsx";
import { Checkbox, FormControlLabel, makeStyles, Select, Switch, TextField, Typography} from "@material-ui/core";
import { useSettings } from "../contexts/settingsProvider";

const useStyles = makeStyles((theme) => ({
    root: {
        display: "flex",
        flexDirection: "column",
    },
    sectionHeader: {
        padding: theme.spacing(2)
    },
    section: {
        display: "flex",
        flexDirection: "column",
        padding: `0px  ${theme.spacing(4)}px`
    },
    field: {
        margin: theme.spacing(2),
    },
    checkboxField: {
        justifyContent: "space-between"
    }
}));

const Profile = () => {
    const classes = useStyles();
    const [options, setOptions] = useSettings();
    const { Profile } = options;

    const handleChange = (event) => {
        setOptions({
            ...options,
            Profile: {
                ...Profile,
                [event.target.id]: event.target.value
            }    
        });
    };

    return (
        <div className={classes.root}>
            <Typography variant="h3" color="primary" className={classes.sectionHeader}>Profile details</Typography>
            <div className={classes.section}>
                <TextField id="email" label="Email" defaultValue={Profile.email} disabled className={classes.field} variant="outlined"/>
                <TextField id="name" label="Name" value={Profile.name} onChange={handleChange} className={classes.field} variant="outlined"/>
                <TextField id="surname" label="Surname" value={Profile.surname} onChange={handleChange} className={classes.field} variant="outlined"/>
            </div>
            <Typography variant="h3" color="primary" className={classes.sectionHeader}>Change password</Typography>
            <div className={classes.section}>
                <TextField id="password-old" label="Current password" type="password" className={classes.field} variant="outlined"/>
                <TextField id="password-new" label="New password" type="password" className={classes.field} variant="outlined"/>
                <TextField id="password-new-confirm" label="Confirm new password" type="password" className={classes.field} variant="outlined"/>
            </div>
        </div>
    );
}

const Devices = () => {
    const classes = useStyles();

    return (
        <div className={classes.root}>
            Devices
        </div>
    );
}

const Notifications = () => {
    const classes = useStyles();
    const [options, setOptions] = useSettings();
    const { Notifications } = options;
    
    const handleOnToggle = () => {
        setOptions({
            ...options,
            Notifications: {
                ...options.Notifications,
                isOn: !options.Notifications.isOn
            }
        });
    };

    const handleReplenishToggle = () => {
        setOptions({
            ...options,
            Notifications: {
                ...options.Notifications,
                notificationTypes: {
                    ...options.Notifications.notificationTypes,
                    replenish: !options.Notifications.notificationTypes.replenish
                }
            }
        });
    };

    const handleAdministrationToggle = () => {
        setOptions({
            ...options,
            Notifications: {
                ...options.Notifications,
                notificationTypes: {
                    ...options.Notifications.notificationTypes,
                    administration: !options.Notifications.notificationTypes.administration
                }
            }
        });
    };


    return (
        <div className={classes.root}>
            <Typography variant="h3" color="primary" className={classes.sectionHeader}>Notifications</Typography>
            <div className={classes.section}>
                <FormControlLabel
                    control={
                        <Switch 
                            color="primary"
                            checked={Notifications.isOn}
                            onChange={handleOnToggle}
                       />
                    }
                    label="Turn off notifications"
                    labelPlacement="start"
                    className={clsx(classes.field, classes.checkboxField)}
                />
            </div>
            <Typography variant="h3" color="primary" className={classes.sectionHeader}>Type of notifications</Typography>
            <div className={classes.section}>
                <FormControlLabel
                    control={<Checkbox color="primary"/>}
                    label="Medicines refill warning"
                    labelPlacement="start"
                    checked={Notifications.notificationTypes.replenish}
                    onChange={handleReplenishToggle}
                    className={clsx(classes.field, classes.checkboxField)}
                />
                <FormControlLabel
                    control={<Checkbox color="primary"/>}
                    label="Medicine administration time"
                    labelPlacement="start"
                    checked={Notifications.notificationTypes.administration}
                    onChange={handleAdministrationToggle}
                    className={clsx(classes.field, classes.checkboxField)}
                />
            </div>
        </div>
    );
}

const Time = () => {
    const classes = useStyles();
    const [options, setOptions] = useSettings();
    const { Time } = options;

    const handleZoneAutoToggle = () => {
        setOptions({
            ...options,
            Time: {
                ...options.Time,
                isZoneAuto: !options.Time.isZoneAuto
            }
        });
    };

    const handleChange = (event) => {
        setOptions({
            ...options,
            Time: {
                ...options.Time,
                timeZone: JSON.parse(event.target.value)
            }
        });
    };


    return (
        <div className={classes.root}>
            <Typography variant="h3" color="primary" className={classes.sectionHeader}>Time</Typography>
            <div className={classes.section}>
                <FormControlLabel
                    control={
                        <Switch 
                            color="primary"
                            checked={Time.isZoneAuto}
                            onChange={handleZoneAutoToggle}
                       />
                    }
                    label="Set time zone automatically"
                    labelPlacement="start"
                    className={clsx(classes.field, classes.checkboxField)}
                />
            </div>
            <Typography variant="h3" color="primary" className={classes.sectionHeader}>Change time zone</Typography>
            <div className={classes.section}>
                <Select native value={JSON.stringify(Time.timeZone)} onChange={handleChange} className={classes.field} disabled={Time.isZoneAuto}>
                    { Time.timeZones.map((zone, idx) => (
                        <option key={idx} value={JSON.stringify(zone)}>{zone.rawFormat}</option>
                    ))}
                </Select>
            </div>
        </div>
    );
}

const Dashboard = () => {
    const classes = useStyles();

    return (
        <div className={classes.root}>
            Dashboard
        </div>
    );
}

const Language = () => {
    const classes = useStyles();
    const [options, setOptions] = useSettings();
    const { Language } = options;

    const handleChange = (event) => {
        setOptions({
            ...options,
            Language: {
                ...Language,
                chosen: event.target.value
            }
        });
    };

    return (
        <div className={classes.root}>
            <Typography variant="h3" color="primary" className={classes.sectionHeader}>Language choice</Typography>
            <div className={classes.section}>
                <Select native value={Language.chosen} onChange={handleChange} className={classes.field}>
                    {Language.options.map((lang)=>(
                        <option key={lang} value={lang}>{lang}</option>
                    ))}
                </Select>
            </div>
        </div>
    );
}

const Help = () => {
    const classes = useStyles();

    return (
        <div className={classes.root}>
            Help
        </div>
    );
}

const settingTabs = [
    {
        name: "Profile",
        component: <Profile/>
    },
    {
        name: "Devices",
        component: <Devices/>
    },
    {
        name: "Notifications",
        component: <Notifications/>
    },
    {
        name: "Time",
        component: <Time/>
    },
    {
        name: "Dashboard",
        component: <Dashboard/>
    },
    {
        name: "Language",
        component: <Language/>
    },
    {
        name: "Help",
        component: <Help/>
    }
];

export default settingTabs;
