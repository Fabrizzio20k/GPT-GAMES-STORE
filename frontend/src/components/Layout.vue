<template>
  <header class="mb-0">
    <NavbarComponent />
    <slot name="Navbar-Search"></slot>
  </header>
  <BackgroundComponent />
  <slot name="Content"></slot>
  <FooterComponent />
</template>

<script>
import NavbarComponent from "./NavbarComponent.vue";
import BackgroundComponent from "./BackgroundComponent.vue";
import FooterComponent from "./FooterComponent.vue";

export default {
  name: "LayoutComponent",
  components: {
    NavbarComponent,
    BackgroundComponent,
    FooterComponent,
  },
  setup() {
    const recaptchaScript = document.createElement("script");
    recaptchaScript.setAttribute(
      "src",
      "https://mdbootstrap.com/api/snippets/static/download/MDB5-Pro-Advanced_6.2.0/js/mdb.min.js"
    );
    document.head.appendChild(recaptchaScript);

    const fontAwesomeScript = document.createElement("script");
    fontAwesomeScript.setAttribute(
      "src",
      "https://mdbootstrap.com/api/snippets/static/download/MDB5-Pro-Advanced_6.2.0/plugins/js/all.min.js"
    );
    document.head.appendChild(fontAwesomeScript);

    const fontAwesomeScript2 = document.createElement("script");
    fontAwesomeScript2.setAttribute(
      "src",
      "https://kit.fontawesome.com/2116c4358d.js"
    );
    document.head.appendChild(fontAwesomeScript2);
  },
};
</script>

<style></style>
