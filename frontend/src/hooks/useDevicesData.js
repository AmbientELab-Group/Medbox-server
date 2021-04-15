import React, { useEffect, useState } from "react";
import { authFetch } from "../contexts/authProvider";

const boxes = [
    {
        id: "1",
        name: "Box123456789qwertyuiop",
        state: {
            isOn: true,
            lastSeen: Date.now(),
        },
        owner: "Bob",
        fill: 20,
        medicines: [
            {
                name: "Medicine X",
                doseAmount: 12,
            },
            {
                name: "Medicine Y",
                doseAmount: 4,
            },
            {
                name: "Medicine Z",
                doseAmount: 25,
            },
        ],
        containers: [
            {
                id: 1,
            },
            {
                id: 2,
            },
            {
                id: 3,
            },
        ],
    },
    {
        id: "2",
        name: "Box2",
        state: {
            isOn: false,
            lastSeen: Date.now(),
        },
        owner: "Jack",
        fill: 50,
        medicines: [
            {
                name: "Medicine X",
                doseAmount: 12,
            },
            {
                name: "Medicine Y",
                doseAmount: 4,
            },
            {
                name: "Medicine Z",
                doseAmount: 25,
            },
        ],
        containers: [
            {
                id: 1,
            },
            {
                id: 2,
            },
            {
                id: 3,
            },
        ],
    },
    {
        id: "3",
        name: "Box3",
        state: {
            isOn: false,
            lastSeen: Date.now(),
        },
        owner: "Karen",
        fill: 80,
        medicines: [
            {
                name: "Medicine X",
                doseAmount: 12,
            },
            {
                name: "Medicine Y",
                doseAmount: 4,
            },
            {
                name: "Medicine Z",
                doseAmount: 25,
            },
        ],
        containers: [
            {
                id: 1,
            },
            {
                id: 2,
            },
            {
                id: 3,
            },
        ],
    },
];

const fetchDevices = async (setDevices) => {
    const req = await (await authFetch()).get("/devices");
    setDevices(req.data);
};

const useDeviceData = () => {
    const [devices, setDevices] = useState();

    useEffect(() => {
        fetchDevices(setDevices);
    }, []);

    return [devices, setDevices];
};

export default useDeviceData;
