import React from "react";
import Grid from "@material-ui/core/Grid";
import DeviceCard from "../components/DeviceCard";

const boxes = [
    {
        id: 1,
        name: "Box123456789qwertyuiop",
        state: "on",
        owner: "Bob",
        fill: 20
    },
    {   
        id: 2,
        name: "Box2",
        state: "off",
        owner: "Jack",
        fill: 50
    },
    {
        id: 3,
        name: "Box3",
        state: "connecting",
        owner: "Karen",
        fill: 80
    },
    {
        id: 4,
        name: "Box4",
        state: "on",
        owner: "Randall",
        fill: 35
    },
    {
        id: 5,
        name: "Box5",
        state: "off",
        owner: "Felix",
        fill: 73
    }
];

const DevicesView = () => (
    <Grid container spacing={3}>
        { boxes.map(box => (
            <Grid key={box.id} item xs={12}>
                <DeviceCard device={box}/>
            </Grid>
        )) }
    </Grid>
);

export default DevicesView;
