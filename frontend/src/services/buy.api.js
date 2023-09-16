import axios from "axios";
import Swal from "sweetalert2";
const BASE_URL = "http://localhost:5002/compra";

export const comprarJuego = async (id) => {
  const headers = {
    "Content-Type": "application/json",
    "X-ACCESS-TOKEN": sessionStorage.getItem("token"),
    "user-id": sessionStorage.getItem("user_id"),
  };
  const config = {
    headers: headers,
  };
  const data_post = {
    id: id,
  };
  try {
    const { data } = await axios.post(BASE_URL, data_post, config);
    return data;
  } catch (error) {
    console.log(error.response);
  }
  return {};
};

export const compraExitosa = () => {
  return new Promise((resolve) => {
    Swal.fire({
      title: "Confirmación de compra",
      text: "La compra se ha realizado con exito",
      icon: "success",
      showCancelButton: false,
      confirmButtonColor: "#01d28e",
      confirmButtonText: "Listo :D",
      background: "#24283b",
      color: "white",
    }).then((result) => {
      resolve(result);
    });
  });
};

export const compraFallida = () => {
  return new Promise((resolve) => {
    Swal.fire({
      title: "Confirmación de compra",
      text: "Lo sentimos, no se pudo realizar la compra. Intentelo más tarde.",
      icon: "error",
      showCancelButton: false,
      confirmButtonColor: "#d33",
      confirmButtonText: "Okey :(",
      background: "#24283b",
      color: "white",
    }).then((result) => {
      resolve(result);
    });
  });
};
