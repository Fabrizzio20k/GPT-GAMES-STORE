<template>
  <div class="background">
    <div class="overlay">
      <section class="ftco-section">
        <div class="container">
          <div class="row justify-content-center">
            <div class="col-md-6 text-center mb-5">
              <h2 class="heading-section">Unete a una nueva experiencia</h2>
            </div>
          </div>
          <div class="row justify-content-center">
            <div class="col-md-7 col-lg-5">
              <div class="wrap">
                <div class="img"></div>
                <div class="login-wrap p-4 p-md-5">
                  <div class="d-flex">
                    <div class="w-100">
                      <h3 class="mb-4" id="message_error"></h3>
                      <h3 class="mb-4" style="color: whitesmoke">
                        Iniciar sesión
                      </h3>
                    </div>
                  </div>
                  <form
                    id="login_data"
                    class="signin-form"
                    @submit.prevent.stop="log_in"
                  >
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
                        id="password-field"
                        type="password"
                        class="form-control"
                        name="password"
                        v-model="user.password"
                        required
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
                        ¡Empezemos!
                      </button>
                    </div>
                    <div class="form-group d-md-flex">
                      <div class="w-100 text-md-flex">
                        <a
                          href="/password_recovery"
                          class="forgot"
                          style="color: #8d8d8d !important"
                          >¿Olvidaste tu contraseña?</a
                        >
                      </div>
                    </div>
                  </form>
                  <p class="text-center">
                    ¿Aún no eres miembro?
                    <a
                      data-toggle="tab"
                      href="/new_user"
                      style="color: #01d28e !important"
                      >Registrate aquí</a
                    >
                  </p>
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
import { login } from "@/services/login.api";

export default {
  name: "LoginView",
  data() {
    return {
      user: {
        email: "",
        password: "",
      },
      show_password: false,
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
    async log_in() {
      await login(this.user);
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
