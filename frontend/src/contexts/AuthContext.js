import React, { useState, createContext, useContext } from "react";

const AuthContext = createContext();

const useAuth = () => {
    const context = useContext(AuthContext);
    if (context === undefined) {
        throw new Error("useAuth must be used within a AuthProvider");
    }

    return [
        context.authState, 
        context.setAuthState, 
        context.isAuthenticated, 
        context.logout
    ];
}

const AuthProvider = ({ children }) => {
    const accessToken = localStorage.getItem("accessToken");
    const accessExp = localStorage.getItem("accessExp");
    const refreshToken = localStorage.getItem("refreshToken");
    const refreshExp = localStorage.getItem("refreshExp");
    const userInfo = localStorage.getItem("userInfo");
    const [ authState, setAuthState ] = useState({
        accessToken,
        accessExp,
        refreshToken,
        refreshExp,
        userInfo: userInfo ? JSON.parse(userInfo) : {}
    });

    const setAuthInfo = ({ access, refresh, userInfo }) => {
        let stateChange = {};

        if (access) {
            localStorage.setItem("accessToken", access.token);
            localStorage.setItem("accessExp", access.expiresAt);

            stateChange = {
                ...stateChange,
                accessToken: access.token,
                accessExp: access.expiresAt
            }
        }

        if (refresh) {
            localStorage.setItem("refreshToken", refresh.token);
            localStorage.setItem("refreshExp", refresh.expiresAt);

            stateChange = {
                ...stateChange,
                refreshToken: refresh.token,
                refreshExp: refresh.expiresAt
            }
        }

        if (userInfo) {
            localStorage.setItem("userInfo", JSON.stringify(userInfo));

            stateChange = {
                ...stateChange,
                userInfo
            }
        }

        setAuthState(stateChange)
    };

    const isAuthenticated = () => {
        if (!authState.accessToken || !authState.accessExp) {
            return false;
        }

        return new Date().getTime() / 1000 < authState.accessExp;
    };

    const logout = () => {
        localStorage.removeItem("accessToken");
        localStorage.removeItem("accessExp");
        localStorage.removeItem("refreshToken");
        localStorage.removeItem("refreshExp");
        localStorage.removeItem("userInfo");
        setAuthState({
            accessToken: null,
            accessExp: null,
            refreshToken: null,
            refreshExp: null,
            userInfo: {}
        });
    };

    return (
        <AuthContext.Provider value={{
            authState,
            setAuthState: authInfo => setAuthInfo(authInfo),
            isAuthenticated,
            logout
        }}>
            {children}
        </AuthContext.Provider>
    )
}

export { AuthProvider, useAuth };
