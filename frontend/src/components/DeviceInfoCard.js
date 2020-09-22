import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import Typography from "@material-ui/core/Typography";


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