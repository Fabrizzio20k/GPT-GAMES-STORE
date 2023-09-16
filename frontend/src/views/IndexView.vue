<template>
  <LayoutComponent>
    <template #Content>
      <div class="main_body">
        <SliderComponent />
        <div class="index_content">
          <h2 style="color: whitesmoke">Hola,</h2>
          <p>
            ¡Bienvenido a GPT Games! Aquí encontrarás los videojuegos más
            emocionantes y cautivadores del mercado. Nuestro amplio catálogo
            abarca todos los géneros y plataformas, ofreciéndote una experiencia
            de juego inigualable. No esperes más, explora nuestra selección y
            comienza a comprar ahora para sumergirte en emocionantes aventuras
            virtuales. En GPT Games, nos apasiona brindarte una experiencia de
            compra excepcional. Nuestro sitio web es fácil de navegar y seguro,
            para que puedas realizar tus compras con confianza. Además, contamos
            con un equipo de atención al cliente dedicado que estará encantado
            de ayudarte en cualquier consulta. Descubre la comodidad y emoción
            de comprar en GPT Games. Nos enorgullece trabajar en estrecha
            colaboración con los principales desarrolladores y editoriales de la
            industria para ofrecerte los títulos más recientes y populares.
            Desde juegos de acción llenos de adrenalina hasta cautivadoras
            historias de rol y desafiantes juegos de estrategia, tenemos algo
            para todos los jugadores. Sumérgete en un mundo de entretenimiento
            sin límites y disfruta de la emoción de los videojuegos en GPT
            Games.
          </p>
        </div>

        <div class="back_pac1"></div>
        <div class="pac_container">
          <div class="pacman">
            <div class="pacman-top"></div>
            <div class="pacman-bottom"></div>
            <div class="feed"></div>
          </div>
        </div>
        <div class="back_pac2"></div>
      </div>
    </template>
  </LayoutComponent>
</template>

<script>
import LayoutComponent from "@/components/Layout.vue";
import SliderComponent from "@/components/SliderComponent.vue";
import { verifier_login } from "@/services/login.api";

export default {
  name: "IndexView",
  components: {
    LayoutComponent,
    SliderComponent,
  },
  async mounted() {
    await verifier_login();
  },
};
</script>

<style>
@import url("../css/index/index.css");
</style>
