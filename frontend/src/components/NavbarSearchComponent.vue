<template>
  <!-- Navbar -->
  <nav class="navbar navbar-expand-lg">
    <!-- Container wrapper -->
    <div
      class="container justify-content-center justify-content-md-between"
      style="font-weight: bold"
    >
      <!-- Left links -->
      <ul class="navbar-nav flex-row">
        <li class="nav-item me-2 me-lg-0">
          <a
            class="nav-link btn shadow-0 p-0 me-3"
            role="button"
            data-mdb-toggle="sidenav"
            data-mdb-target="#sidenav-1"
            aria-controls="#sidenav-1"
            aria-haspopup="true"
          >
            <i class="fas fa-bars me-1"></i>
            <span>Categorias</span>
          </a>
        </li>
      </ul>
    </div>
    <!-- Container wrapper -->
  </nav>
  <!-- Navbar -->

  <!-- Sidenav -->
  <div
    id="sidenav-1"
    class="sidenav"
    role="navigation"
    data-mdb-hidden="true"
    data-mdb-accordion="true"
  >
    <ul class="sidenav-menu">
      <li class="sidenav-item">
        <a class="sidenav-link"
          ><i class="fas fa-layer-group pe-3"></i><span>Géneros</span></a
        >
        <ul class="sidenav-collapse show" id="list_genres">
          <li
            class="sidenav-item"
            v-for="genre in search_genres"
            :key="genre.id"
            :id="genre.name"
            @click="updateSearchParams('genre', genre.name)"
          >
            <a class="sidenav-link" :id="genre.name">{{ genre.name }}</a>
          </li>
        </ul>
      </li>
      <li class="sidenav-item">
        <a class="sidenav-link"
          ><i class="fas fa-gem pe-3"></i><span>Plataformas</span></a
        >
        <ul class="sidenav-collapse" id="list_platforms">
          <li
            class="sidenav-item"
            v-for="platform in search_platforms"
            :key="platform.id"
            :id="platform.name"
            @click="updateSearchParams('platform', platform.name)"
          >
            <a class="sidenav-link" :id="platform.name">{{ platform.name }}</a>
          </li>
        </ul>
      </li>
    </ul>
  </div>
  <!-- Sidenav -->
</template>
<script>
import { changeSearchParams } from "@/js/search_functions";

export default {
  name: "NavbarSearchComponent",
  emits: ["updateSearch"],
  props: {
    search_platforms: {
      type: Array,
      required: true,
    },
    search_genres: {
      type: Array,
      required: true,
    },
  },
  methods: {
    updateSearchParams(categoria, elemento) {
      changeSearchParams(categoria, elemento);
      this.$emit("updateSearch");
    },
  },
};
</script>
<style></style>
