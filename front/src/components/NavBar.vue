<template>

</template>

<script>
export default {
  name: "NavBar",

  data: () => ({
    appDrawer: false,
    loggingOut: false,
  }),

  methods: {
    logout() {
      this.$session.destroy();
      this.$router.push('/login');
    }
  }
}
</script>

<style scoped>

</style>