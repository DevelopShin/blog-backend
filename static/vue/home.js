var home = new Vue({
  delimiters: ["[[", "]]"],
  el: "#page-top",

  data: {
    postList: [],
    tag: "",
    category: "",
    totalPage: 1,
    currentPage: 1,
  },
  created() {
    const param = new URL(location).searchParams;
    this.category = param.get("category");
    this.tag = param.get("tag");

    this.fetchPostList();
  },

  computed: {
    pages() {
      pages = [];
      if (this.totalPage === 1) pages = [1];
      else if (this.totalPage === 2) pages = [1, 2];
      else if (this.totalPage === 3) pages = [1, 2, 3];
      else {
        if (this.currentPage === 1)
          pages = [
            this.currentPage,
            this.currentPage + 1,
            this.currentPage + 2,
          ];
        else if (this.currentPage === this.totalPage) {
          pages = [
            this.currentPage - 2,
            this.currentPage - 1,
            this.currentPage,
          ];
        } else
          pages = [
            this.currentPage - 1,
            this.currentPage,
            this.currentPage + 1,
          ];
      }
      return pages;
    },
  },
  methods: {
    fetchPostList(page = 1) {
      let url = "";
      if (this.category)
        url = `/api/post/list?page=${page}&category=${this.category}`;
      else if (this.tag) url = `/api/post/list?page=${page}&tag=this.tag`;
      else url = `/api/post/list/?page=${page}`;
      axios
        .get(url)
        .then((res) => {
          this.postList = res.data.postList;
          this.totalPage = res.data.totalPage;
          this.currentPage = res.data.currentPage;
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

    pagenation(page) {
      if (page == this.currentPage || page == 0) return;
      else if (page <= this.totalPage) {
        this.fetchPostList(page);
      }
    },
  },
});
