const post = document.querySelector(".post");
const postLiked = post.getAttribute("data-liked");
const likeBtn = post.querySelector(".post-like__btn");

if (postLiked === "true") {
  likeBtn.style.color = "red";
}

const onClickLogin = (url) => {
  if (confirm("로그인이 필요합니다. 로그인 하시겠습니까?")) {
    location.href = `/login?next=${url}`;
  }
};

const requestLike = new XMLHttpRequest();
const onClickLike = (userID, postID) => {
  const post = document.querySelector(`.post[data-id="${postID}"]`);
  const postLiked = post.getAttribute("data-liked");

  let action;
  if (postLiked === "true") {
    action = "off";
    post.setAttribute("data-liked", "false");
  } else {
    action = "on";
    post.setAttribute("data-liked", "true");
  }

  const url = "/post/like/";
  requestLike.open("POST", url, true);
  requestLike.setRequestHeader(
    "Content-Type",
    "application/x-www-form-urlencoded"
  );
  requestLike.send(
    JSON.stringify({ user_id: userID, post_id: postID, action: action })
  );
};

const likeHandler = () => {
  if (requestLike.status < 400) {
    const { action } = JSON.parse(requestLike.response);
    const likeBtn = document.querySelector(".post-like__btn");
    const likeCnt = document.querySelector(".post-like__cnt");
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
    likeHandler();
  }
};
