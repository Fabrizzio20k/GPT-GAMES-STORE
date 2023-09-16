import axios from "axios";
import Swal from "sweetalert2";
const BASE_URL = "http://localhost:5002/create";

const confirmationRegister = () => {
  return new Promise((resolve) => {
    Swal.fire({
      title: "Confirmación de registro",
      text: "Te has registrado correctamente",
      icon: "success",
      showCancelButton: false,
      confirmButtonColor: "#01d28e",
      confirmButtonText: "Volver al login",
      background: "#24283b",
      color: "white",
    }).then((result) => {
      resolve(result);
    });
  });
};

export const register = async (user) => {
  try {
    const { data } = await axios.post(BASE_URL, user);
    if (data.success) {
      const result = await confirmationRegister();
      if (result.isConfirmed) {
        window.location.href = "/login";
      } else {
        window.location.href = "/login";
      }
    } else {
      return data.errors;
    }
  } catch (error) {
    const message_error = document.getElementById("message_error");
    message_error.style.display = "block";
    message_error.innerHTML =
      "Ha ocurrido un error. Vuelve a intentarlo mas tarde 😪";
  }
  return [];
};
