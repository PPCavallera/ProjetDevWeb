<template>
    <div id="mainInterface">
        <QAContainer></QAContainer>
    </div>
</template>
<script>
import QAContainer from './ChatInterfaceComponents/QAContainer.vue';

export default {
    props: ["question", "answers"],
    components: { QAContainer }
}
</script>
<style>
#mainInterface {
    background-color: rgb(44, 44, 44);
    display: flex;
    overflow-x: hidden;
    overflow-y: auto;
    text-align: center;
    height: 90vh;
}
</style>