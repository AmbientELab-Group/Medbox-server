import axios from "axios";
import { API_URL } from "../config";

const publicAccountFetch = axios.create({
  baseURL: API_URL + "/account"
});

export { publicAccountFetch };