<template>
  <Splide :options="{ rewind: true }" aria-label="My Favorite Images">
    <SplideSlide>
      <img src="../images/Slide_1.png" alt="Sample 1" />
    </SplideSlide>
    <SplideSlide>
      <img src="../images/Slide_2.png" alt="Sample 2" />
    </SplideSlide>
    <SplideSlide>
      <img src="../images/Slide_3.png" alt="Sample 2" />
    </SplideSlide>
  </Splide>
</template>
<script>
import { Splide, SplideSlide } from "@splidejs/vue-splide";
export default {
  name: "SliderComponent",
  components: {
    Splide,
    SplideSlide,
  },
};
</script>
<style>
@import url("../css/slider/splide-sea-green.min.css");
</style>
