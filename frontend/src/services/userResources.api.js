import axios from "axios";
const BASE_URL = "http://34.192.216.79:5002/compra";

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
