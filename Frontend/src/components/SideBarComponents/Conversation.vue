<template>
    <div class="conversation">
        <label class="convName">{{ name }}</label>
    </div>
</template>
<script>
export default {
    props: ["name"],

}
</script>
<style>
.conversation {
    display: flex;
    background-color: rgb(67, 67, 67);
    height: 25px;
    text-align: center;
    justify-content: space-between;
    border-radius: 10px;
    padding: 10px;
    color: white;
}

.convName {
    margin: auto;
}
</style>