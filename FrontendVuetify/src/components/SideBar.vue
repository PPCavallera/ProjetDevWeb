<template>
    <v-navigation-drawer permanent left app>
        <template v-slot:prepend>
            <v-list-item>
                <v-list-item-title :style="{
                    'text-align': 'center'
                }">{{ this.user }}</v-list-item-title>
            </v-list-item>
        </template>
        <v-divider></v-divider>
        <v-btn class="newConv" @click="convDialog = true">+</v-btn>
        <SideBarElements v-for="conv in convName" v-bind:id="conv.conv_id" v-bind:name="conv.conv_name"
            v-on:delete="refreshConvListAfterDelete" v-on:update="refreshConvListAfterUpdate">
        </SideBarElements>
        <template v-slot:append>
            <v-divider></v-divider>
            <div class="pa-2">
                <v-btn block @click="logout" >
                    Se déconnecter
                </v-btn>
            </div>
        </template>
    </v-navigation-drawer>
    <v-dialog v-model="convDialog" max-width="500px">
        <v-card>
            <v-card-title>
                Enter the conversation name
            </v-card-title>
            <v-card-text>
                <v-text-field v-model="newConvName" placeholder="Type Something" @keypress.enter="addConv" />
            </v-card-text>
            <v-card-actions>
                <v-btn color="primary" text @click="addConv">
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
import SideBarElements from "./SideBarElements.vue"
import { mapState, mapWritableState } from 'pinia';
import { UserStore } from '@/stores/User.store';
export default {
    data() {
        return {
            convName: [],
            convDialog: false,
            newConvName: ""
        }
    },
 
    created() {
        fetch("/api/conversations?user=" + this.user,
            { method: "GET" })
            .then(response => response.json())
            .then(data => {
                for (let res of data.results) {
                    this.convName.push({ "conv_id": res.conv_id, "conv_name": res.conv_name });
                }
            });
    },
    computed: {
        ...mapWritableState(UserStore, ["user"]),

    },
    methods: {
        logout() {
            localStorage.clear()
            location.reload()
        },

        refreshConvListAfterDelete(id) {
            for (let i = 0; i < this.convName.length; i++) {
                if (this.convName[i].conv_id === id) {
                    this.convName.splice(i, 1);
                }
                console.log(this.convName[0].conv_id)
            }
        },
        refreshConvListAfterUpdate(id, newConv_name) {
            for (let i = 0; i < this.convName.length; i++) {
                if (this.convName[i].conv_id === id) {
                    this.convName[i].conv_name = newConv_name
                }
                console.log(this.convName[0].conv_id)
            }
        },
        addConv() {
            if (this.newConvName != "") {
                fetch("/api/conversations?user=" + this.user + "&conv_name=" + this.newConvName,
                    {
                        method: "POST"
                    })
                    .then(response => response.json())
                    .then(data => {
                        this.convName.push({ "conv_id": data.conv_id, "conv_name": data.conv_name });

                    });
                this.convDialog = false
                this.newConvName = ""
            }
        },

    },

    components: {
        SideBarElements
    }
}
</script>
<style scoped>
.newConv {
    width: 220px;
    font-size: larger;
    margin-left: 15px;
    margin-right: 15px;
}
</style>