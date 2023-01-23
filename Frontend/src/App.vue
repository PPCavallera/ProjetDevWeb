

<template>
  <header>
  </header>

  <main>
    <aside>
      <SideBar></SideBar>
    </aside>
    <article>
      <ChatInterface></ChatInterface>
      <Prompt></Prompt>
    </article>

  </main>
</template>
<script>
import ChatInterface from "./components/ChatInterface.vue"
import Prompt from "./components/Prompt.vue"
import SideBar from "./components/SideBar.vue"

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
  components: { Prompt, ChatInterface, SideBar }
}
</script>

<style scoped>
main {
  display: flex;
  flex-direction: row;
  flex: 1;

}

article {
  flex: 70vh;
}

aside {
  display: flex;
  flex: 7vh;
  /* background-color: #aaa; */
}

header {
  line-height: 1.5;
}
</style>
