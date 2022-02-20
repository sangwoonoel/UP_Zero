const search = new URL(location.href).searchParams;
const option = search.get("sort")
const select = document.querySelector(".select-default span");

const current = window.location.pathname;

const write_nav = document.querySelector("#write_post");
const like_nav = document.querySelector("#like_post");
const write_post = document.querySelector("#write-nav");
const like_post = document.querySelector("#like-post");

if (current.includes('/mypage/posts/')) {
    like_post.style=" color: var(--dark-gray); border: none";
    like_nav.style=" color: var(--line-gray);";
}
else if(current.includes('/mypage/scraps/')){
    write_post.style=" color: var(--dark-gray); border: none";
    write_nav.style=" color: var(--line-gray);";


}

const keyword = document.querySelector(".input-keyword");
keyword.addEventListener("keydown", (e) => {
    if (e.keyCode !== 13) return;
    PostSearch(this); // 엔터 쳐도 PostSearch 실행
});

switch(option) {
    case 'latest':
        select.innerText = '최신 순';
        break;
    case 'like':
        select.innerText = '인기 순';
        break;
    case 'past':
        select.innerText = '과거 순';
        break;
}

function SortChange(e) {
    const keyword = search.get("keyword");
    const page = search.get("page");

    if (keyword) {
        location.href = "/mypage/posts/?keyword="+keyword+"&sort="+ e.id;
    }
    else {
    location.href = "/mypage/posts/?sort="+ e.id;
    } 

}

function PostSearch(e) {
    const keyword = document.querySelector(".input-keyword").value;
    const sort = search.get("sort")

    if (sort) {
        location.href = "/mypage/posts/?keyword="+keyword+"&sort="+ sort;
    }
    else {
        location.href = "/mypage/posts/?keyword="+ keyword;
    }
}

function pagination(e) {
    const sort = search.get("sort")
    const keyword = search.get("keyword")

    if (sort){
        if (keyword) {
            location.href = "/mypage/posts/?keyword="+keyword+"&sort="+sort+"&page="+ e.value;
        }
        else {
        location.href = "/mypage/posts/?sort="+sort+"&page="+ e.value;
        }
    }
    else {
        if (keyword) {
            location.href = "/mypage/posts/?keyword="+keyword+"&page="+ e.value;
        }
        else {
            location.href = "/mypage/posts/?page="+ e.value;

        }
    }
}