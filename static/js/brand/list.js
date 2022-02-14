const params = new URL(location.href).searchParams;
const cateId = params.get("category");
const sort = params.get("sort");

// activate selected category
let activeCate;
if (cateId) {
  activeCate = document.querySelector(`li[data-category='${cateId}']`);
} else {
  activeCate = document.querySelector(`li[data-category='0']`);
}
activeCate.classList.toggle("active");

// deactivate sort button
if (sort === "like") {
  const btn = document.querySelector(".sort-btn");
  btn.classList.toggle("active");
  btn.innerText = "좋아요 순으로 보기 해제";

  btn.addEventListener("click", (e) => {
    e.preventDefault();
    let url = location.pathname;
    if (cateId) {
      url += `?category=${cateId}`;
    }
    location.href = url;
  });
}

// pagination
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
