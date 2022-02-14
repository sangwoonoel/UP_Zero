const params = new URL(location.href).searchParams;
const cateId = params.get("category");
const sort = params.get("sort");

// Activate selected category
let activeCate;
if (cateId) {
  activeCate = document.querySelector(`li[data-category='${cateId}']`);
} else {
  activeCate = document.querySelector(`li[data-category='0']`);
}
activeCate.classList.toggle("active");
activeCate.querySelector(".focus").classList.toggle("hidden");

// When brands are sorted
if (sort === "like") {
  const sortBtn = document.querySelector(".sort-btn");
  sortBtn.classList.toggle("active");
  sortBtn.previousElementSibling.innerText = "좋아요 순으로 보기 해제";

  sortBtn.addEventListener("click", (e) => {
    e.preventDefault();
    let url = location.pathname;
    if (cateId) {
      url += `?category=${cateId}`;
    }
    location.href = url;
  });
}

// Pagination
const pagination = (angleBtn) => {
  let url = location.pathname;

  let queryArr = new Array();
  if (cateId) {
    queryArr.push(`category=${cateId}`);
  }
  if (sort) {
    queryArr.push(`sort=${sort}`);
  }

  if (queryArr.length === 0) {
    location.href = `${url}?page=${angleBtn.value}`;
    return;
  } else if (queryArr.length === 1) {
    url += "?" + queryArr[0];
  } else {
    // queryArr.length === 2
    url += "?" + queryArr[0] + "&" + queryArr[1];
  }
  location.href = `${url}&page=${angleBtn.value}`;
};
