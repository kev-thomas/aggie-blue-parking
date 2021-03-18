import Vue from 'vue';
import jwt from 'jsonwebtoken';

let encodeOptions = {
    algorithm: 'HS256',
    expiresIn: '1h'
}

let decodeOptions = {
    issuer: 'NeuralCog'
}

let key = "secret"

const encode = function(payload) {
    return jwt.sign(payload, key, encodeOptions);
}

const decode = function(token) {
    let decoded;
    try {
        decoded = jwt.verify(token, key, decodeOptions, function(error, payload) {
            if(error) {
                throw error;
            }
            else {
                return payload;
            }
        });
    }
    catch(e) {
        decoded = {'TOKEN': e.msg}
        this.$router.push('/logout');
    }
    return decoded;
}

let token = {
    encode,
    decode
};

Vue.use(token);

export default token;
