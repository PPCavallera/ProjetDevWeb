<template>
    <v-card width="400" class="mx-auto mt-5">
        <v-card-title>
            <h2>Connexion</h2>
        </v-card-title>
        <v-card-text>
            <v-form>
                <v-text-field v-model="username" label="Utilisateur" prepend-icon="mdi-account-circle" />
                <v-text-field v-model="password" type="password" label="Password" prepend-icon="mdi-lock" />
            </v-form>
        </v-card-text>
        <v-card-actions>
            <v-btn color="success" @click="register">S'inscrire</v-btn>
            <v-btn color="info" @click="login">Se connecter</v-btn>
        </v-card-actions>
    </v-card>
    <v-snackbar v-model="snackbar">
        {{ message }}
            <v-btn color="pink" @click="snackbar = false">
                Close
            </v-btn>
    </v-snackbar>
</template>


<script>
import { mapWritableState } from 'pinia';
import { UserStore } from '@/stores/User.store';
export default {
    data() {
        return {
            password: "",
            username: "",
            message: "",
            snackbar: false
        };
    },
    computed: {
        ...mapWritableState(UserStore, ["isConnected", "user"]),

    },
    methods: {
        login() {
            if (this.username == "" || this.password == "") {
                this.message = "Required fields"
                this.snackbar = true
            }
            else {
                fetch("/login", {
                    method: "POST",
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ username: this.username, password: this.password })
                })
                    .then(response => response.json())
                    .then(data => {
                        if (data["isConnected"]) {
                            localStorage.isConnected = data["isConnected"]
                            localStorage.user = data["user"]
                            this.isConnected = data["isConnected"]
                            this.user = data["user"]
                        }
                        else {
                            this.message = data["message"]
                            this.snackbar = true
                        }
                    });
            }
        },

        register() {
            if (this.username == "" || this.password == "") {
                this.message = "Required fields"
                this.snackbar = true
            }
            else {
                fetch("/register", {
                    method: "POST",
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ username: this.username, password: this.password })
                })
                    .then(response => response.json())
                    .then(data => {
                        this.message = data["message"]
                        this.snackbar = true
                    });
            }
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