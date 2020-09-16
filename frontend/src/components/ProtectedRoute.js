import React from "react";
import { useAuth } from "../contexts/authProvider";
import { Route, Redirect } from "react-router-dom"; 
 
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