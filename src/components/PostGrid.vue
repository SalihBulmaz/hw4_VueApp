<template>
  <v-container>
    <ol :start="currentPage * 10 +1" class="post_grid">
      <li v-for="post in sortedPosts.slice(currentPage * 10, currentPage * 10 + 10)" :key="post.id">
        <div class="title"><v-icon small class="upvote" @click="upvote(post.id)">mdi-arrow-up-thick</v-icon><a :href="post.link">{{post.title}}</a></div>
        <p><v-icon small class="hidden" @click="upvote(post.id)">mdi-plus</v-icon>{{post.votes}} points by {{post.username}} | {{post.createdAt}} hours ago | hide | {{post.commentsLength}} comments
          <span v-show="user.votedPostIds.includes(post.id)" @click="unvote(post.id)" class="unvote">| unvote </span>
        </p>
      </li>
    </ol>
    <div class="pagination">
      <v-btn dense depressed color="secondary" v-for="pageIdx in pages" :key="pageIdx" class="mx-1"
        @click="currentPage = pageIdx">
        {{pageIdx + 1}}
      </v-btn>
    </div>
  </v-container>
</template>

<script>
export default {
  name: 'PostGrid',
  props: { posts: Array },
  data() {
    return {
      currentPage: 0,
      user: {
        name: '',
        password: '',
        votedPostIds: []
      }

    }
  },
  computed: {
    sortedPosts() {
      return [...this.posts].sort(function (a, b) { return b.votes - a.votes });
    },
    pages() {
      let result = [];
      let pageIdx = 0;
      for (var i = 0; i < this.sortedPosts.length; i += 10) {
        result.push(pageIdx++);
      }
      return result;
    }
  },
  methods: {

    upvote(postId) {
      if (this.user.votedPostIds.includes(postId)) return;
      this.posts[postId - 1].votes += 1;
      this.user.votedPostIds.push(postId);
    },
    unvote(postId) {
      if (this.posts[postId - 1].votes == 0) return;
      this.posts[postId - 1].votes -= 1;
      this.user.votedPostIds = this.user.votedPostIds.filter(id => id != postId);
    },
  }
}
</script>

<style scoped>
.post_grid {
  font-size: .9rem;
}

.title {
  margin: 0;
  padding: 0;
}

a {
  text-decoration: none;
  color: black!important;
}

.upvote {
  cursor: pointer;
}

.unvote {
  cursor: pointer;
}

.pagination {
  position: relative;
  margin: auto
}
.hidden {
  visibility:hidden;
}
</style>