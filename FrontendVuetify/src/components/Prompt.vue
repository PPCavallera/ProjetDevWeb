<template>
    <v-form class="formPrompt">
        <v-text-field id="question" class="principalPrompter">
            <img width="24" height="24" src="@/assets/send.png">
        </v-text-field>
        <button class="sendButton" v-on:click.prevent="getResponse" type="submit"></button>
    </v-form>
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
<style>
.sendButton {
    width: 0;
    height: 0;
}
</style>