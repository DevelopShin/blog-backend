var postDetail = new Vue({
  delimiters: ["[[", "]]"],
  el: "#detail-sec",
  data: {
    post: {},
  },
  created() {
    let postId = location.pathname.split("/")[2];
    this.fetchPostDetail(postId);
  },
  methods: {
    fetchPostDetail(postId) {
      console.log("post detail: ", postId);
      axios
        .get(`/api/post/${postId}/`)
        .then((res) => {
          console.log("post detail: ", postId, res.data);

          this.post = res.data;
        })
        .catch((err) => {
          console.log("post detail fetch error : ", err.response);
        });
    },
  },
});
