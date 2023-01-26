<template>
    <div class="box">
        <h1>Se connecter</h1>
        <form @submit.prevent="login">
            <input v-model="email" placeholder="Email" required type="email">
            <input v-model="password" type="password" placeholder="Mot de passe" required>
            <input type="submit" value="Submit">
        </form>
        <span>Pas encore de compte ? <a @click="register">S'inscrire</a> </span>
        <h1>{{ message }}</h1>
    </div>
</template>


<script>
export default {
    data() {
        return {
            password: "",
            email: "",
            message: ""
        };
    },
    methods: {
        login() {
            fetch("/login", {
                method: "POST",
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email: this.email, password: this.password })
            })
                .then(response => response.json())
                .then(data => {
                    this.$emit("isConnected", data["isConnected"]);
                    console.log(data);
                    if (data["isConnected"] == true) {
                        this.$emit("user", data["user"]);
                    }
                    this.message = data["message"];
                });
        },

        register() {
            fetch("/register", {
                method: "POST",
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email: this.email, password: this.password })
            })
                .then(response => response.json())
                .then(data => {
                    this.message = data["message"];
                });
        }

    }
};
</script>

<style scoped>
a {
    color: blue;
    text-decoration: underline;
}

a:hover {
    cursor: pointer;
}
</style>