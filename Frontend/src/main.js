/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Components
// Composables
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'


// Plugins

const pinia = createPinia()

const app = createApp(App)

app.use(pinia)
app.mount('#app')
