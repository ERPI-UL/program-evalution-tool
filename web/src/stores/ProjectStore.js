import {defineStore} from "pinia";
import {useAlertStore} from '@/stores/AlertStore';
import programs from "@/data/projects.json";


export const useProjectStore = defineStore("ProjectStore",{
    state : () =>{
        return{
            projects: [],
        };
    }, 
    actions: {
        fetchProject(){
            // get project where the user is enrolled
            try {
                this.projects = programs;
            } catch (error) {
                console.log(error);
                const useAlert = useAlertStore()
                useAlert.addAlert("Problème dans la récupération de la liste de projet", "error", 4000)
            }
        },
    }
})