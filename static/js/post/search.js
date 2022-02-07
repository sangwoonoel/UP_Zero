const keyword = document.querySelector(".keyword");
keyword.addEventListener("keydown", (e) => {
    if (e.keyCode !== 13) return;
  onClickSearch(keyword); // 엔터 쳐도 onClickSearch 실행
});


const onClickSearch = async(keyword) => {
    if (!keyword.value) {
        // 검색어 없으면 포스트 기본 리스트 페이지로 이동
        location.href = "/post/list";
        return;
        }

    const url = "/post/search/";
    const {data} = await axios.post(url, {
        keyword:keyword.value
    });
    keyword.value = null;
    searchResHandler(data.keyword,data.posts);
}

const searchResHandler = (keyword,posts) => {
    keyword = keyword.toLowerCase();
    const newURL = `?keyword=${keyword}`;
    history.replaceState(null, null, newURL); 

    const postListSection = document.querySelector("#post-list");

    const existingSearchTitle = document.querySelector(".post-search-title");
    if (existingSearchTitle) {
      existingSearchTitle.remove();
    } // 기존 검색 결과 안내 있었다면 삭제
    const searchTitle = document.createElement("p");
    searchTitle.classList.toggle("post-search-title"); // 새로운 검색 결과 안내

    const existingPostsContainer = document.querySelector(".posts");
    if (existingPostsContainer) {
      existingPostsContainer.remove();
    } // 기존 브랜드 리스트 있었다면 삭제

    if (posts.length === 0) {
      // 검색 결과 없을 때
      searchTitle.innerHTML = "검색 결과가 없습니다.";
      postListSection.prepend(searchTitle);
      return;
    }

    // 검색 결과 존재 시
    searchTitle.innerHTML = `<span class="post-search-title__keyword">${keyword}</span>에 대한
      <span class="post-search-title__cnt">${posts.length}</span>개의 게시물 검색
      결과입니다.`;
    postListSection.prepend(searchTitle);

    const postsContainer = document.createElement("div");
    postsContainer.classList.toggle("posts"); // 새로운 브랜드 리스트
    postListSection.append(postsContainer);

    for (const post of posts) {
      const postContainer = document.createElement("div");
      postContainer.classList.toggle("post");
      postContainer.innerHTML = `<a href = "/post/${post.id}">
      <div class="post-title">
          제목: ${post.title}
      </div>
      <div class="post-preview">
          ${post.content}
      </div>
      <div class="post-author">
          작성자 : ${post.username}
      </div>
      <div class="post-created">
          <span>작성시간 : </span>
          <td>${ post.created_at }</td>
      </div>
      <div class="post-comment">
          댓글 : ${post.comment_cnt}개
      </div>
      <div class="post-like">
          좋아요 : ${post.like_cnt}개
      </div>
  </a>`; 
      postsContainer.append(postContainer);
    }
}

