<template>
  <LayoutComponent>
    <template #Navbar-Search>
      <NavbarSearchComponent
        :search_platforms="this.s_platforms"
        :search_genres="this.s_genres"
        @updateSearch="updateGames"
      />
    </template>
    <template #Content>
      <h2 class="search_text_p" id="search_text_p">
        {{ "Resultados para la busqueda: " + search }}
      </h2>
      <div class="main_container_games">
        <div class="container_games" id="container_games">
          <div
            class="item_game"
            v-for="game in games"
            :key="game.api_id"
            @click="getVideogame(game.api_id)"
          >
            <img :src="game.cover" :alt="game.name" />
            <h4 style="color: white">{{ game.name }}</h4>
            <p>Publicado en: {{ game.release_year }}</p>
          </div>
        </div>
      </div>
      <h3 class="search_results_counter" id="search_results_counter">
        {{
          games.length > 0
            ? `Mostrando ${games.length} resultado(s)`
            : "No hay resultados que coincidan con la busqueda"
        }}
      </h3>
    </template>
  </LayoutComponent>
</template>

<script>
import LayoutComponent from "@/components/Layout.vue";
import NavbarSearchComponent from "@/components/NavbarSearchComponent.vue";
import { getGenres, getPlatforms, getGames } from "@/services/search.api";
import { verifier_login } from "@/services/login.api";

export default {
  name: "SearchView",
  components: {
    LayoutComponent,
    NavbarSearchComponent,
  },
  data() {
    return {
      s_platforms: [],
      s_genres: [],
      games: [],
      search: "",
    };
  },
  async mounted() {
    await verifier_login();
    const params = new URLSearchParams(window.location.search);
    this.search = params.get("name") || "";
    this.games = await getGames();
    let platform_request = await getPlatforms();
    this.s_platforms = platform_request.data;
    let genre_request = await getGenres();
    this.s_genres = genre_request.data;
  },
  methods: {
    async updateGames() {
      this.games = await getGames();
    },
    getVideogame(id) {
      window.location.href = `/videogame?id=${id}`;
    },
  },
};
</script>

<style>
@import url("../css/search/search.css");
</style>
