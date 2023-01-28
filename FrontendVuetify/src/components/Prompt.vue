<template>
    <v-app-bar location="bottom">
        <v-text-field id="question" placeholder="Type Something" @keypress.enter="getResponse" />
        <v-btn icon class="ml-4" @click="getResponse"><v-icon>mdi-send</v-icon></v-btn>

    </v-app-bar>
</template>
<script>
import { mapWritableState, mapState } from 'pinia';
import { QAStore } from '@/stores/QA.store';
import { CurrentConvStore } from '@/stores/CurrentConv.store';
export default {
    computed: {
        ...mapWritableState(QAStore, ["QA"]),
        ...mapState(CurrentConvStore, ["conv_id"]),
    },
    methods: {
        getResponse: function (event) {
            let val = document.getElementById("question").value;
            if (val.length > 0) {
                fetch("/api/response?question=" + val + "&conv_id=" + this.conv_id,
                    { method: "GET" })
                    .then(response => response.json())
                    .then(data => {
                        this.QA.push({ "question": { "id": data.question_id, "content": val }, "answer": data.answer });
                        console.log(data.answer);
                    });
                document.getElementById("question").value = "";
            }
        }
    },
}
</script>
<style scoped>

</style>