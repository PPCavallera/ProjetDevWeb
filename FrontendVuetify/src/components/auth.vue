<template>
    <div class="box">
        <h1>Se connecter</h1>
        <form @submit.prevent="login">
            <input v-model="email" placeholder="Email" required>
            <input v-model="password" type="password" placeholder="Mot de passe" required>
            <input type="submit" value="Submit">
        </form>
        <span>Pas encore de compte ? <a href="/register">S'inscrire</a> </span>
    </div>
</template>


<script>
export default {
    data() {
        return {
            password: "",
            email: ""
        };
    },
    methods: {
        login() {
            fetch("/login", {
                method: "POST",
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({email: this.email, password: this.password })
            })
                .then(response => response.text())
                .then(data => {
                    console.log(data);
                });
        }

    }
};
</script>