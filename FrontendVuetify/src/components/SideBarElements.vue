<template>
    <div class="conversation">
        <v-btn v-on:click.prevent="loadConversation" class="convBtn">
            {{ name }}
        </v-btn>
        <v-btn class="convUpdate" >
            <v-icon>mdi-rename-box</v-icon>
        </v-btn>
        <v-btn class="convUpdate" >
            <v-icon>mdi-delete</v-icon>
        </v-btn>

    </div>
</template>
<script>
import { mapWritableState } from 'pinia';
import { CurrentConvStore } from '@/stores/CurrentConv.store';
import { QAStore } from '@/stores/QA.store';
export default {
    computed: {
        ...mapWritableState(CurrentConvStore, ['conv_id']),
        ...mapWritableState(QAStore, ['QA'])
    },
    props: ["id", "name"],
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