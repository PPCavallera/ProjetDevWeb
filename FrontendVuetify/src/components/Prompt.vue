<template>
    <v-app-bar location="bottom">
        <v-text-field id="question" class="principalPrompter" prepend-icon="mdi-send" placeholder="Posez votre question"
            @keydown.enter="getResponse">
        </v-text-field>
    </v-app-bar>
</template>
<script>
import { mapWritableState, mapState } from 'pinia';
import { QAStore } from '@/stores/QA.store';
import { CurrentConvStore } from '@/stores/CurrentConv.store';
export default {
    computed: {
        ...mapWritableState(QAStore, ["QA"]),
        ...mapState(CurrentConvStore, ["conv_id"])
    },
    methods: {
        getResponse: function (event) {
            let val = document.getElementById("question").value;
            if (val.length > 0) {

                fetch("/api/response?question=" + val + "&conv_id=" + this.conv_id,
                    { method: "GET" })
                    .then(response => response.text())
                    .then(data => {
                        this.QA.push({ "question": val, "answer": data });
                        console.log(data);
                    });
                document.getElementById("question").value = "";
            }
        }
    },
}
</script>
<style scoped>

</style>