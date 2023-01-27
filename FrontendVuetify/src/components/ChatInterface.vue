<template>
    <v-container class="mainContainer">
        <QAElement v-for="qa in QA" v-bind:question="qa.question" v-bind:answer="qa.answer"/>
        <!-- <Answer v-for="qa in QA" v-bind:answer="qa.answer" /> -->
    </v-container>
</template>
<script>
import QAElement from './ChatInterfaceComponents/QAElement.vue';
// import Answer from './ChatInterfaceComponents/Answer.vue';
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