import React, { useState } from "react";
import { useHistory } from "react-router-dom";
import MoreHorizIcon from "@material-ui/icons/MoreHoriz";
import Popover from "@material-ui/core/Popover";
import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import IconButton from "@material-ui/core/IconButton";

const ContextMenu = ({editUrl}) => {
    const history = useHistory();
    const [anchorEl, setAnchorEl] = useState(null);

    const handleClick = (event) => {
        setAnchorEl(event.currentTarget);
    };

    const handleClose = () => {
        setAnchorEl(null);
    };

    const open = Boolean(anchorEl);
    const id = open ? 'simple-popover' : undefined;

    return (
        <>
        <IconButton aria-describedby={id} onClick={handleClick}>
            <MoreHorizIcon/>
        </IconButton>
        <Popover 
            id={id}
            open={open}
            anchorEl={anchorEl}
            onClose={handleClose}
            anchorOrigin={{
                vertical: "bottom",
                horizontal: "right",
            }}
            transformOrigin={{
                vertical: "top",
                horizontal: "right",
            }}
        >
            <List style={{width: 100}}>
                <ListItem button onClick={()=>{
                    handleClose();
                    history.push(editUrl);
                }}>
                    Edit
                </ListItem>
                <ListItem button>
                    Delete
                </ListItem>
            </List>
        </Popover>
        </>
    );
};

export default ContextMenu;
