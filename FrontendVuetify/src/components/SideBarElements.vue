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
                    <v-btn icon="mdi-pen" @click="convDialog = true"></v-btn>
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

    <v-dialog v-model="convDialog" max-width="500px">
        <v-card>
            <v-card-title>
                Enter new conversation name
            </v-card-title>
            <v-card-text>
                <v-text-field v-model="newConvName" @keypress.enter="renameConv"></v-text-field>
            </v-card-text>
            <v-card-actions>
                <v-btn color="primary" text @click="renameConv">
                    Add
                </v-btn>
                <v-btn color="primary" text @click="convDialog = false">
                    Close
                </v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>
<script>
import { mapWritableState } from 'pinia';
import { CurrentConvStore } from '@/stores/CurrentConv.store';
import { QAStore } from '@/stores/QA.store';
export default {
    data: () => ({
        snackbar: false,
        convDialog: false,
        newConvName: ""
    }),
    computed: {
        ...mapWritableState(CurrentConvStore, ['conv_id']),
        ...mapWritableState(QAStore, ['QA'])
    },
    props: ["id", "name"],
    emits: ["delete", "update"],
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
        },
        renameConv() {
            fetch("/api/conversations?conv_id=" + this.id + "&conv_name=" + this.newConvName,
                {
                    method: "PUT"
                })
                .then(response => response.json())
                .then(data => {
                    console.log(data.message);
                });
            this.convDialog = false
            this.$emit('update', this.id, this.newConvName)
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