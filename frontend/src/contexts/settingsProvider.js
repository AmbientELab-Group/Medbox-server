import React, { createContext, useState, useContext } from "react";

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
        isAuto: true,
        isZoneAuto: false,
        time: Date.now,
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

    return (
        <SettingsContext.Provider value={[options, setOptions]}>
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