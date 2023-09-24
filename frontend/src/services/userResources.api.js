import axios from "axios";
import { api_url } from "./DOMAIN";
const BASE_URL = api_url + ":5002/compra";

export const getCompras = async () => {
  const headers = {
    "Content-Type": "application/json",
    "X-ACCESS-TOKEN": sessionStorage.getItem("token"),
    "user-id": sessionStorage.getItem("user_id"),
  };
  const config = {
    headers: headers,
  };

  try {
    const { data } = await axios.get(BASE_URL, config);
    return data;
  } catch (error) {
    console.log(error);
  }

  return {};
};
