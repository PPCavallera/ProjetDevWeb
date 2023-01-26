<template>
    <div id="sidebar">
        <v-btn class="newConv">+</v-btn>
        <SideBarElements v-for="conv in convName" v-bind:name="conv"></SideBarElements>
    </div>
</template>
<script>
import SideBarElements from "./SideBarElements.vue"

export default {
    data() {
        return {
            convName: []
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