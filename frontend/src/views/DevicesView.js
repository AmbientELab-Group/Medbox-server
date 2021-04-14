import React from "react";
import Grid from "@material-ui/core/Grid";
import DeviceCard from "../components/DeviceCard";

const boxes = [
    {
        id: "1",
        name: "Dozownik Janiny",
        state: {
            isOn: true,
            lastSeen: Date.now(),
        },
        owner: "Janina",
        fill: 20,
        medicines: [
            {
                name: "Allosol",
                doseAmount: 12,
            },
            {
                name: "Sensistar",
                doseAmount: 4,
            },
            {
                name: "Invalin",
                doseAmount: 25,
            },
        ],
        containers: [
            {
                id: 0,
                position: 0,
                capacity: 8,
                chambers: [],
            },
            {
                id: 1,
                position: 1,
                capacity: 16,
            },
            {
                id: 2,
                position: 2,
            },
        ],
    },
    {
        id: "2",
        name: "Dozownik Henryka",
        state: {
            isOn: false,
            lastSeen: Date.now(),
        },
        owner: "Henryk",
        fill: 50,
        medicines: [
            {
                name: "Allosol",
                doseAmount: 12,
            },
            {
                name: "Sensistar",
                doseAmount: 4,
            },
            {
                name: "Invalin",
                doseAmount: 25,
            },
        ],
        containers: [
            {
                id: 0,
                position: 0,
            },
        ],
    },
    {
        id: "3",
        name: "Dozownik Stefanii",
        state: {
            isOn: false,
            lastSeen: Date.now(),
        },
        owner: "Stefania",
        fill: 80,
        medicines: [
            {
                name: "Allosol",
                doseAmount: 12,
            },
            {
                name: "Sensistar",
                doseAmount: 4,
            },
            {
                name: "Invalin",
                doseAmount: 25,
            },
        ],
        containers: [],
    },
];

const DevicesView = ({ devices }) => (
    <Grid container spacing={3}>
        {console.log(devices[0])}
        {boxes.map((box) => (
            <Grid key={box.id} item xs={12}>
                <DeviceCard device={box} />
            </Grid>
        ))}
    </Grid>
);

export default DevicesView;
