<template>
    <v-app-bar location="bottom">
        <v-text-field id="question" class="principalPrompter" prepend-icon="mdi-send" placeholder="Posez votre question"
            @keydown.enter="getResponse">
        </v-text-field>
    </v-app-bar>
</template>
<script>
import { mapWritableState } from 'pinia';
import { QAStore } from '@/stores/QA.store';
export default {
    computed: {
        ...mapWritableState(QAStore, ["QA"])
    },
    methods: {
        getResponse: function (event) {
            let val = document.getElementById("question").value;
            if (val.length > 0) {

                fetch("/api/response?question=" + val,
                    { method: "GET" })
                    .then(response => response.text())
                    .then(data => {
                        this.QA.push({ "question": val, "answer": data });
                        console.log(data);
                    });
            }
        }
    },
}
</script>
<style scoped>

</style>