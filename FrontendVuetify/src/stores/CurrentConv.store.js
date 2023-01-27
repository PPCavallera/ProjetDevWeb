import { defineStore, } from 'pinia'


export const CurrentConvStore = defineStore('CurrentConv', {
  state: () => ({ conv_id: -1, conv_name: ""}),
  getters: {
  },
})
