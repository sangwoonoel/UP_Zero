const brand = document.querySelector(".brand");
const isBrandLiked = brand.getAttribute("data-liked"); // when the page is loaded for the first time
const likeBtn = brand.querySelector(".like-btn");
if (isBrandLiked === "true") {
  likeBtn.style.color = "red";
}

const onClickLike = async (userID, brandID) => {
  const isBrandLiked = brand.getAttribute("data-liked"); // needs to be defined inside the function as well
  let action;
  if (isBrandLiked === "true") {
    action = "off";
  } else {
    action = "on";
  }

  const url = "/brand/like/";
  const { data } = await axios.post(url, {
    user_id: userID,
    brand_id: brandID,
    action: action,
  });
  likeResHandler(data.action);
};

const likeResHandler = (action) => {
  const likeCnt = brand.querySelector(".like-cnt");
  let num;

  if (action === "on") {
    brand.setAttribute("data-liked", "true");
    likeBtn.style.color = "red";
    num = Number(likeCnt.innerText) + 1;
  } else {
    brand.setAttribute("data-liked", "false");
    likeBtn.style.color = "black";
    num = Number(likeCnt.innerText) - 1;
  }
  likeCnt.innerText = num;
};

const onClickLogin = () => {
  if (confirm("로그인이 필요합니다. 로그인 하시겠습니까?")) {
    location.href = `/login?next=${location.pathname}`;
  }
};
