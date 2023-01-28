<template>
    <v-card width="800" v-bind:text="question">
        <img width="24" height="24" src="@/assets/user.png">
        <v-btn v-on:click.prevent="waterfallDelete" icon="mdi-close"></v-btn>
    </v-card>
</template>
<script>
import { QAStore } from '@/stores/QA.store';
import { CurrentConvStore } from '@/stores/CurrentConv.store';
import { mapState, mapWritableState } from 'pinia';
export default {
    props: ['id', 'question'],
    computed: {
        ...mapState(CurrentConvStore, ["conv_id"]),
        ...mapWritableState(QAStore, ["QA"])
    },
    methods: {
        waterfallDelete: function (event) {
            fetch("/api/deleteMsg?q_id=" + this.id + "&conv_id=" + this.conv_id,
                { method: "DELETE" })
                .then(response => response.text())
                .then(data => { });
            fetch("/api/load_messages?conv_id=" + this.id,
                { method: "GET" })
                .then(response => response.json())
                .then(data => {
                    this.QA = [];
                    for (const res of data.results) {
                        this.QA.push(res);
                    }
                });
        }
    }

}
</script>
<style scoped>
img {
    /* lef */
}
</style>