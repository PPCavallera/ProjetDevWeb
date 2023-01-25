<template>
    <div class="question">
        <label>{{ text }}</label>
    </div>
</template>
<script>
export default {
    props: ["text"]
}
</script>
<style scoped>
.question {
    display: flex;
    background-color: rgb(67, 67, 67);
    flex-wrap: wrap;
    max-width: 75vh;
    justify-content: space-between;
    border-radius: 10px;
    padding: 5px;
    color: white;
    text-align: initial;
}
</style>