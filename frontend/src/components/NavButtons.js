import React from "react";
import { useHistory } from "react-router-dom";
import NavigateBeforeIcon from '@material-ui/icons/NavigateBefore';
import NavigateNextIcon from '@material-ui/icons/NavigateNext';
import Toolbar from "@material-ui/core/Toolbar";
import IconButton from "@material-ui/core/IconButton"; 

const NavButtons = () => {
    const history = useHistory();

    return (
        <Toolbar>
            <IconButton onClick={()=>history.goBack()}>
                <NavigateBeforeIcon/>
            </IconButton>
            <IconButton onClick={()=>history.goForward()}>
                <NavigateNextIcon/>
            </IconButton>
        </Toolbar>
    );
};

export default NavButtons
