import React from "react";
import Grid from "@material-ui/core/Grid";
import DeviceCard from "../components/DeviceCard";

const boxes = [
    {
        id: "1",
        name: "Box123456789qwertyuiop",
        state: {
            isOn: true,
            lastSeen: Date.now()
        },
        owner: "Bob",
        fill: 20,
        medicines: [
            { 
                name: "Medicine X",
                doseAmount: 12
            },
            { 
                name: "Medicine Y",
                doseAmount: 4
            },
            { 
                name: "Medicine Z",
                doseAmount: 25
            }
        ],
        containers: [
            {
                id: 1
            },
            {
                id: 2
            },
            {
                id: 3
            }
        ],
    },
    {   
        id: "2",
        name: "Box2",
        state: {
            isOn: false,
            lastSeen: Date.now()
        },
        owner: "Jack",
        fill: 50,
        medicines: [
            { 
                name: "Medicine X",
                doseAmount: 12
            },
            { 
                name: "Medicine Y",
                doseAmount: 4
            },
            { 
                name: "Medicine Z",
                doseAmount: 25
            }
        ],
        containers: [
            {
                id: 1
            },
            {
                id: 2
            },
            {
                id: 3
            }
        ],
    },
    {
        id: "3",
        name: "Box3",
        state: {
            isOn: false,
            lastSeen: Date.now()
        },
        owner: "Karen",
        fill: 80,
        medicines: [
            { 
                name: "Medicine X",
                doseAmount: 12
            },
            { 
                name: "Medicine Y",
                doseAmount: 4
            },
            { 
                name: "Medicine Z",
                doseAmount: 25
            }
        ],
        containers: [
            {
                id: 1
            },
            {
                id: 2
            },
            {
                id: 3
            }
        ],
    }
];

const DevicesView = ({devices}) => (
    <Grid container spacing={3}>
        {console.log(devices[0])}
        { boxes.map(box => (
            <Grid key={box.id} item xs={12}>
                <DeviceCard device={box}/>
            </Grid>
        )) }
    </Grid>
);

export default DevicesView;
