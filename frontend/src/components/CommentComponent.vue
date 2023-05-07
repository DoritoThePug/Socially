<template>
    <div>
        <CommentModalComponent v-if="commentModalOpen" class="fixed z-10 inset-0" @close-modal="toggleCommentModal"/>

        <div class="flex flex-row">
            <img class="h-[38px] min-w-[38px] rounded-full mr-[16px] bg-black-75"/>
            <div>
                <div class="flex flex-row items-center">
                    <h5>Jamal Baking</h5>
                    <i class="fa-solid fa-circle text-[2px] text-black-50 mx-[4px]"></i>
                    <p class="text-[9px] text-black-50 align-middle">10 days ago</p>
                    <button class="ml-auto">
                        <i class="fa-solid fa-ellipsis text-[20px] text-black-75"></i>
                    </button>
                </div>
                <p class="mb-[8px]">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
                    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation
                    ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in
                    voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
                    proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>

                <div class="flex flex-row justify-between">
                    <button class="flex items-center space-x-[8px] group">
                        <!--          <i class="fa-solid fa-heart text-[24px] inline" :class="{-->
                        <!--            'text-primary-100': isLiked,-->
                        <!--            'text-black-75': !isLiked-->
                        <!--          }"></i>-->
                        <i class="fa-solid fa-heart text-[18px] text-black-75 group-hover:text-secondary-100"></i>
                        <p class="text-[12px] group-hover:text-secondary-100">123 likes</p>
                    </button>
                    <button class="flex items-center space-x-[8px] group" @click="toggleCommentModal">
                        <i class="fa-solid fa-comment text-[18px] text-black-75 group-hover:text-secondary-100"></i>
                        <p class="text-[12px] group-hover:text-secondary-100">7k comments</p>
                    </button>
                    <button class="flex items-center space-x-[8px] group">
                        <i class="fa-solid fa-share text-[18px] text-black-75 group-hover:text-secondary-100"></i>
                        <p class="text-[12px] group-hover:text-secondary-100">1k shares</p>
                    </button>
                    <button class="flex items-center space-x-[8px] group">
                        <i class="fa-solid fa-bookmark text-[18px] text-black-75 group-hover:text-secondary-100"></i>
                        <p class="text-[12px] group-hover:text-secondary-100">500 bookmarks</p>
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import CommentModalComponent from "@/components/CommentModalComponent.vue";

export default defineComponent({
    name: "CommentComponent",
    components : {
        CommentModalComponent
    },
    data() {
        return {
            commentModalOpen: false
        }
    },
    methods: {
        toggleCommentModal() {
            this.commentModalOpen = !this.commentModalOpen;
        }
    }
});
</script>

<style scoped>

</style>