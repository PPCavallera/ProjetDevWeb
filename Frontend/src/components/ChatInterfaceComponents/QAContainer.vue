<template>
    <div id="mainContainer">
        <QAElement v-for="qa in QA" v-bind:question="qa.question" v-bind:answer="qa.answer"></QAElement>
    </div>
</template>
<script>
import QAElement from './QAElement.vue';
import { mapState } from 'pinia';
import { QAStore } from '@/stores/QA.store';
export default {
    components: {
        QAElement
    },
    computed: {
        ...mapState(QAStore, ['QA'])
    },
}
</script>
<style>
#mainContainer{
    display: flex;
    flex-direction: column;
}

</style>