<template>
  <v-app>
    <Auth v-if="!isConnected" />
    <div v-if="isConnected">
      <SideBar />
      <v-main fill-height>
        <ChatInterface />
        <Prompt />
      </v-main>
    </div>
  </v-app>
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

    };
  },
  computed: {
    ...mapState(UserStore, ['isConnected', 'user'])
  },
  components: { Prompt, SideBar, ChatInterface, Auth }
}
</script>
<style scoped>

</style> 
