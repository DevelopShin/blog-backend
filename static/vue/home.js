var home = new Vue({
  delimiters: ["[[", "]]"],
  el: "#page-top",
  data: {
    postList: ["Hello Vue!"],
  },
  created() {
    this.fetchPostList();
  },
  methods: {
    fetchPostList() {
      axios
        .get("/api/post/list/")
        .then((res) => {
          this.postList = res.data;
        })
        .catch((err) => {
          console.log("fetch error result: ", err.response);
        });
    },
  },
});
