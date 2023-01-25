<template>
  <header></header>
  <main>
    <aside>
      <SideBar />
    </aside>
    <article>
      <ChatInterface />
      <div class="prompter">
        <Prompt />
      </div>
    </article>
  </main>
  <footer></footer>
</template>

<script>
import SideBar from './components/SideBar.vue'
import ChatInterface from './components/ChatInterface.vue'

import Prompt from './components/Prompt.vue';
export default {
  components: { Prompt, SideBar, ChatInterface }
}
</script>
<style scoped>
main {
  display: flex;
  flex-direction: row;
  /* flex: 100vh;
  width: 100vh;
  height: 100%; */

}

article {
  display: flex;
  flex-direction: column;
  width: 100%;
}

aside {
  display: flex;
  flex-direction: column;
  width: 250px;

}

header {
  line-height: 1.5;
}
</style> 
