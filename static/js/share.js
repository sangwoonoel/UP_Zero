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

document.querySelector("meta[property='og:url']").setAttribute("content", url);
document.querySelector("meta[name='twitter:url']").setAttribute("content", url);

const shareFacebook = () => {
  open(`http://www.facebook.com/sharer.php?u=${url}&t=${title}`);
};
const shareTwitter = () => {
  open(`https://twitter.com/intent/tweet?url=${url}&text=${title}`);
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
