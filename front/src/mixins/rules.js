//add form validation rules here
export default {
    data() {
        return {
            requiredRules: [
                value => !!value || "Required.",
            ],
            usernameRules: [
                value => !!value || "Username is required.",
                value => (value && value.length > 3) || "Username must be more than 3 characters long."
            ],
            passwordRules: [
                value => !!value || "Password is required.",
                value => (value && value.length > 5) || "Password must be more than 5 characters long."
            ],
            // TODO: INSERT EMAIL RULES
            emailRules: [
                value => !!value || "Email address is required.",
                // !INSERT REGEX FOR EMAIL RULE, SPENCER'S GOT THIS COVERED! 
                // value => 
            ],
        }
    }
};
