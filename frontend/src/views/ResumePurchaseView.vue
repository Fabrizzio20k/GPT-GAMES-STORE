<template>
  <LayoutComponent>
    <template #Content>
      <div class="wrapper_resume">
        <div class="container_resume">
          <h1>¡Gracias por tu compra!</h1>

          <div class="thank-you">
            <p>
              Hemos enviado una copia de la orden de compra a tu correo
              electrónico &#x1F60A;
            </p>
          </div>

          <div class="order-details">
            <div class="image-resume">
              <img :src="purchase_image" :alt="purchase_game" />
            </div>
            <div class="info">
              <div class="title" id="game_title">{{ purchase_game }}</div>
              <div class="purchase-date" id="purchase_date">
                Fecha de compra:
                {{
                  purchase_date
                    ? formatear_fecha(purchase_date)
                    : "Getting data..."
                }}
              </div>
              <div class="purchase-date" id="purchase_date">
                Vendedor: {{ purchase_vendor_name }}
                {{ purchase_vendor_last_name }}
              </div>
              <div class="purchase-date" id="purchase_date">
                Plataforma: {{ purchase_platform }}
              </div>
              <div class="purchase-date" id="purchase_date">
                Precio: S/. {{ purchase_price }}
              </div>
              <div class="order-id" id="order_id">
                ID de compra: {{ purchase_id }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </template>
  </LayoutComponent>
</template>

<script>
import LayoutComponent from "@/components/Layout.vue";
import { getPurchaseData, formatearFecha } from "@/services/search.api";
import { verifier_login } from "@/services/login.api";

export default {
  name: "ResumePurchaseView",
  components: {
    LayoutComponent,
  },
  async mounted() {
    await verifier_login();
    const urlParams = new URLSearchParams(window.location.search);
    const id = urlParams.get("id");
    const purchase = await getPurchaseData(id);
    this.purchase_game = purchase.compra.game.name;
    this.purchase_image = purchase.compra.game.cover;
    this.purchase_date = purchase.compra.created_at;
    this.purchase_id = purchase.compra.id;
    this.purchase_vendor_name = purchase.compra.oferta.usuario.name;
    this.purchase_vendor_last_name = purchase.compra.oferta.usuario.lastname;
    this.purchase_platform = purchase.compra.oferta.platform;
    this.purchase_price = purchase.compra.oferta.price;
  },
  data() {
    return {
      purchase_game: "Getting data...",
      purchase_date: "",
      purchase_id: "Getting data...",
      purchase_image: "Getting data...",
      purchase_vendor_name: "Getting data...",
      purchase_vendor_last_name: "Getting data...",
      purchase_price: "Getting data...",
      purchase_platform: "Getting data...",
    };
  },
  methods: {
    formatear_fecha(fecha) {
      return formatearFecha(fecha);
    },
  },
};
</script>

<style scoped>
@import url("../css/resume/resume.css");
</style>
