

<template>
  <header>
  </header>

  <main>
    <button v-on:click.prevent="test" type="input">test api</button>
  </main>
</template>
<script>
export default {
  methods: {
    test: function (event) {
      fetch('/api/test',
        {
          method: "GET"
        })
        .then(response => response.json())
        .then(data => { console.log(data) })
    }
  },

}
</script>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
