import { defineStore } from "pinia";

export const useAuthenticationComponentStore = defineStore("authenticationComponentStore", {
    state: () => ({
        isAuthenticationComponentOpen: false,
        isSignUpComponentOpen: false,
        isAccountDetailsComponentOpen: false
    }),
    actions: {
        toggleAuthenticationComponent() {
            this.isAuthenticationComponentOpen = !this.isAuthenticationComponentOpen
            this.isSignUpComponentOpen = false
            this.isAccountDetailsComponentOpen = false
        },
        toggleSignUpComponent() {
            this.isSignUpComponentOpen = !this.isSignUpComponentOpen
            this.isAuthenticationComponentOpen = false
            this.isAccountDetailsComponentOpen = false
        },
        navBarToggle() {
            if (this.isAuthenticationComponentOpen || this.isSignUpComponentOpen) {
                this.isAuthenticationComponentOpen = false
                this.isSignUpComponentOpen = false
            } else {
                this.toggleAuthenticationComponent()
            }
        },
        toggleAccountDetailsComponent() {
            this.isAccountDetailsComponentOpen = !this.isAccountDetailsComponentOpen
            this.isSignUpComponentOpen = false
            this.isAuthenticationComponentOpen = false
        }
    }
})