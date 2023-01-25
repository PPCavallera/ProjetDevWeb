<template>
    <v-form>
        <v-text-field id="question" class="principalPrompter">
            <img width="24" height="24" src="@/assets/send.png">
        </v-text-field>
        <button class="sendButton" v-on:click.prevent="getResponse" type="submit"></button>

    </v-form>
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
<style>
.sendButton{
    width: 0;
    height: 0;
}
</style>