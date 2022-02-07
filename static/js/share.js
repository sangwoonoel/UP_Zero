$(document).ready(function () {
  $(".share-btn").click(function (e) {
    $(".networks-5")
      .not($(this).next(".networks-5"))
      .each(function () {
        $(this).removeClass("active");
      });

    $(this).next(".networks-5").toggleClass("active");
  });
});

const title = document.querySelector(".brand__name").innerText;
const url = location.href;
const imageUrl = document.querySelector(".brand__img").src;

document.querySelector("meta[property='og:url']").setAttribute("content", url);
document.querySelector("meta[property='og:image']").setAttribute("content", imageUrl);
document.querySelector("meta[name='twitter:url']").setAttribute("content", url);
document.querySelector("meta[name='twitter:image']").setAttribute("content", imageUrl);


Kakao.init("173a3e42a028e54899bcec0a78b03d66");
const shareKakao = () => {
  Kakao.Link.sendDefault({
    objectType: "feed",
    content: {
      title: `${title}`,
      description: `${document.querySelector(".brand__desc").innerText}`,
      imageUrl: `${imageUrl}`,
      link: {
        webUrl: `${url}`,
        // mobileWebUrl: `${url}`
      },
    },
    social: {
      likeCount: Number(document.querySelector(".like-cnt").innerText),
    },
    buttons: [
      {
        title: "자세히 보기",
        link: {
          webUrl: `${url}`,
        },
      },
      // {
      //   title: '모바일',
      //   link: {
      //     mobileWebUrl: '${url}',
      //   },
      // },
    ],
  });
};

const shareTwitter = () => {
  open(`https://twitter.com/intent/tweet?url=${url}&text=${title}`);
};
const shareFacebook = () => {
  open(`http://www.facebook.com/sharer.php?u=${url}&t=${title}`);
};
const copyURL = () => {
  let dummy = document.createElement("input");
  document.body.append(dummy);
  dummy.value = url;
  dummy.select();
  document.execCommand("copy");
  dummy.remove();
  alert("현재 주소가 복사되었습니다.");
};
