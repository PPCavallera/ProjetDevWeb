import { defineStore, } from 'pinia'


export const UserStore = defineStore('User', {
  state: () => ({ isConnected: localStorage.isConnected, user: localStorage.user  }),
  getters: {
  },
})
