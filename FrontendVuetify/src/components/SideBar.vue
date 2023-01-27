<template>
    <v-navigation-drawer permanent left app>
        <template v-slot:prepend>
            <v-list-item>
                <v-list-item-title :style="{
                    'text-align': 'center'}">{{ this.user }}</v-list-item-title>
            </v-list-item>
        </template>
        <v-divider></v-divider>
        <v-btn class="newConv">+</v-btn>
        <SideBarElements v-for="conv in convName" v-bind:name="conv"></SideBarElements>
        <template v-slot:append>
            <v-divider></v-divider>
            <div class="pa-2">
                <v-btn block @click="logout">
                    Se déconnecter
                </v-btn>
            </div>
        </template>
    </v-navigation-drawer>
</template>

<script>
import SideBarElements from "./SideBarElements.vue"
import { mapWritableState } from 'pinia';
import { UserStore } from '@/stores/User.store';
export default {
    data() {
        return {
            convName: ["test", "test"]
        }
    },
    created() {
        fetch("/api/conversations",
            { method: "GET" })
            .then(response => response.json())
            .then(data => {
                console.log(data.results);
                for (let res of data.results) {
                    console.log(res);
                    this.convName.push(res.conv_name);
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
        }
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