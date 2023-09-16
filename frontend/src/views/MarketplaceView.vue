<template>
  <LayoutComponent>
    <template #Content>
      <h2 class="titulo-market">
        Desde aquí podras administrar todos los juegos que has publicado hasta
        ahora 🤑
      </h2>
      <div class="container-market">
        <div class="row-market" v-for="sale in pending" :key="sale.id">
          <div class="column-market-image">
            <div class="image-container-market">
              <img :src="sale.game.cover" alt="Image" />
            </div>
          </div>
          <div class="column-market-content">
            <h2 class="no-venta">Estado de venta: No vendido</h2>
            <h2 class="nombre">Nombre del juego: {{ sale.game.name }}</h2>
            <div class="form_group_game_market">
              <label for="price" class="label-market">PRECIO - S/</label>
              <input
                type="number"
                id="price_market"
                class="form_control_game_market"
                :value="sale.price"
                required
                disabled
              />
            </div>
            <div class="form_group_game_market">
              <label for="platforms" class="label-market">PLATAFORMAS</label>
              <div class="custom-select-market">
                <input
                  type="text"
                  id="platform_market"
                  class="form_control_game_market"
                  :value="sale.platform"
                  required
                  disabled
                />
              </div>
            </div>

            <div class="botones-market">
              <button class="actualizar-market" @click="updateOffer(sale.id)">
                Actualizar
              </button>
              <button class="eliminar-market" @click="deleteOffer(sale.id)">
                Eliminar
              </button>
            </div>
          </div>
        </div>

        <div class="row-market" v-for="sale in sales" :key="sale.id">
          <div class="column-market-image">
            <div class="image-container-market">
              <img :src="sale.game.cover" alt="Image" />
            </div>
          </div>
          <div class="column-market-content">
            <h2 class="venta">Estado de venta: Vendido</h2>
            <h2 class="nombre">Nombre del juego: {{ sale.game.name }}</h2>
            <div class="form_group_game_market">
              <label for="price" class="label-market">PRECIO - S/</label>
              <input
                type="number"
                id="price_market"
                class="form_control_game_market"
                :value="sale.price"
                required
                disabled
              />
            </div>
            <div class="form_group_game_market">
              <label for="platforms" class="label-market">PLATAFORMAS</label>
              <div class="custom-select-market">
                <input
                  type="text"
                  id="platform_market"
                  class="form_control_game_market"
                  :value="sale.platform"
                  required
                  disabled
                />
              </div>
            </div>
          </div>
        </div>
        <h1 v-if="showMessage">
          Aún no has publicado ningun juego. ¿Por qué no hacerlo ahora? 😎
        </h1>
      </div>
    </template>
  </LayoutComponent>
</template>

<script>
import LayoutComponent from "@/components/Layout.vue";
import { verifier_login } from "@/services/login.api";
import {
  getSales,
  confirmarEliminacionOferta,
  deleteSale,
} from "@/services/seller.api";

export default {
  name: "MarketplaceView",
  components: {
    LayoutComponent,
  },
  data() {
    return {
      sales: [],
      pending: [],
      showMessage: false,
    };
  },
  async mounted() {
    await verifier_login();
    const data = await getSales();
    this.sales = data.ofertas_done;
    this.pending = data.ofertas_pending;
    if (this.sales.length === 0 && this.pending.length === 0) {
      this.showMessage = true;
    }
  },
  methods: {
    async deleteOffer(id) {
      const result = await confirmarEliminacionOferta();
      if (result.isConfirmed) {
        try {
          await deleteSale(id);
          const data = await getSales();
          this.sales = data.ofertas_done;
          this.pending = data.ofertas_pending;
        } catch (error) {
          console.log(error);
        }
      }
    },
    updateOffer(id) {
      window.location.href = `/offer?id=${id}`;
    },
  },
};
</script>

<style>
@import url("../css/marketplace/update_game.css");
</style>
