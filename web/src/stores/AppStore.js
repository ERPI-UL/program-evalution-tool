import {defineStore} from "pinia";

export const useAppStore = defineStore("AppStore",{
    state: () =>{
        return{
            selected_project: null,
            dashboard_tab: null,
        };
    }, 
    actions:{
        defineSelectedProject(projid){
            this.selected_project = projid;
        },
        defineSelectedWp(wpid){
            this.dashboard_tab = wpid;
        }
    }
})

