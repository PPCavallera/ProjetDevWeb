import { defineStore, } from 'pinia'


export const UserStore = defineStore('User', {
  state: () => ({ isConnected: false, user:'' }),
  getters: {
  },
})
