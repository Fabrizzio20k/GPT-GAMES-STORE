import Swal from "sweetalert2";
import axios from "axios";

const BASE_URL = "http://localhost:5002/";

export const confirmarVenta = () => {
  return new Promise((resolve) => {
    Swal.fire({
      title: "Confirmación de venta",
      text: "¿Estás seguro de que quieres vender este juego?",
      icon: "question",
      showCancelButton: true,
      confirmButtonColor: "#01d28e",
      cancelButtonColor: "#d33",
      confirmButtonText: "Obvio",
      cancelButtonText: "Ya no",
      background: "#24283b",
      color: "white",
    }).then((result) => {
      resolve(result);
    });
  });
};

export const confirmarCompra = () => {
  return new Promise((resolve) => {
    Swal.fire({
      title: "Confirmación de compra",
      text: "¿Estás seguro de que quieres comprar este juego?",
      icon: "question",
      showCancelButton: true,
      confirmButtonColor: "#01d28e",
      cancelButtonColor: "#d33",
      confirmButtonText: "¡Si, lo quiero!",
      cancelButtonText: "Ya no",
      background: "#24283b",
      color: "white",
    }).then((result) => {
      resolve(result);
    });
  });
};

export const confirmarActualizacionVenta = () => {
  return new Promise((resolve) => {
    Swal.fire({
      title: "Confirmación de venta",
      text: "¿Estás seguro de actualizar los datos de esta venta?",
      icon: "question",
      showCancelButton: true,
      confirmButtonColor: "#01d28e",
      cancelButtonColor: "#d33",
      confirmButtonText: "Obvio",
      cancelButtonText: "Ya no",
      background: "#24283b",
      color: "white",
    }).then((result) => {
      resolve(result);
    });
  });
};

export const confirmarEliminacionOferta = () => {
  return new Promise((resolve) => {
    Swal.fire({
      title: "Confirmar eliminación de oferta",
      text: "¿Estás seguro de que quieres eliminar esta venta? Esta acción no se puede deshacer.",
      icon: "question",
      showCancelButton: true,
      confirmButtonColor: "#d33",
      cancelButtonColor: "#01d28e",
      confirmButtonText: "Si, eliminar",
      cancelButtonText: "Ya no",
      background: "#24283b",
      color: "white",
    }).then((result) => {
      resolve(result);
    });
  });
};

const confirmationOffer = () => {
  return new Promise((resolve) => {
    Swal.fire({
      title: "Confirmación de venta",
      text: "Tu oferta de este juego se ha realizado con éxito",
      icon: "success",
      showCancelButton: false,
      confirmButtonColor: "#01d28e",
      confirmButtonText: "Okey",
      background: "#24283b",
      color: "white",
    }).then((result) => {
      resolve(result);
    });
  });
};

const confirmationUpdateOffer = () => {
  return new Promise((resolve) => {
    Swal.fire({
      title: "Confirmación de venta",
      text: "Tu oferta de este juego se ha actualizado con exito",
      icon: "success",
      showCancelButton: false,
      confirmButtonColor: "#01d28e",
      confirmButtonText: "Okey",
      background: "#24283b",
      color: "white",
    }).then((result) => {
      resolve(result);
    });
  });
};

export const createSale = async (sellData) => {
  const headers = {
    "Content-Type": "application/json",
    "X-ACCESS-TOKEN": sessionStorage.getItem("token"),
    "user-id": sessionStorage.getItem("user_id"),
  };
  const config = {
    headers: headers,
  };
  try {
    const { data } = await axios.post(BASE_URL + "oferta", sellData, config);
    if (data.success) {
      const result = await confirmationOffer();
      if (result.isConfirmed) {
        window.location.href = "/marketplace";
      } else {
        window.location.href = "/marketplace";
      }
    } else {
      Swal.fire({
        title: "Error",
        text: data.message,
        icon: "error",
        showCancelButton: false,
        confirmButtonColor: "#d33",
        confirmButtonText: "Okey :(",
        background: "#24283b",
        color: "white",
      });
    }
  } catch (error) {
    console.log(error.response);
  }
};

export const getSales = async () => {
  const headers = {
    "Content-Type": "application/json",
    "X-ACCESS-TOKEN": sessionStorage.getItem("token"),
    "user-id": sessionStorage.getItem("user_id"),
  };
  const config = {
    headers: headers,
  };
  try {
    const { data } = await axios.get(BASE_URL + "oferta", config);
    return data;
  } catch (error) {
    console.log(error.response);
  }
  return {};
};

export const deleteSale = async (id) => {
  const headers = {
    "Content-Type": "application/json",
    "X-ACCESS-TOKEN": sessionStorage.getItem("token"),
    "user-id": sessionStorage.getItem("user_id"),
  };
  const config = {
    headers: headers,
  };
  try {
    const { data } = await axios.delete(BASE_URL + "oferta/" + id, config);
    if (data.success) {
      Swal.fire({
        title: "Listo",
        text: "La oferta se ha eliminado con éxito",
        icon: "success",
        showCancelButton: false,
        confirmButtonColor: "#01d28e",
        confirmButtonText: "Okey",
        background: "#24283b",
        color: "white",
      });
    } else {
      Swal.fire({
        title: "Error",
        text: data.message,
        icon: "error",
        showCancelButton: false,
        confirmButtonColor: "#d33",
        confirmButtonText: "Okey :(",
        background: "#24283b",
        color: "white",
      });
    }
  } catch (error) {
    console.log(error.response);
  }
};

export const getOfferById = async (id) => {
  const headers = {
    "Content-Type": "application/json",
    "X-ACCESS-TOKEN": sessionStorage.getItem("token"),
    "user-id": sessionStorage.getItem("user_id"),
  };
  const config = {
    headers: headers,
  };
  try {
    const { data } = await axios.get(BASE_URL + "oferta/" + id, config);
    return data;
  } catch (error) {
    console.log(error.response);
  }
  return {};
};

export const updateSale = async (id, sellData) => {
  const headers = {
    "Content-Type": "application/json",
    "X-ACCESS-TOKEN": sessionStorage.getItem("token"),
    "user-id": sessionStorage.getItem("user_id"),
  };
  const config = {
    headers: headers,
  };
  try {
    const { data } = await axios.patch(
      BASE_URL + "oferta/" + id,
      sellData,
      config
    );
    if (data.success) {
      const result = await confirmationUpdateOffer();
      if (result.isConfirmed) {
        window.location.href = "/marketplace";
      } else {
        window.location.href = "/marketplace";
      }
    } else {
      Swal.fire({
        title: "Error",
        text: data.message,
        icon: "error",
        showCancelButton: false,
        confirmButtonColor: "#d33",
        confirmButtonText: "Okey :(",
        background: "#24283b",
        color: "white",
      });
    }
  } catch (error) {
    console.log(error.response);
  }
};
