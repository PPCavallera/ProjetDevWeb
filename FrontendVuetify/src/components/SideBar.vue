<template>
    <v-navigation-drawer absolute permanent left>
        <template v-slot:prepend>
            <v-list-item>
                <v-list-item-title>{{ this.user }}</v-list-item-title>
                <v-list-item link @click="logout">Se déconnecter</v-list-item>
            </v-list-item>
        </template>
        <v-btn class="newConv">+</v-btn>
        <SideBarElements v-for="conv in convName" v-bind:id="conv.conv_id" v-bind:name="conv.conv_name"></SideBarElements>
    </v-navigation-drawer>
</template>

<script>
import SideBarElements from "./SideBarElements.vue"
import { mapWritableState } from 'pinia';
import { UserStore } from '@/stores/User.store';
export default {
    data() {
        return {
            convName: []
        }
    },
    created() {
        fetch("/api/conversations?user=" + this.user,
            { method: "GET" })
            .then(response => response.json())
            .then(data => {
                console.log(data.results);
                for (let res of data.results) {
                    console.log(res);
                    this.convName.push({"conv_id":res.conv_id, "conv_name":res.conv_name});
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