import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import Typography from "@material-ui/core/Typography";
import ConnectionState from "./ConnectionState";
import { Divider, Grid } from "@material-ui/core";
import { useTranslation } from "react-i18next";

const useStyles = makeStyles((theme) => ({
    content: {
        display: "flex",
        flexDirection: "column",
        padding: theme.spacing(3),
    },
    divider: {
        color: theme.palette.primary.main,
        borderTop: "1px solid",
        marginTop: theme.spacing(2),
    },
    medicine: {
        textAlign: "center",
    },
    medicineLabels: {
        padding: `${theme.spacing(2)}px 0px`,
    },
    oddMedicineEntry: {
        backgroundColor: theme.palette.grey[100],
    },
    evenMedicineEntry: {},
}));

const DeviceInfoCard = ({ device }) => {
    const classes = useStyles();
    const { t } = useTranslation("device");

    return (
        <Card>
            <CardContent className={classes.content}>
                <ConnectionState state={device.state} />
                <Typography variant="h2" noWrap>
                    {device.name}
                </Typography>
                <Typography variant="body2" color="textSecondary">
                    {t("Owner")}: {device.owner}
                </Typography>
                <Divider className={classes.divider} />
                <Grid container className={classes.medicine}>
                    <Grid
                        container
                        item
                        xs={12}
                        className={classes.medicineLabels}
                    >
                        <Grid item xs={6}>
                            <Typography variant="h3" color="textSecondary">
                                {t("Medicine name")}
                            </Typography>
                        </Grid>
                        <Grid item xs={6}>
                            <Typography variant="h3" color="textSecondary">
                                {t("Number of doses")}
                            </Typography>
                        </Grid>
                    </Grid>
                    {device.medicines.map((medicine, idx) => (
                        <Grid
                            container
                            item
                            xs={12}
                            className={
                                idx % 2
                                    ? classes.oddMedicineEntry
                                    : classes.evenMedicineEntry
                            }
                            key={medicine.name}
                        >
                            <Grid item xs={6}>
                                <Typography>{medicine.name}</Typography>
                            </Grid>
                            <Grid item xs={6}>
                                <Typography>{medicine.doseAmount}</Typography>
                            </Grid>
                        </Grid>
                    ))}
                </Grid>
            </CardContent>
        </Card>
    );
};

export default DeviceInfoCard;
