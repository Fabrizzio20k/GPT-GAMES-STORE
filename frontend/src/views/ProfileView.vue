<template>
  <LayoutComponent>
    <template #Content>
      <section class="ftco-section">
        <div class="container">
          <div class="row justify-content-center">
            <div class="col-md-12 col-lg-8">
              <div class="wrap" style="background-color: #0b233b">
                <div class="login-wrap p-4 p-md-5">
                  <div class="d-flex">
                    <div class="w-100">
                      <h3 class="mb-4" id="message_error"></h3>
                      <h3 class="mb-4" style="color: whitesmoke">
                        Actualiza tus datos en cualquier momento
                      </h3>
                    </div>
                  </div>
                  <form
                    id="register_data_2"
                    class="signin-form"
                    @submit.prevent.stop="updateData"
                  >
                    <div class="form-group mt-3">
                      <input
                        type="text"
                        class="form-control"
                        name="username"
                        id="name"
                        v-model="user.name"
                        required
                      />
                      <label class="form-control-placeholder" for="name"
                        >Nombre(s)</label
                      >
                    </div>
                    <div class="form-group mt-3">
                      <input
                        type="text"
                        class="form-control"
                        name="lastname"
                        id="lastname"
                        v-model="user.lastname"
                        required
                      />
                      <label class="form-control-placeholder" for="lastname"
                        >Apellido
                      </label>
                    </div>
                    <div class="form-group mt-3">
                      <textarea
                        class="form-control"
                        name="bio"
                        id="bio"
                        required
                        v-model="user.bio"
                      ></textarea>
                      <label class="form-control-placeholder" for="bio"
                        >Biografía (Max. 50 Palabras)</label
                      >
                    </div>
                    <div class="form-group mt-3">
                      <input
                        type="text"
                        class="form-control"
                        name="email"
                        id="email"
                        v-model="user.email"
                        disabled
                      />
                      <label
                        class="form-control-placeholder"
                        for="email"
                        style="display: none"
                        >Correo electrónico</label
                      >
                    </div>
                    <div class="form-group">
                      <input
                        id="password-field"
                        type="password"
                        class="form-control"
                        name="password"
                        v-model="user.password"
                      />
                      <label
                        class="form-control-placeholder"
                        for="password-field"
                        >Contraseña</label
                      >
                      <span
                        toggle="#password-field"
                        class="fa fa-fw fa-eye field-icon toggle-password"
                        @click="togglePassword"
                      ></span>
                    </div>
                    <div class="form-group">
                      <button
                        type="submit"
                        class="form-control btn btn-primary rounded submit px-3"
                      >
                        ¡Actualizar datos!
                      </button>
                    </div>
                    <div class="w-100">
                      <h3
                        class="mb-4"
                        id="confirm_msg"
                        style="font-size: medium"
                        v-if="confirm_delete"
                      >
                        ¿Estás seguro de eliminar tu cuenta? Esta acción no se
                        puede deshacer
                      </h3>
                    </div>
                    <div class="form-group">
                      <button
                        type="button"
                        @click="hide_msg"
                        class="form-control btn btn-primary rounded submit px-3"
                        id="prev_submit"
                        v-if="!confirm_delete"
                      >
                        ¡Eliminar mi cuenta!
                      </button>
                    </div>
                    <div class="form-group">
                      <button
                        type="button"
                        @click="delete_user"
                        class="form-control btn btn-primary rounded submit px-3"
                        id="submit_final"
                        v-if="confirm_delete"
                      >
                        ¡Si, quiero eliminar mi cuenta!
                      </button>
                    </div>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </template>
  </LayoutComponent>
</template>

<script>
import LayoutComponent from "@/components/Layout.vue";
import { no_resizable_textarea } from "@/js/login_functions";
import {
  getUserData,
  updateUserData,
  deleteUser,
} from "@/services/manageUserData.api";
import { verifier_login } from "@/services/login.api";

export default {
  name: "ProfileView",
  components: {
    LayoutComponent,
  },
  async mounted() {
    await verifier_login();
    this.user = await getUserData(this.user);
    no_resizable_textarea();
  },
  data() {
    return {
      user: {
        name: "",
        lastname: "",
        email: "",
        bio: "",
        password: "",
      },
      show_password: false,
      confirm_delete: false,
    };
  },
  methods: {
    togglePassword() {
      this.show_password = !this.show_password;

      let spanElement = document.querySelector(".toggle-password");

      let password_field = document.getElementById("password-field");

      if (this.show_password) {
        password_field.setAttribute("type", "text");
        spanElement.classList.remove("fa-eye");
        spanElement.classList.add("fa-eye-slash");
      } else {
        password_field.setAttribute("type", "password");
        spanElement.classList.remove("fa-eye-slash");
        spanElement.classList.add("fa-eye");
      }
    },
    hide_msg() {
      this.confirm_delete = !this.confirm_delete;
    },
    delete_user() {
      this.confirm_delete = !this.confirm_delete;
      deleteUser();
    },
    updateData() {
      updateUserData(this.user);
    },
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css?family=Lato:300,400,700&display=swap");
@import url("https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css");
@import url("../css/login/style.css");
@import url("../css/login/extra.css");
@import url("../css/user/user.css");
</style>
