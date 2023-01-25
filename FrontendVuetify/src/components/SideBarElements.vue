<template>
    <div class="conversation">
        <v-btn class="convBtn">
            {{ name }}
        </v-btn>
    </div>
</template>
<script>
export default {
    props: ["name"],

}
</script>
<style>
.convBtn{
    width:220px;
    margin-left: 15px;
    margin-right: 15px;
}
</style>