import {defineStore} from "pinia";

export const useAlertStore = defineStore("AlertStore",{
    state: () =>{
        return{
            alerts: [],
        };
    }, 
    actions:{
        removeAlert(msgid) {
            const objWithIdIndex = this.alerts.findIndex((obj) => obj.id === msgid);
            if (objWithIdIndex > -1) {
                this.alerts.splice(objWithIdIndex, 1);
              }
            
        },
        addAlert(msg, type = "warning", duration = 0) {
            var min = Math.ceil(100);
            var max = Math.floor(999);
            var randomid = Math.floor(Math.random() * (max - min)) + min;
            var alert = {
                id: randomid,
                msg: msg,
                type: type == null ? "warning" : type,
                duration: duration == null ? 0 : duration,
            };
            this.alerts.push(alert);
        },
    }
})

