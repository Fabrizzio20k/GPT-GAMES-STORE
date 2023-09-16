<template>
  <LayoutComponent>
    <template #Content>
      <div class="contenedor">
        <h1>Ya casi completas tu compra. Espera un momento por favor...</h1>
        <div class="spinner-box">
          <div class="configure-border-1">
            <div class="configure-core"></div>
          </div>
          <div class="configure-border-2">
            <div class="configure-core"></div>
          </div>
        </div>
      </div>
    </template>
  </LayoutComponent>
</template>

<script>
import LayoutComponent from "@/components/Layout.vue";
import { verifier_login } from "@/services/login.api";
import { comprarJuego, compraExitosa, compraFallida } from "@/services/buy.api";

export default {
  name: "CheckoutView",
  components: {
    LayoutComponent,
  },
  async mounted() {
    await verifier_login();
    const urlParams = new URLSearchParams(window.location.search);
    const id = urlParams.get("id");
    if (id) {
      const res = await comprarJuego(id);
      if (res.success) {
        const result = await compraExitosa();
        if (result.isConfirmed) {
          window.location.href =
            "/resume?id=" + res.compra.id + "&compra=exitosa";
        } else {
          window.location.href =
            "/resume?id=" + res.compra.id + "&compra=exitosa";
        }
      } else {
        const result = await compraFallida();
        if (result.isConfirmed) {
          window.location.href = "/";
        } else {
          window.location.href = "/";
        }
      }
    } else {
      window.location.href = "/";
    }
  },
};
</script>

<style scoped>
@import url("../css/wait/wait.css");
</style>
