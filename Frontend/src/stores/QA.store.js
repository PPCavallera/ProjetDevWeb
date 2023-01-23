import { defineStore, } from 'pinia'


export const QAStore = defineStore('QA', {
  state: () => ({ questions: [], answers: [] }),
  getters: {
  },
})
