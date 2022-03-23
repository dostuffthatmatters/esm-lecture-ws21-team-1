<template>
  <div
    class="fixed px-3 py-2 text-sm font-medium text-green-800 z-50"
    v-bind:class="{
      'left-0': x === 'l',
      'right-0': x === 'r',
      'top-0': y === 't',
      'bottom-0': y === 'b',
    }"
  >
    <SlideCurrentNo />
  </div>
</template>

<script>
export default {
  props: {
    x: {
      default: "r",
      type: String,
      validator: (value) => value === "l" || value === "r",
    },
    y: {
      default: "b",
      type: String,
      validator: (value) => value === "t" || value === "b",
    },
  },
};
</script>