<template>
  <Auth v-if="!isConnected"/>
  <div v-if="isConnected">
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
  </div>
</template>

<script>
import SideBar from './components/SideBar.vue'
import ChatInterface from './components/ChatInterface.vue'
import Auth from "../../FrontendVuetify/src/components/auth.vue";
import Prompt from './components/Prompt.vue';
import { UserStore } from './stores/User.store';
import { mapState } from 'pinia';
export default {
  data() {
    return {
      // isConnected: false
    };
  },
  computed:{
    ...mapState(UserStore, ['isConnected', 'user'])
  },
  // methods: {
  //   changeConnected(param){
  //     this.isConnected = param;
  //   }
  // },
  components: { Prompt, SideBar, ChatInterface, Auth }
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
