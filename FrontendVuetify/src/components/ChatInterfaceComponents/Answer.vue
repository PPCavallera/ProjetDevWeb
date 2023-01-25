<template>
    <v-card width="800" v-bind:text="answer">
        <img width="24" height="24" src="@/assets/cat.png">
    </v-card>
</template>
<script>
export default {
    props: ['answer']
}
</script>
<style>

</style>