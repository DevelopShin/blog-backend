var home = new Vue({
  delimiters: ["[[", "]]"],
  el: "#page-top",
  data: {
    postList: [],
    tag: "",
    category: "",
  },
  created() {
    const param = new URL(location).searchParams;
    this.category = param.get("category");
    this.tag = param.get("tag");

    this.fetchPostList();
  },

  methods: {
    fetchPostList() {
      let url = "";
      if (this.category) url = "/api/post/list?category=" + this.category;
      else if (this.tag) url = "/api/post/list?tag=" + this.tag;
      else url = "/api/post/list/";
      axios
        .get(url)
        .then((res) => {
          this.postList = res.data;
        })
        .catch((err) => {
          alert("sorry!!, server error");
        });
    },

    keywordSearch(cate = "", tag = "") {
      if (cate) location.href = `?category=${cate}#blog-post`;
      else if (tag) location.href = `?tag=${tag}#blog-post`;
      else return;
    },
  },
});
