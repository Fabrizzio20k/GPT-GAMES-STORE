<template>
  <LayoutComponent>
    <template #Content>
      <div id="container">
        <div id="game_details">
          <div id="left_column">
            <div id="game_image">
              <img :src="game_image" :alt="game_name" />
            </div>
            <div id="synopsis">
              <h2>Sinopsis</h2>
              <p id="synopsis_p">
                {{ game_synopsis }}
              </p>
            </div>
          </div>
          <div id="right_column">
            <div id="game_info">
              <h3 id="game_name">{{ game_name }}</h3>
              <div id="year">Fecha de publicación: {{ game_year }}</div>
              <div id="genre">
                Generos:
                {{ game_genre }}
              </div>
              <div id="publisher">Editores: {{ game_publisher }}</div>
              <div id="platform">
                Plataformas:
                {{ game_platform }}
              </div>
            </div>
            <div id="offers_container">
              <h4>Ofertas disponibles</h4>
              <div
                class="offer-card"
                v-for="offer in offers"
                :key="offer.id"
                @click="buyGame(offer.id)"
              >
                <div class="seller">
                  Vendedor: {{ offer.usuario.name }}
                  {{ offer.usuario.lastname }}
                </div>
                <div class="price">S/. {{ offer.price }}</div>
                <div class="date-publish">
                  Fecha de publicación: {{ formatDate(offer.modified_at) }}
                </div>
                <div class="platform-publish">
                  Plataforma: {{ offer.platform }}
                </div>
              </div>
              <div id="buy_message" v-if="this.offers.length === 0">
                No hay ofertas disponibles para este título 😓
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="sell-card">
        <div class="sell-card-overlay"></div>
        <div class="sell-card-content">
          <div class="sell-card-text">
            <h3>¿Quieres vender este juego?</h3>
          </div>
          <div class="sell-card-button">
            <button @click="sellProduct">¡Vender ahora!</button>
          </div>
        </div>
      </div>
    </template>
  </LayoutComponent>
</template>

<script>
import LayoutComponent from "@/components/Layout.vue";
import { getGameData } from "@/services/search.api";
import { verifier_login } from "@/services/login.api";
import { confirmarCompra } from "@/services/seller.api";

export default {
  name: "VideogameView",
  components: {
    LayoutComponent,
  },
  methods: {
    async buyGame(id) {
      const result = await confirmarCompra(id);
      if (result.isConfirmed) {
        window.location.href = "/checkout?id=" + id;
      }
    },
    sellProduct() {
      const urlParams = new URLSearchParams(window.location.search);
      const id = urlParams.get("id");
      window.location.href = "/sell?id=" + id;
    },
    formatDate(dateString) {
      const fecha = new Date(dateString);
      const options = { year: "numeric", month: "long", day: "numeric" };
      return fecha.toLocaleDateString(undefined, options);
    },
  },
  data() {
    return {
      game_id: "Getting data...",
      game_name: "Getting data...",
      game_year: "Getting data...",
      game_genre: "Getting data...",
      game_publisher: "Getting data...",
      game_platform: "Getting data...",
      game_synopsis: "Getting data...",
      game_image: "Getting data...",
      offers: [],
    };
  },
  async mounted() {
    await verifier_login();
    const urlParams = new URLSearchParams(window.location.search);
    const id = urlParams.get("id");
    const game = await getGameData(id);
    this.game_id = game.game.api_id;
    this.game_name = game.game.name;
    this.game_year = game.game.release_year;
    this.game_genre = game.game.genres;
    this.game_genre = this.game_genre.join(", ");
    this.game_publisher = game.game.involved_companies;
    this.game_publisher = this.game_publisher.join(", ");
    this.game_platform = game.game.platforms;
    this.game_platform = this.game_platform.join(", ");
    this.game_synopsis = game.game.summary;
    this.game_image = game.game.cover;
    let prev_offers = game.ofertas;
    console.log(prev_offers);
    for (let i = 0; i < prev_offers.length; i++) {
      if (
        (prev_offers[i].usuario.id !== sessionStorage.getItem("user_id")) &
        !prev_offers[i].realizada
      ) {
        this.offers.push(prev_offers[i]);
      }
    }
  },
};
</script>

<style>
@import url("../css/game/game.css");
</style>
