const search = new URL(location.href).searchParams;
const option = search.get("sort")
const select = document.querySelector(".select-default span");

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
        location.href = "/post/list/?keyword="+keyword+"&sort="+ e.id;
    }
    else {
    location.href = "/post/list/?sort="+ e.id;
    } 

}

function PostSearch(e) {
    const keyword = document.querySelector(".input-keyword").value;
    const sort = search.get("sort")

    if (sort) {
        location.href = "/post/list/?keyword="+keyword+"&sort="+ sort;
    }
    else {
        location.href = "/post/list/?keyword="+ keyword;
    }
}

function pagination(e) {
    const sort = search.get("sort")
    const keyword = search.get("keyword")

    if (sort){
        if (keyword) {
            location.href = "/post/list/?keyword="+keyword+"&sort="+sort+"&page="+ e.value;
        }
        else {
        location.href = "/post/list/?sort="+sort+"&page="+ e.value;
        }
    }
    else {
        if (keyword) {
            location.href = "/post/list/?keyword="+keyword+"&page="+ e.value;
        }
        else {
            location.href = "/post/list/?page="+ e.value;

        }
    }
}