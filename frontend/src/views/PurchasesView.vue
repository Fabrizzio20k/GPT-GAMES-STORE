<template>
  <LayoutComponent>
    <template #Content>
      <h2 class="search_text_p" id="welcome_text">
        {{
          user_name
            ? `${user_name}, estos son los juegos que has comprado:`
            : "Getting data, please wait..."
        }}
      </h2>
      <div class="main_container_games">
        <div class="container_games" id="container_games">
          <div
            class="item_game"
            v-for="juego in games"
            :key="juego.game.api_id"
          >
            <img :src="juego.game.cover" :alt="juego.game.name" />
            <h4 style="color: white">{{ juego.game.name }}</h4>
            <p>Publicado en: {{ juego.game.release_year }}</p>
            <p>
              Vendedor: {{ juego.oferta.usuario.name }}
              {{ juego.oferta.usuario.lastname }}
            </p>
            <p>Precio: S/. {{ juego.oferta.price }}</p>
            <p>Plataforma: {{ juego.oferta.platform }}</p>
          </div>
        </div>
      </div>
      <h3 class="search_results_counter" id="counter_games">
        En total has adquirido {{ games.length }} juegos
      </h3>
    </template>
  </LayoutComponent>
</template>

<script>
import LayoutComponent from "@/components/Layout.vue";
import { verifier_login } from "@/services/login.api";
import { getCompras } from "@/services/userResources.api";
import { getUserData } from "@/services/manageUserData.api";

export default {
  name: "PurchasesView",
  components: {
    LayoutComponent,
  },
  data() {
    return {
      games: [],
      user_name: "",
    };
  },
  async mounted() {
    await verifier_login();
    const user = await getUserData();
    this.user_name = user.name;
    const data = await getCompras();
    this.games = data.games;
  },
};
</script>

<style>
@import url("../css/purchases/purchases.css");
</style>
