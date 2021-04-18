import axios from "axios";
import { API_URL } from "../config";

const publicAccountFetch = axios.create({
    baseURL: API_URL + "/account",
});

const publicTokenFetch = axios.create({
    baseURL: API_URL + "/account/token",
});

export { publicAccountFetch, publicTokenFetch };
