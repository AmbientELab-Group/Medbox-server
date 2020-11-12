import React from "react";
import { Route, Redirect } from "react-router-dom"; 
import { useAuth } from "../contexts/authProvider";
 
const ProtectedRoute = ({ children, redirectPath, ...rest }) => {
    const [logged] = useAuth();
    
    return (
        logged ? (
            <Route {...rest}>
                { children }
            </Route>
        ) : (
            <Redirect to={redirectPath}/>
        )
    );
};

export default ProtectedRoute;