import createTokenProvider from "./tokenProvider";
import axios from "axios";
import { API_URL } from "../config";
import { useEffect, useState } from "react";

const createAuthProvider = () => {
    const tokenProvider = createTokenProvider();

    const login = (newTokens) => {
        tokenProvider.setTokens(newTokens.access, newTokens.refresh);
        updateUserInfo();
    };

    const logout = () => {
        tokenProvider.setTokens();
        tokenProvider.setUserInfo();
    };

    const authFetch = async () => {
        const token = await tokenProvider.getAccessToken();
        const axiosInstance = axios.create({
            baseURL: API_URL,
            timeout: 1000,
            headers: {
                Authorization: `Bearer ${token}`,
            },
        });

        return axiosInstance;
    };

    const useAuth = () => {
        const [isLogged, setIsLogged] = useState(tokenProvider.isLoggedIn());

        useEffect(() => {
            const listener = (newIsLogged) => {
                setIsLogged(newIsLogged);
            };

            tokenProvider.subscribe(listener);

            return () => {
                tokenProvider.unsubscribe(listener);
            };
        }, []);

        return [isLogged];
    };

    const getUserInfo = () => tokenProvider.getUserInfo();

    const checkAuth = async () => {
        const isAuthenticated = await tokenProvider.checkAuth();
        if (!isAuthenticated) {
            logout();
        }
    };

    const updateUserInfo = async () => {
        const token = await tokenProvider.getAccessToken();
        const jwt = JSON.parse(atob(token.split(".")[1]));
        const { data } = await (await authFetch()).get(
            `/account/users/${jwt.user_id}`
        );
        tokenProvider.setUserInfo(data);
    };

    return {
        useAuth,
        authFetch,
        checkAuth,
        getUserInfo,
        login,
        logout,
    };
};

export const {
    useAuth,
    authFetch,
    checkAuth,
    getUserInfo,
    login,
    logout,
} = createAuthProvider();
