import axios from "axios";
const BASE_URL = "http://172.31.83.155:5002/compra";

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
