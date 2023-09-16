<template>
  <div class="p-3 text-center">
    <div class="container">
      <div class="row">
        <div
          class="col-md-4 d-flex justify-content-center justify-content-md-start mb-3 mb-md-0"
        >
          <a href="/" class="ms-md-2">
            <img src="../logo/logo_2.png" height="50" />
          </a>
        </div>

        <div class="col-md-4">
          <form
            @submit.prevent.stop="searchGame"
            class="d-flex input-group w-auto my-auto mb-3 mb-md-0"
            id="searchForm"
          >
            <input
              autocomplete="off"
              type="search"
              class="form-control rounded"
              placeholder="Busca aquí"
              id="SearchInput"
              v-model="search"
            />
            <span class="input-group-text border-0 d-none d-lg-flex"
              ><i class="fas fa-search"></i
            ></span>
          </form>
        </div>

        <div
          class="col-md-4 d-flex justify-content-center justify-content-md-end align-items-center"
        >
          <div class="d-flex">
            <!-- Cart -->
            <a class="text-reset me-3" href="/purchases">
              <span
                ><i class="fa-solid fa-gamepad" style="color: #ffffff"></i
              ></span>
              <span
                class="badge rounded-pill badge-notification"
                id="counter_purchases_cart"
                >{{ Purchases.length > 9 ? "+9" : Purchases.length }}</span
              >
            </a>
            <!-- Marketplace dashboard -->
            <a class="text-reset me-3" href="/marketplace">
              <span
                ><i class="fa-solid fa-shop" style="color: #ffffff"></i
              ></span>
            </a>
            <!-- User -->
            <div class="dropdown">
              <a
                class="text-reset dropdown-toggle d-flex align-items-center hidden-arrow"
                href="#"
                id="navbarDropdownMenuLink"
                role="button"
                data-mdb-toggle="dropdown"
                aria-expanded="false"
              >
                <img
                  src="../images/user.png"
                  class="rounded-circle"
                  height="22"
                  alt=""
                  loading="lazy"
                />
              </a>
              <ul
                class="dropdown-menu dropdown-menu-end"
                aria-labelledby="navbarDropdownMenuLink"
              >
                <li>
                  <a class="dropdown-item" href="/profile">Mi perfil</a>
                </li>
                <li>
                  <a class="dropdown-item" @click="logOut">Cerrar sesión</a>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { getCompras } from "../services/userResources.api";
import { logout } from "../services/login.api";
export default {
  name: "NavbarComponent",
  data() {
    return {
      search: "",
      Purchases: [],
    };
  },
  async mounted() {
    const data = await getCompras();
    this.Purchases = data.games;
  },
  methods: {
    searchGame() {
      if (this.search !== "") {
        const queryParams = new URLSearchParams({
          name: this.search,
          genre: "Todas",
          platform: "Todas",
        });

        const url = `/search?${queryParams.toString()}`;
        window.location.href = url;
      }
    },
    async logOut() {
      logout();
    },
  },
};
</script>
<style>
@import url("https://fonts.googleapis.com/css?family=Lato:300,400,700&display=swap");
@import url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css");
@import url("https://mdbootstrap.com/api/snippets/static/download/MDB5-Pro-Advanced_6.2.0/css/mdb.min.css");
@import url("https://mdbootstrap.com/api/snippets/static/download/MDB5-Pro-Advanced_6.2.0/plugins/css/all.min.css");
@import url("../css/main_parts/navbar.css");
@import url("../css/main_parts/nav_extra.css");
@import url("../css/main_parts/nav_fixed.css");
</style>
