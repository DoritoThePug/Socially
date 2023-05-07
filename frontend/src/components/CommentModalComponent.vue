

<template>
<div class="w-full h-full backdrop-blur-md flex place-content-center">
    <div class="flex flex-col min-w-[500px] p-[32px] bg-white rounded-[25px] self-center">
        <div class="flex flex-row mb-[16px] content-start">
            <div class="rounded-full bg-black-75 w-[42px] h-[42px] mr-[8px]"></div>
            <div>
                <h4 class="text-[22px] text-black-100 leading-[22px]">Jamal Baking</h4>
                <p class="text-[9px] text-black-50">10 days ago</p>
            </div>
            <button class="ml-auto h-fit" @click="$emit('close-modal')">
                <i class="fa-solid fa-x text-[16px]"></i>
            </button>
        </div>

        <p class="mb-[32px]">Check out my cookies</p>

        <div class="h-[1px] w-full bg-black-50 mb-[32px]"></div>

        <textarea class="resize-none overflow-hidden mb-[32px] min-h-[32px] max-h-full w-full focus:outline-none" placeholder="Reply to Jamal Baking's post" @input="adjustTextareaHeight" ref="textarea" maxlength="280"></textarea>

        <button class="bg-primary-100 h-[39px] w-[140px] rounded-[5px] inline-block ml-auto">
            <h5 class="text-white">Comment</h5>
        </button>
    </div>
</div>
</template>

<script lang="ts">
import {defineComponent, defineEmits} from 'vue'

export default defineComponent({
    name: "CommentModalComponent",
    emits: ['close-modal'],
    methods: {
        adjustTextareaHeight() {
            const textarea = this.$refs.textarea as HTMLTextAreaElement;

            textarea.style.height = 'auto';
            textarea.style.height = textarea.scrollHeight + 'px';
        },
        test() {
            this.$emit('close-modal')
        }
    },
})
</script>

<style scoped>

</style>