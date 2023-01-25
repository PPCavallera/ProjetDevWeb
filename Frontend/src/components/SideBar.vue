<template>
    <div id="sidebar">
        <Conversation v-for="conv in convName" v-bind:name="conv"></Conversation>
    </div>
</template>
<script>
import Conversation from "./SideBarComponents/Conversation.vue"

export default {
    data() {
        return {
            convName: ["name1", "name2", "name3"]
        }
    },
    components: {
        Conversation
    }
}
</script>
<style>
#sidebar {
    background-color: rgb(37, 61, 48);
    position: sticky;
    flex: 1;
    height: 90vh;
    display: flex;
    flex-direction: column;
    width: 100vh;
}
</style>