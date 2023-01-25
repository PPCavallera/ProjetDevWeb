<template>
    <div class="answer">
        <label>{{ text }}</label>
    </div>
</template>
<script>
export default {
    props: ["text"]
}
</script>
<style scoped>
.answer {
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