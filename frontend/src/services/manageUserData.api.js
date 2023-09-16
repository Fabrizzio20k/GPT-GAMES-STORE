import axios from "axios";
const BASE_URL = "http://localhost:5002/profile";

export const getUserData = async () => {
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
    if (data.success) {
      return data.user;
    }
  } catch (error) {
    console.log(error.response.data);
  }
  return {
    name: "",
    lastname: "",
    email: "",
    bio: "",
    password: "",
  };
};

export const updateUserData = async (user) => {
  const headers = {
    "Content-Type": "application/json",
    "X-ACCESS-TOKEN": sessionStorage.getItem("token"),
    "user-id": sessionStorage.getItem("user_id"),
  };
  const config = {
    headers: headers,
  };
  const message_error = document.getElementById("message_error");
  const user_data = {
    name: user.name,
    lastname: user.lastname,
    bio: user.bio,
    password: user.password || "",
  };
  try {
    const { data } = await axios.patch(BASE_URL, user_data, config);
    if (data.success) {
      message_error.style.display = "none";
      window.location.href = "/";
    } else {
      message_error.style.display = "block";
      message_error.innerHTML = data.message;
    }
  } catch (error) {
    console.log(error.response);
  }
};

export const deleteUser = async (user) => {
  const message_error = document.getElementById("message_error");
  try {
    const { data } = await axios.delete(BASE_URL, user);
    if (data.success) {
      message_error.style.display = "none";
      window.location.href = "/";
    }
  } catch (error) {
    message_error.style.display = "block";
    message_error.innerHTML = error.response.data.message;
  }
};
