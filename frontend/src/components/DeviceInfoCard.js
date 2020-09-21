import { Card, makeStyles } from "@material-ui/core";
import CardContent from "@material-ui/core/CardContent";
import Typography from "@material-ui/core/Typography";
import React from "react";


const useStyles = makeStyles((theme) => ({

}));

const DeviceInfoCard = ({device}) => {
    const classes = useStyles();

    return (
        <Card>
            <CardContent className={classes.content}>
                <Typography variant="h5" noWrap>
                    {device.name}
                </Typography>
                <Typography variant="body2" color="textSecondary">
                    Owner: {device.owner}
                </Typography>
            </CardContent>
        </Card>
    );
};

export default DeviceInfoCard;