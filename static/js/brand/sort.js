const params = new URL(location.href).searchParams;

if (params.get("sort") === "like") {
  const form = document.querySelector(".sort-form");
  const btn = document.querySelector(".sort-btn");
  btn.classList.toggle("active");
  btn.innerText = "좋아요 순으로 보기 해제";

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    location.href = location.pathname;
  });
}
