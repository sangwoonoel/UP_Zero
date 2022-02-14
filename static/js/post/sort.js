function SortChange(e) {
    const search = new URL(location.href).searchParams;
    const keyword = search.get("keyword")
    const page = search.get("page")

    if (keyword) {
        location.href = "/post/list/?keyword="+keyword+"&sort="+ e.value;
    }
    else {
    location.href = "/post/list/?sort="+ e.value;
    } 
}

const params = new URL(location.href).searchParams;
const value = params.get("sort")
const element = document.querySelector(`option[value=${value}`);
element.selected = true;

const btn = document.querySelector(".page");

function pagination(e) {
    const search = new URL(location.href).searchParams;
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