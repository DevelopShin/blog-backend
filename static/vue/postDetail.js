var postDetail = new Vue({
  delimiters: ["[[", "]]"],
  el: "#detail-sec",
  data: {
    post: {},
    nextPost: {},
    prevPost: {},
    cateList: [],
    tagList: [],
    comments: [],
    commentValue: "",
    nickname: "",
  },

  created() {
    let postId = location.pathname.split("/")[2];
    this.fetchPostDetail(postId);
    this.fetchCateTagList();
  },
  methods: {
    fetchPostDetail(postId) {
      axios
        .get(`/api/post/${postId}/`)
        .then((res) => {
          this.post = res.data.post;
          this.nextPost = res.data.nextPost;
          this.prevPost = res.data.prevPost;
          this.comments = res.data.comments;
        })
        .catch((err) => {
          alert("sorry!!, server error");
        });
    },

    fetchCateTagList() {
      axios
        .get(`/api/post/catetag/`)
        .then((res) => {
          this.cateList = res.data.cateList;
          this.tagList = res.data.tagList;
        })
        .catch((err) => {
          alert("sorry!!, server error");
        });
    },

    keywordSearch(cate = "", tag = "") {
      if (cate) location.href = `/?category=${cate}#blog-post`;
      else if (tag) location.href = `/?tag=${tag}#blog-post`;
      else return;
    },
    onSubmitForm() {
      axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
      axios.defaults.xsrfCookieName = "csrftoken";
      let form = new FormData();
      form.set("post", this.post?.id);
      form.set("content", this.commentValue);
      form.set("nickname", this.nickname);

      axios
        .post("/api/post/comment/add/", form)
        .then((res) => {
          if (res.data.id) {
            this.comments.push(res.data);
            this.commentValue = "";
          }
        })
        .catch((error) => {
          console.log(error);
          alert("Please, try again");
        });
    },
  },
});
