const params = new URL(location.href).searchParams;

// activate selected category
const cateId = params.get("category");
let activeCate;

if (cateId) {
  activeCate = document.querySelector(`li[data-category='${cateId}']`);
} else {
  activeCate = document.querySelector(`li[data-category='0']`);
}
activeCate.classList.toggle("active");


// deactivate sort button
if (params.get("sort") === "like") {
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