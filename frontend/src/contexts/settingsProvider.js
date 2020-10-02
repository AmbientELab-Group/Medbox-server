import React, { createContext, useState, useContext } from "react";
import { diff } from "deep-object-diff";

import { getTimeZones } from "@vvo/tzdb";
const data = {
    Profile: {
        email: "user@gmail.com",
        name: "Tom",
        surname: "Ross",
    },
    Devices: {
        
    },
    Notifications: {
        isOn: true,
        notificationTypes: {
            replenish: true,
            administration: false
        }
    },
    Time: {
        isZoneAuto: true,
        timeZone: getTimeZones()[173],
        timeZones: getTimeZones()
    },
    Language: {
        options: [
            "Polish",
            "English"
        ],
        chosen: "English"
    }
}


const SettingsContext = createContext();

const SettingsProvider = ({children}) => {
    const [options, setOptions] = useState(data);

    const save = () => {
        const newData = diff(data, options);
        console.log(newData);
    };

    const discard = () => {
        setOptions(data);
    };

    return (
        <SettingsContext.Provider value={[options, setOptions, save, discard]}>
            {children}
        </SettingsContext.Provider>
    );
}

const useSettings = () => {
    const context = useContext(SettingsContext);
    if (context === undefined) {
        throw new Error("useSettings muse be used within a SettingsProvider");
    }

    return context;
}

export {SettingsProvider, useSettings};