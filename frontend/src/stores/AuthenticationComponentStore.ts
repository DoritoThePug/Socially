import { defineStore } from "pinia";

export const useAuthenticationComponentStore = defineStore(
  "authenticationComponentStore",
  {
    state: () => ({
      isAuthenticationComponentOpen: false,
      isSignUpComponentOpen: false,
      isAccountInfoComponentOpen: false,
    }),
    actions: {
      toggleAuthenticationComponent() {
        this.isAuthenticationComponentOpen =
          !this.isAuthenticationComponentOpen;
        this.isSignUpComponentOpen = false;
        this.isAccountInfoComponentOpen = false;
      },
      toggleSignUpComponent() {
        this.isSignUpComponentOpen = !this.isSignUpComponentOpen;
        this.isAuthenticationComponentOpen = false;
        this.isAccountInfoComponentOpen = false;
      },
      navBarToggle() {
        if (this.isAuthenticationComponentOpen || this.isSignUpComponentOpen) {
          this.isAuthenticationComponentOpen = false;
          this.isSignUpComponentOpen = false;
        } else {
          this.toggleAuthenticationComponent();
        }
      },
      toggleAccountInfoComponent() {
        this.isAccountInfoComponentOpen = !this.isAccountInfoComponentOpen;
        this.isSignUpComponentOpen = false;
        this.isAuthenticationComponentOpen = false;
      },
    },
  }
);
