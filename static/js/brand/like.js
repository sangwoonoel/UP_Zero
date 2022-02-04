const brand = document.querySelector(".brand");
const brandLiked = brand.getAttribute("data-liked");
const likeBtn = brand.querySelector(".like-btn");
if (brandLiked === "true") {
    likeBtn.style.color = "red";}

const onClickAlert = () => {
    alert("로그인이 필요합니다.");
}

const requestLike = new XMLHttpRequest();
const onClickLike = (userID, brandID) => {
  const brand = document.querySelector(`.brand[data-id="${userID}"]`);
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
  requestLike.open("POST", url, true);
  requestLike.setRequestHeader(
    "Content-Type",
    "application/x-www-form-urlencoded"
  );
  requestLike.send(JSON.stringify({ user_id: userID, brand_id: brandID, action: action }));
};

const likeResHandler = () => {
  if (requestLike.status < 400) {
    const { action } = JSON.parse(requestLike.response);
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
  }
};

requestLike.onreadystatechange = () => {
  if (requestLike.readyState === XMLHttpRequest.DONE) {
    likeResHandler();
  }
};