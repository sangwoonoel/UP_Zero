const keyword = document.querySelector(".keyword");
keyword.addEventListener("keydown", (e) => {
    if (e.keyCode !== 13) return;
  onClickSearch(keyword); // 엔터 쳐도 onClickSearch 실행
});


const onClickSearch = async(keyword) => {
    console.log(keyword.value)
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
}