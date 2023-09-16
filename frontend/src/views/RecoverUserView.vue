<template>
  <div class="background">
    <div class="overlay">
      <section class="ftco-section">
        <div class="container">
          <div class="row justify-content-center">
            <div class="col-md-6 text-center mb-5">
              <h2 class="heading-section">Recupere su contraseña ahora</h2>
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
                        Ingrese los datos de la cuenta a recuperar
                      </h3>
                    </div>
                  </div>
                  <form
                    id="data_recover"
                    class="signin-form"
                    @submit.prevent.stop="checkData"
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
                      <label
                        class="form-control-placeholder"
                        for="email"
                        id="text_email"
                        >Correo electrónico</label
                      >
                    </div>
                    <div class="form-group mt-3">
                      <input
                        type="text"
                        class="form-control"
                        name="name"
                        id="name"
                        v-model="user.name"
                        required
                      />
                      <label
                        class="form-control-placeholder"
                        for="name"
                        id="text_name"
                        >Nombre(s)</label
                      >
                    </div>

                    <div class="form-group" id="submit1">
                      <button
                        type="submit"
                        class="form-control btn btn-primary rounded submit px-3"
                      >
                        ¡Me siento con suerte!
                      </button>
                    </div>
                    <div class="form-group d-md-flex"></div>
                  </form>
                  <div class="d-flex">
                    <div class="w-100">
                      <h3
                        v-for="(error, index) in errors"
                        :key="index"
                        class="mb-4"
                        id="message_error2"
                      >
                        {{ error }}
                      </h3>
                      <h3 class="mb-4" id="text_change">
                        Ahora puede cambiar su contraseña
                      </h3>
                    </div>
                  </div>
                  <form
                    id="password_changer"
                    class="signin-form"
                    @submit.prevent.stop="changePassword"
                  >
                    <div class="form-group">
                      <input
                        id="password-field1"
                        type="password"
                        class="form-control"
                        name="password1"
                        required
                        v-model="user.password1"
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
                        v-model="user.password2"
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
                        id="submit2"
                      >
                        ¡Empezemos nuevamente!
                      </button>
                    </div>
                  </form>

                  <p class="text-center">
                    <a
                      data-toggle="tab"
                      href="/login"
                      style="color: #01d28e !important"
                      >🡸 Regresar al login</a
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
import { validateData, resetPassword } from "@/services/passwordRecovery.api";

export default {
  name: "RecoverUserView",
  data() {
    return {
      user: {
        email: "",
        name: "",
        password1: "",
        password2: "",
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
    async checkData() {
      await validateData(this.user);
    },
    async changePassword() {
      this.errors = await resetPassword(this.user);
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
