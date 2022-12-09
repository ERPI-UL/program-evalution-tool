import { defineStore } from "pinia";
import { account } from '@/plugins/appwrite';
import { useAlertStore } from '@/stores/AlertStore';

export const useUserStore = defineStore("UserStore", {
    state: () => {
        return {
            userData: null,
            isLogged: false,
        };
    },
    actions: {
        loginUser(email, password) {
            account.createEmailSession(email, password).then((user) => {
                this.userData = user;
                this.isLogged = true;
                this.router.push({ name: "Programs" });
            }).catch((error) => {
                console.log(error);
                const useAlert = useAlertStore()
                useAlert.addAlert("Problème lors de l'authentification. Attention à ne pas faire d'erreur dans le mot de passe 😅", "error", 4000)
            });
        },
        async checkLogin() {
            try {
                const response = await appwrite.account.get();
                this.userData = response;
                this.isLogged = true;
            } catch(err) {
                if (err == 'Error: Unauthorized'){
                    const useAlert = useAlertStore()
                    useAlert.addAlert("Vous n'êtes pas authorisé à accceder au système", "error", 4000)
                } else{
                    console.error(err)
                    const useAlert = useAlertStore()
                    useAlert.addAlert("Problème lors de l'authentification.", "error", 4000)
                };
                ;
            }
        },
        async checkUser() {
            account.get().then((user) => {
                this.userData = user;
                this.isLogged = true;
                // return promise
            }).catch((error) => {
                console.log(error);
                this.userData = null;
                this.isLogged = false;
                const useAlert = useAlertStore()
                useAlert.addAlert("Vous n'êtes pas connecté.", "info", 4000)
            })
        },
        registerUser(email, password, username) {
            account
                .create(ID.unique(), email, password, username)
                .then(
                    (response) => {
                        console.log(response);
                        account.createEmailSession(this.username, this.password);
                        this.router.push({ name: "Programs" })
                    },
                    (error) => {
                        console.log(error);
                    }
                ).catch((error) => {
                    console.log(error);
                    const useAlert = useAlertStore()
                    useAlert.addAlert("Problème lors de la creation de compte.", "error", 4000)
                });
        },
        async logout() {
            this.isLogged = false;
            this.userData= null;
            account.deleteSession('current');
            const useAlert = useAlertStore()
            useAlert.addAlert("Vous êtes déconnecté(e).", "success", 4000)
            this.router.push({ name: "Home" })
          },
          async accountRecovery(email){
            const useAlert = useAlertStore()
            account.createRecovery(email, 'localhost:3000').then((response)=>{
                console.log(response);
                useAlert.addAlert("Email de récupération envoyé.", "success", 4000)
            }).catch((error)=>{
                console.log(error);
                useAlert.addAlert("L'email de récupéartion n'a pas pas pu être envoyé.", "error", 4000)
            });
          }
    }
})