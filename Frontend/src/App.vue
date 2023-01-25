

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
  flex: 100vh;
}

aside {
  display: flex;
  width: 240px;
  /* background-color: #aaa; */
}

header {
  line-height: 1.5;
}
</style>
