<template>
    <div class="element">
        <div class="Q">
            <Question v-bind:id="question.id" v-bind:question="question.content"></Question>
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
/* .element {
    display: flex;
    flex-direction: column;
    margin-left: 15vh;
    margin-right: 15vh;
    width:7 0%;
} */
.Q {
    display: flex;
    justify-content: flex-end;
    padding: 15px;
}

.A {
    display: flex;
    justify-content: flex-start;
    padding: 15px;
}
</style>