<template>
  <v-app>
    <v-main>
      <v-container>
        {{hackernews}}
        <NavBar />
        <AddPost @addpost="addPost" />
        <PostGrid :posts="posts" />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import PostGrid from './components/PostGrid.vue';
import NavBar from './components/NavBar.vue';
import AddPost from './components/AddPost.vue';
import hackernews from './hackernews.json';
export default {
  name: 'App',
  components: {
    PostGrid,
    NavBar,
    AddPost
  },
  data: () => ({
    posts: [],
  }),
  async mounted() {
    await this.fetchPosts();
  },
  methods: {
    async fetchPosts() {
      const usernames = [
        "Authenticyc",
        "Bondusine",
        "Breakinst",
        "ChampionHeaven",
        "ChattyFox",
        "EliteSleek",
        "Enhiumex",
        "Epitoolus",
        "Filogerse",
        "GlaceBorg",
      ];
      try {
        const response = await fetch('https://jsonplaceholder.typicode.com/posts');
        if (!response.ok) {
          const message = `An error has occured: ${response.status} - ${response.statusText}`;
          throw new Error(message);
        }
        const data = await response.json();
        this.posts = data.map(post => {
          post.votes = Math.floor(Math.random() * 250);
          post.createdAt = Math.floor(Math.random() * 20);
          post.commentsLength = Math.floor(Math.random() * 100);
          post.username = usernames[post.userId - 1];
          post.link = hackernews[post.id];
          return post;
        });
      } catch (error) {
        console.error(error);
      }
    },
    addPost(post) {
      this.posts.push(post);
      console.log(this.posts[this.posts.length - 1])
    }
  }
};
</script>

<style>
</style>