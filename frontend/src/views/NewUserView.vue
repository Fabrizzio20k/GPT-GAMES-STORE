<template>
  <div class="background">
    <div class="overlay">
      <section class="ftco-section">
        <div class="container">
          <div class="row justify-content-center">
            <div class="col-md-6 text-center mb-5">
              <h2 class="heading-section">
                ¡Registrate ahora! Es gratis &#x1F911;
              </h2>
            </div>
          </div>
          <div class="row justify-content-center">
            <div class="col-md-7 col-lg-5">
              <div class="wrap">
                <div class="img"></div>
                <div class="login-wrap p-4 p-md-5">
                  <div class="d-flex">
                    <div class="w-100">
                      <h3
                        v-for="(error, index) in errors"
                        :key="index"
                        class="mb-4"
                        id="message_error_create"
                      >
                        {{ error }}
                      </h3>
                      <h3 class="mb-4" style="color: whitesmoke">
                        Registra tus datos aqui
                      </h3>
                    </div>
                  </div>
                  <form
                    id="register_data"
                    class="signin-form"
                    @submit.prevent.stop="registerUser"
                  >
                    <div class="form-group mt-3">
                      <input
                        type="text"
                        class="form-control"
                        name="name"
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
                        v-model="user.bio"
                        required
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
                        required
                      />
                      <label class="form-control-placeholder" for="email"
                        >Correo electrónico</label
                      >
                    </div>
                    <div class="form-group">
                      <input
                        id="password-field1"
                        type="password"
                        class="form-control"
                        name="password1"
                        required
                        v-model="user.password"
                      />
                      <label
                        class="form-control-placeholder"
                        for="password-field1"
                        >Nueva contraseña</label
                      >
                      <span
                        toggle="#password-field1"
                        id="tpassword1"
                        class="fa fa-fw fa-eye field-icon toggle-password"
                        @click="togglePassword(1)"
                      ></span>
                    </div>
                    <div class="form-group">
                      <input
                        id="password-field2"
                        type="password"
                        class="form-control"
                        name="password2"
                        required
                        v-model="user.confirmationPassword"
                      />
                      <label
                        class="form-control-placeholder"
                        for="password-field2"
                        >Confirme la contraseña</label
                      >
                      <span
                        toggle="#password-field2"
                        id="tpassword2"
                        class="fa fa-fw fa-eye field-icon toggle-password"
                        @click="togglePassword(2)"
                      ></span>
                    </div>
                    <div class="form-group">
                      <button
                        type="submit"
                        class="form-control btn btn-primary rounded submit px-3"
                      >
                        ¡Registrate ahora!
                      </button>
                    </div>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import { no_resizable_textarea } from "@/js/login_functions";
import { register } from "@/services/register.api";

export default {
  name: "NewUserView",
  mounted() {
    no_resizable_textarea();
  },
  data() {
    return {
      user: {
        name: "",
        lastname: "",
        bio: "",
        email: "",
        password: "",
        confirmationPassword: "",
      },
      show_password1: false,
      show_password2: false,
      errors: [],
    };
  },
  methods: {
    togglePassword(n) {
      let spanElement = document.getElementById("tpassword" + n);
      let password_field = document.getElementById("password-field" + n);

      if (n == 1) {
        this.show_password1 = !this.show_password1;
        if (this.show_password1) {
          password_field.setAttribute("type", "text");
          spanElement.classList.remove("fa-eye");
          spanElement.classList.add("fa-eye-slash");
        } else {
          password_field.setAttribute("type", "password");
          spanElement.classList.remove("fa-eye-slash");
          spanElement.classList.add("fa-eye");
        }
      } else {
        this.show_password2 = !this.show_password2;
        if (this.show_password2) {
          password_field.setAttribute("type", "text");
          spanElement.classList.remove("fa-eye");
          spanElement.classList.add("fa-eye-slash");
        } else {
          password_field.setAttribute("type", "password");
          spanElement.classList.remove("fa-eye-slash");
          spanElement.classList.add("fa-eye");
        }
      }
    },
    async registerUser() {
      this.errors = await register(this.user);
    },
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Lato:300,400,700&display=swap");
@import url("https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css");
@import url("../css/login/style.css");
@import url("../css/login/extra.css");
</style>
