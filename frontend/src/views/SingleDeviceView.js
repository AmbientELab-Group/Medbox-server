import React from "react";
import { useParams } from "react-router-dom";
import Grid from "@material-ui/core/Grid";
import DeviceInfoCard from "../components/DeviceInfoCard";

const boxes = [
    {
        id: "1",
        name: "Box123456789qwertyuiop",
        state: "on",
        owner: "Bob",
        fill: 20
    },
    {   
        id: "2",
        name: "Box2",
        state: "off",
        owner: "Jack",
        fill: 50
    },
    {
        id: "3",
        name: "Box3",
        state: "connecting",
        owner: "Karen",
        fill: 80
    }
];

const SingleDeviceView = () => {
    const { id } = useParams();

    return (
        <Grid container spacing={3}>
            <Grid item xs={12} md={6} lg={6}>
                <DeviceInfoCard device={boxes.find((box)=>box.id===id)}/>
            </Grid>
        </Grid>
    );
};

export default SingleDeviceView;
