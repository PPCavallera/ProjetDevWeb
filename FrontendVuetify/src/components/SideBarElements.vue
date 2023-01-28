<template>
    <v-container>
        <v-btn v-on:click.prevent="loadConversation" class="convBtn">
            {{ name }}
        </v-btn>
        <v-menu bottom left>
            <template v-slot:activator="{ props }">
                <v-btn icon="mdi-dots-vertical" v-bind="props"></v-btn>
            </template>
            <v-list>
                <v-list-item>
                    <v-btn icon="mdi-pen"></v-btn>
                    <v-btn icon="mdi-delete" @click="snackbar = true"></v-btn>
                </v-list-item>
            </v-list>
        </v-menu>
    </v-container>

    <v-snackbar v-model="snackbar">
        Do you want to delete "{{ name }}" ?
        <v-btn color="green" @click="deleteConv">
            Yes
        </v-btn>
        <v-btn color="pink" @click="snackbar = false">
            No
        </v-btn>
    </v-snackbar>
</template>
<script>
import { mapWritableState } from 'pinia';
import { CurrentConvStore } from '@/stores/CurrentConv.store';
import { QAStore } from '@/stores/QA.store';
export default {
    data: () => ({
        snackbar: false,
    }),
    computed: {
        ...mapWritableState(CurrentConvStore, ['conv_id']),
        ...mapWritableState(QAStore, ['QA'])
    },
    props: ["id", "name"],
    emits:["delete"],
    methods: {
        loadConversation: function (event) {
            console.log(this.id)
            fetch("/api/load_messages?conv_id=" + this.id,
                { method: "GET" })
                .then(response => response.json())
                .then(data => {
                    this.QA = [];
                    for (const res of data.results) {
                        this.QA.push(res);
                    }
                });
            this.conv_id = this.id;
        },
        deleteConv() {
            fetch("/api/conversations?conv_id=" + this.id,
                { method: "DELETE" })
                .then(response => response.json())
                .then(data => {
                    console.log(data.message);
                });
            this.snackbar = false
            this.$emit('delete', this.id)
        }
    },
    location: 'end',
}
</script>
<style>
.convBtn {
    width: 150px;
    /* margin-left: 5px; */
    margin-right: 5px;
}

.conversation {
    display: flex;
    flex-direction: row;

}

.convUpdate {
    max-width: 20px;
    margin-right: 5px;
}
</style>