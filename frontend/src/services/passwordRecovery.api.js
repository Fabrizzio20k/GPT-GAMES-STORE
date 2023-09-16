import axios from "axios";
const BASE_URL = "http://localhost:5002/";

export const validateData = async (user) => {
  const message_error = document.getElementById("message_error");
  const password_changer = document.getElementById("password_changer");
  const submit1 = document.getElementById("submit1");
  const email = document.getElementById("email");
  const name = document.getElementById("name");
  const text_email = document.getElementById("text_email");
  const text_name = document.getElementById("text_name");
  const text_change = document.getElementById("text_change");

  try {
    const { data } = await axios.post(BASE_URL + "usuarios/data", user);
    if (data.success) {
      message_error.style.display = "none";
      password_changer.style.display = "block";
      submit1.style.display = "none";
      text_change.style.display = "block";
      email.disabled = true;
      name.disabled = true;
      text_email.innerHTML = "";
      text_name.innerHTML = "";
    } else {
      message_error.style.display = "block";
      password_changer.style.display = "none";
      message_error.innerHTML = data.errors;
      text_change.style.display = "none";
    }
  } catch (error) {
    console.log(error.response);
  }
};

export const resetPassword = async (user) => {
  try {
    const { data } = await axios.patch(BASE_URL + "usuarios/password", user);
    if (data.success) {
      window.location.href = "/login";
    } else {
      return data.errors;
    }
  } catch (error) {
    console.log(error.response);
  }

  return [];
};
