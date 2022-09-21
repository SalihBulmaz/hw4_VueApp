
<template>
    <v-form v-model="valid">
        <v-container>
            <v-row>
                <v-col cols="12" md="3">
                    <v-text-field v-model="username" :rules="nameRules" :counter="10" label="Username" required>
                    </v-text-field>
                </v-col>
                <v-col cols="12" md="6">
                    <v-text-field v-model="title" :rules="titleRules" :counter="150" label="Title" required>
                    </v-text-field>
                </v-col>
                <v-col  class="text-center" style="margin: auto 0;" cols="12" md="2">
                    <v-btn @click="addPost" color="#ff6600" style="color: white">Submit</v-btn>
                </v-col>
            </v-row>
        </v-container>
    </v-form>
</template>
  
<script>
export default {
    name: 'AddPost',
    emits: ['addpost'],
    data: () => ({
        valid: false,
        username: '',
        nameRules: [
            v => !!v || 'Username is required',
            v => v.length <= 10 || 'Username must be less than 10 characters',
        ],
        title: '',
        titleRules: [
            v => !!v || 'Title is required',
            v => v.length > 15 || 'Title must be at least 15 characters',
        ],
    }),
    methods: {
        addPost() {
            if(!this.valid) return;
            this.$emit('addpost', {username: this.username, title: this.title, createdAt: 0, votes: 0, commentsLength: 0});
        }
    }
}
</script>
  
<style>
</style>