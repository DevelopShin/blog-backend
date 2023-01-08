var postDetail = new Vue({
  delimiters: ["[[", "]]"],
  el: "#detail-sec",
  data: {
    post: {},
    cateList: [],
    tagList: [],
  },
  created() {
    let postId = location.pathname.split("/")[2];
    this.fetchPostDetail(postId);
    this.fetchCateTagList();
  },
  methods: {
    fetchPostDetail(postId) {
      console.log("fetchPostDetail: ", postId);
      axios
        .get(`/api/post/${postId}/`)
        .then((res) => {
          console.log("fetchPostDetail: ", postId, res.data);

          this.post = res.data;
        })
        .catch((err) => {
          console.log("fetchPostDetail error : ", err.response);
        });
    },
    fetchCateTagList() {
      axios
        .get(`/api/post/catetag/`)
        .then((res) => {
          console.log("fetchCateTagList: ", res.data);
          this.cateList = res.data.cateList;
          this.tagList = res.data.tagList;
        })
        .catch((err) => {
          console.log("fetchCateTagList error : ", err.response);
        });
    },
  },
});
