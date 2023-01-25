<template>
    <div class="element">
        <div class="Q">
            <Question v-bind:text="question"></Question>
        </div>
        <div class="A">
            <Answer v-bind:text="answer"></Answer>
        </div>
    </div>
</template>
<script>
import Answer from './Answer.vue';
import Question from './Question.vue';
export default {
    props: ["question", "answer"],
    components: {
        Answer, Question
    }
}
</script>
<style scoped>
.element {
    display: flex;
    flex-direction: column;
    width: 100vh;
}
.Q{
    display: flex;
    justify-content: flex-end;
}
.A{
    display: flex;
    justify-content: flex-start;
}
</style>