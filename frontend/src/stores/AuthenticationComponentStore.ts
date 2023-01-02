import { defineStore } from "pinia";

export const useAuthenticationComponentStore = defineStore("authenticationComponentStore", {
    state: () => ({
        isAuthenticationComponentOpen: false,
        isSignUpComponentOpen: false,
    }),
    actions: {
        toggleAuthenticationComponent() {
            this.isAuthenticationComponentOpen = !this.isAuthenticationComponentOpen
            this.isSignUpComponentOpen = false
        },
        toggleSignUpComponent() {
            this.isSignUpComponentOpen = !this.isSignUpComponentOpen
            this.isAuthenticationComponentOpen = false
        }
    }
})