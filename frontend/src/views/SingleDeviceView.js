import React from "react";
import { useParams } from "react-router-dom";
import Grid from "@material-ui/core/Grid";
import DeviceInfoCard from "../components/DeviceInfoCard";
import DeviceContainerInfo from "../components/DeviceContainersInfo";

const boxes = [
    {
        id: "1",
        name: "Box123456789qwertyuiop",
        state: {
            isOn: true,
            lastSeen: Date.now()
        },
        owner: "Jan",
        fill: 20,
        medicines: [
            { 
                name: "Allosol",
                doseAmount: 12
            },
            { 
                name: "Sensistar",
                doseAmount: 4
            },
            { 
                name: "Invalin",
                doseAmount: 25
            }
        ],
        containers: [
            {
                id: 0,
                position: 0,
                capacity: 8,
                chambers: [
                    
                ]
            },
            {
                id: 1,
                position: 1,
                capacity: 16
            },
            {
                id: 2,
                position: 2
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
        owner: "Tadeusz",
        fill: 50,
        medicines: [
            { 
                name: "Allosol",
                doseAmount: 12
            },
            { 
                name: "Sensistar",
                doseAmount: 4
            },
            { 
                name: "Invalin",
                doseAmount: 25
            }
        ],
        containers: [
            {
                id: 0,
                position: 0
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
        owner: "Ilona",
        fill: 80,
        medicines: [
            { 
                name: "Allosol",
                doseAmount: 12
            },
            { 
                name: "Sensistar",
                doseAmount: 4
            },
            { 
                name: "Invalin",
                doseAmount: 25
            }
        ],
        containers: [],
    }
];

const SingleDeviceView = () => {
    const { id } = useParams();
    const device = boxes.find((box)=>box.id===id);

    return (
        <Grid container spacing={3}>
            <Grid item xs={12} md={6} lg={6}>
                <DeviceInfoCard device={device}/>
            </Grid>
            <Grid item xs={12} md={6} lg={6}>
                <DeviceContainerInfo device={device}/>
            </Grid>
        </Grid>
    );
};

export default SingleDeviceView;
