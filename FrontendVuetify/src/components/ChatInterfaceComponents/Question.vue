<template>
    <v-card width="800" v-bind:text="question" >
        <img width="24" height="24" src="@/assets/user.png">
    </v-card>
</template>
<script>
export default{
    props:['question']
}
</script>
<style scoped>
img{
    /* lef */
}
</style>