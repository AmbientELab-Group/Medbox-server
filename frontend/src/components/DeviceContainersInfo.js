import { Card, CardContent, makeStyles, Select } from "@material-ui/core";
import React, { useState, useEffect } from "react";
import ContainerDiagram from "./ContainerDiagram";
import { useTranslation } from "react-i18next";

const useStyles = makeStyles((theme) => ({
    cardContent: {
        display: "flex",
        flexDirection: "column",
    },
    select: {
        margin: "auto",
    },
}));

const DeviceContainersInfo = ({ device }) => {
    const classes = useStyles();
    const { containers } = device;
    const [selectedContainer, setSelectedContainer] = useState();
    const { t } = useTranslation("device");

    useEffect(() => {
        setSelectedContainer(containers.length > 0 ? containers[0] : null);
    }, [containers]);

    const handleChange = (event) => {
        setSelectedContainer(containers[event.target.value]);
    };

    return (
        <Card>
            <CardContent className={classes.cardContent}>
                <Select
                    native
                    disabled={selectedContainer === null}
                    value={selectedContainer ? selectedContainer.id : ""}
                    onChange={handleChange}
                    variant="outlined"
                >
                    {!selectedContainer && (
                        <option aria-label="None" value="">
                            Device is empty
                        </option>
                    )}
                    {containers.map((cnt) => (
                        <option
                            key={`device-${device.id}/container-${cnt.id}`}
                            value={cnt.id}
                        >
                            {t("Container")}{" "}
                            {String.fromCharCode(65 + cnt.position)}
                        </option>
                    ))}
                </Select>
                <ContainerDiagram container={selectedContainer} />
            </CardContent>
        </Card>
    );
};

export default DeviceContainersInfo;
