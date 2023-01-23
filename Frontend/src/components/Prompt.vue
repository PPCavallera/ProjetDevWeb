<template>
    <form id='prompter'>
        <input type="text" id="question" name="question">
        <button v-on:click.prevent="getResponse" type="submit">Test</button>
    </form>
</template>
<script>
import { mapWritableState } from 'pinia';
import { QAStore } from '@/stores/QA.store';
export default {
    computed: {
        ...mapWritableState(QAStore, ['questions', 'answers'])
    },
    methods: {
        getResponse: function (event) {
            let val = document.getElementById("question").value;
            if (val.length > 0) {
                this.questions.push();
                fetch("/api/response?question=" + val,
                    { method: "GET" })
                    .then(response => response.text())
                    .then(data => {
                        this.answers.push(data);
                        console.log(data);
                    });
            }
        }
    },
}
</script>
<style>

</style>