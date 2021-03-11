import Vue from 'vue';
import axios from 'axios';

let config = {
    baseURL: process.env.API,
    timeout: 10000,
    headers: {
        "Content-Type": "application/json",
    }
}
const parking = axios.create(config)

parking.interceptors.response.use(undefined, function(error) {
    return new Promise(function(resolve, reject) {
        if(error.response) {
            if (error.response.includes('TOKEN') || error.response.statusCode === 403) {
                this.$router.push('/logout');
                resolve();
            } else {
                reject();
            }
        }
    })
});

parking.interceptors.request.use(function(config) {
    let token = this.$session.get('token') ? this.$session.get('token') : "";
    if(token) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
});

Vue.use(parking);

export default parking;