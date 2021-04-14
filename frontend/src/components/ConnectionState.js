import React, { useState } from "react";
import { makeStyles } from "@material-ui/core/styles";
import StateIcon from "@material-ui/icons/FiberManualRecord";
import Typography from "@material-ui/core/Typography";
import { Tooltip } from "@material-ui/core";
import { useTranslation } from "react-i18next";

const useStyles = makeStyles((theme) => ({
    statusIndicator: {
        display: "flex",
        alignSelf: "flex-end",
        alignItems: "center",
    },
    onIcon: {
        color: theme.palette.success.main,
        marginLeft: 2,
    },
    offIcon: {
        color: theme.palette.error.main,
        marginLeft: 2,
    },
}));

const getElapsedTime = (lastSeen) => {
    const elapsedSeconds = Math.floor((Date.now() - lastSeen) / 1000);

    if (elapsedSeconds <= 0) {
        return "now";
    }

    const elapsedMinutes = Math.floor(elapsedSeconds / 60);

    if (elapsedMinutes === 0) {
        return `${elapsedSeconds} seconds ago`;
    }

    const elapsedHours = Math.floor(elapsedMinutes / 60);

    if (elapsedHours === 0) {
        return `${elapsedMinutes} minutes ago`;
    }

    const elapsedDays = Math.floor(elapsedHours / 24);

    if (elapsedDays === 0) {
        return `${elapsedHours} hours ago`;
    }

    return `${elapsedDays} days ago`;
};

const ConnectionState = ({ state }) => {
    const classes = useStyles();
    const [lastSeen, setLastSeen] = useState(getElapsedTime(state.lastSeen));
    const [open, setOpen] = useState(false);
    const { t } = useTranslation("device");

    const handleClose = () => {
        setOpen(false);
    };

    const handleOpen = () => {
        setLastSeen(getElapsedTime(state.lastSeen));
        setOpen(true);
    };

    return (
        <Tooltip
            title={`Last seen: ${lastSeen}`}
            aria-label="status"
            open={open}
            onClose={handleClose}
            onOpen={handleOpen}
        >
            <div className={classes.statusIndicator}>
                <Typography color="textSecondary">
                    {state.isOn ? t("Connected") : t("Disconnected")}
                </Typography>
                <StateIcon
                    className={state.isOn ? classes.onIcon : classes.offIcon}
                />
            </div>
        </Tooltip>
    );
};

export default ConnectionState;
