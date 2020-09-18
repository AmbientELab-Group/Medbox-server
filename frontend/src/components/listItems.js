import React from 'react';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import ListSubheader from '@material-ui/core/ListSubheader';
import DashboardIcon from '@material-ui/icons/Dashboard';
import AssignmentIcon from '@material-ui/icons/Assignment';
import AllInboxIcon from '@material-ui/icons/AllInbox';
import LocalHospitalIcon from '@material-ui/icons/LocalHospital';
import SettingsIcon from '@material-ui/icons/Settings';
import { Link as RouterLink } from "react-router-dom";

export const mainListItems = (
    <>
    <ListItem button component={RouterLink} to="/dashboard">
        <ListItemIcon>
            <DashboardIcon />
        </ListItemIcon>
        <ListItemText primary="Dashboard" />
    </ListItem>
    <ListItem button component={RouterLink} to="/dashboard/devices">
        <ListItemIcon>
            <AllInboxIcon />
        </ListItemIcon>
        <ListItemText primary="Devices" />
    </ListItem>
    <ListItem button component={RouterLink} to="/dashboard/treatments">
        <ListItemIcon>
            <LocalHospitalIcon />
        </ListItemIcon>
        <ListItemText primary="Treatments" />
    </ListItem>
    <ListItem button component={RouterLink} to="/dashboard/settings">
        <ListItemIcon>
            <SettingsIcon />
        </ListItemIcon>
        <ListItemText primary="Settings" />
    </ListItem>
    </>
);

export const secondaryListItems = (
    <div>
        <ListSubheader inset>Saved reports</ListSubheader>
        <ListItem button>
            <ListItemIcon>
                <AssignmentIcon />
            </ListItemIcon>
            <ListItemText primary="Current month" />
        </ListItem>
        <ListItem button>
            <ListItemIcon>
                <AssignmentIcon />
            </ListItemIcon>
            <ListItemText primary="Last quarter" />
        </ListItem>
        <ListItem button>
            <ListItemIcon>
                <AssignmentIcon />
            </ListItemIcon>
            <ListItemText primary="Year-end sale" />
        </ListItem>
    </div>
);