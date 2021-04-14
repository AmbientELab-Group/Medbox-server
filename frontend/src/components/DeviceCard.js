import React from "react";
import { useHistory } from "react-router-dom";
import { makeStyles, withStyles, useTheme } from "@material-ui/core/styles";
import useMediaQuery from "@material-ui/core/useMediaQuery";
import Card from "@material-ui/core/Card";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import Typography from "@material-ui/core/Typography";
import LinearProgress from "@material-ui/core/LinearProgress";
import ConnectionState from "./ConnectionState";
import { useTranslation } from "react-i18next";

import FatTextButton from "./FatTextButton";

const FillBar = withStyles((theme) => ({
    root: {
        height: 10,
        borderRadius: 5,
    },
    colorPrimary: {
        backgroundColor:
            theme.palette.grey[theme.palette.type === "light" ? 200 : 700],
    },
    bar: {
        borderRadius: 5,
    },
}))(LinearProgress);

const useStyles = makeStyles((theme) => ({
    content: {
        display: "flex",
        flexDirection: "column",
    },
    actions: {
        display: "flex",
        justifyContent: "flex-end",
    },
    barFull: {
        backgroundColor: theme.palette.primary.light,
    },
    barMedium: {
        backgroundColor: theme.palette.primary.main,
    },
    barLow: {
        backgroundColor: theme.palette.primary.dark,
    },
    fill: {
        marginTop: theme.spacing(3),
    },
}));

const DeviceCard = ({ device }) => {
    const classes = useStyles();
    const history = useHistory();
    const theme = useTheme();
    const sm = useMediaQuery(theme.breakpoints.up("sm"));
    const { t } = useTranslation(["device", "buttons"]);

    return (
        <Card>
            <CardContent className={classes.content}>
                <ConnectionState state={device.state} />
                <Typography variant="h3" noWrap>
                    {device.name}
                </Typography>
                <Typography variant="body2" color="textSecondary">
                    {t("device:Owner")}: {device.owner}
                </Typography>
                <Typography className={classes.fill}>
                    {t("device:Device fill")}: {device.fill}%
                </Typography>
                <FillBar
                    variant="determinate"
                    value={device.fill}
                    classes={{
                        bar:
                            device.fill > 70
                                ? classes.barFull
                                : device.fill > 30
                                ? classes.barMedium
                                : classes.barLow,
                    }}
                />
            </CardContent>
            <CardActions className={classes.actions}>
                <FatTextButton
                    size={sm ? "large" : "small"}
                    onClick={() =>
                        history.push(`/dashboard/devices/${device.id}`)
                    }
                >
                    {t("buttons:Show more")}
                </FatTextButton>
                <FatTextButton
                    size={sm ? "large" : "small"}
                    onClick={() =>
                        history.push(`/dashboard/devices/${device.id}`)
                    }
                >
                    {t("buttons:Edit")}
                </FatTextButton>
                <FatTextButton size={sm ? "large" : "small"}>
                    {t("buttons:Delete")}
                </FatTextButton>
            </CardActions>
        </Card>
    );
};

export default DeviceCard;
