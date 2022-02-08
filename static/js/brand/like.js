const brand = document.querySelector(".brand");
const brandLiked = brand.getAttribute("data-liked");
const likeBtn = brand.querySelector(".like-btn");
if (brandLiked === "true") {
  likeBtn.style.color = "red";
}

const onClickAlert = () => {
  alert("로그인이 필요합니다.");
};

const onClickLike = async (userID, brandID) => {
  const brand = document.querySelector(`.brand[data-id="${brandID}"]`);
  const brandLiked = brand.getAttribute("data-liked");

  let action;
  if (brandLiked === "true") {
    action = "off";
    brand.setAttribute("data-liked", "false");
  } else {
    action = "on";
    brand.setAttribute("data-liked", "true");
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
  const likeBtn = document.querySelector(".like-btn");
  const likeCnt = document.querySelector(".like-cnt");
  let num;

  if (action === "on") {
    likeBtn.style.color = "red";
    num = Number(likeCnt.innerText) + 1;
  } else {
    likeBtn.style.color = "black";
    num = Number(likeCnt.innerText) - 1;
  }
  likeCnt.innerText = num;
};
