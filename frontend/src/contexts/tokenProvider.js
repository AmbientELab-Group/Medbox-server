import { publicTokenFetch } from "../api/publicFetch";

const createTokenProvider = () => {
    let accessToken = JSON.parse(
        localStorage.getItem("access-token") || "null"
    );
    let refreshToken = JSON.parse(
        localStorage.getItem("refresh-token") || "null"
    );
    let userInfo = JSON.parse(localStorage.getItem("user-info") || "null");
    let observers = [];

    // returns expiration date in ms from provided token
    const getExpirationDate = (jwtToken) => {
        if (!jwtToken) {
            return null;
        }

        const jwt = JSON.parse(atob(jwtToken.split(".")[1]));

        return jwt?.exp && jwt.exp * 1000;
    };

    // returns true if token is expired, false otherwise
    const isExpired = (exp) => {
        if (!exp) {
            return null;
        }

        return Date.now() > exp;
    };

    // returns refresh payload or null if refresh token is invalid
    const fetchRefresh = async () => {
        try {
            const { data } = await publicTokenFetch.post("/refresh", {
                refresh: refreshToken,
            });

            return data;
        } catch (error) {
            return null;
        }
    };

    // returns valid access token, revalidates if expired
    // clears tokens and user data on failure
    const getAccessToken = async () => {
        if (isExpired(getExpirationDate(accessToken))) {
            const data = await fetchRefresh();

            if (data) {
                setTokens(data.access, refreshToken);
            } else {
                setTokens();
                setUserInfo();
            }
        }

        return accessToken;
    };

    const getRefreshToken = () => {
        return refreshToken;
    };

    const getUserInfo = () => {
        return userInfo;
    };

    // sets tokens in provider state and local storage
    // requires both tokens to set them, clears if at least one lacks
    // notifies subscribers about change
    const setTokens = (newAccess = null, newRefresh = null) => {
        if (newAccess && newRefresh) {
            localStorage.setItem("access-token", JSON.stringify(newAccess));
            localStorage.setItem("refresh-token", JSON.stringify(newRefresh));
            accessToken = newAccess;
            refreshToken = newRefresh;
        } else {
            localStorage.removeItem("access-token");
            localStorage.removeItem("refresh-token");
            accessToken = refreshToken = null;
        }

        notify();
    };

    // sets user info if info is provided, clears otherwise
    const setUserInfo = (newInfo) => {
        if (newInfo) {
            localStorage.setItem("user-info", JSON.stringify(newInfo));
            userInfo = newInfo;
        } else {
            localStorage.removeItem("user-info");
            userInfo = null;
        }
    };

    // checks login state based on token presece (stale included)
    const isLoggedIn = () => {
        return !!accessToken && !!refreshToken;
    };

    const subscribe = (observer) => {
        observers.push(observer);
    };

    const unsubscribe = (observer) => {
        observers = observers.filter((_observer) => _observer !== observer);
    };

    const notify = () => {
        const isLogged = isLoggedIn();
        observers.forEach((observer) => observer(isLogged));
    };

    // checks if access token is valid, tries to refresh and returns true on success
    const checkAuth = async () => {
        if (isExpired(getExpirationDate(accessToken))) {
            const newAccess = getAccessToken();
            return !!newAccess;
        }

        return true;
    };

    return {
        getAccessToken,
        getRefreshToken,
        getUserInfo,
        setUserInfo,
        isLoggedIn,
        checkAuth,
        setTokens,
        subscribe,
        unsubscribe,
    };
};

export default createTokenProvider;
