<template>
    <v-card width="800" text="Vous parlez à une IA, ses réponses n'engagent en rien les développeurs de l'application web." prepend-icon="mdi-alert">
    </v-card>
    <QAElement v-for="qa in QA" v-bind:question="qa.question" v-bind:answer="qa.answer" />
</template>
<script>
import QAElement from './ChatInterfaceComponents/QAElement.vue';
import { mapState } from 'pinia';
import { QAStore } from '@/stores/QA.store';
export default {
    components: { QAElement },
    computed: {
        ...mapState(QAStore, ['QA'])
    },
}

</script>
<style>
.mainContainer {
    background-color: rgb(44, 44, 44);
    display: flex;
    flex-direction: column;
    overflow-x: hidden;
    overflow-y: auto;
    text-align: center;
    height: 90vh;
}
</style>