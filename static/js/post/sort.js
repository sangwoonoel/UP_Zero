const search = new URL(location.href).searchParams;
const value = search.get("sort")
const element = document.querySelector(`option[value=${value}]`);

//정렬 option클릭시 고정 - select default 초기화 방지 
if (element) {
    element.selected = true;
}

const keyword = document.querySelector(".input-keyword");
keyword.addEventListener("keydown", (e) => {
    if (e.keyCode !== 13) return;
    PostSearch(this); // 엔터 쳐도 PostSearch 실행
});

function SortChange(e) {
    const keyword = search.get("keyword")
    const page = search.get("page")

    if (keyword) {
        location.href = "/post/list/?keyword="+keyword+"&sort="+ e.value;
    }
    else {
    location.href = "/post/list/?sort="+ e.value;
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