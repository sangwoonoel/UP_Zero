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

const copyURL = () => {
  let dummy = document.createElement("input");
  document.body.append(dummy);
  dummy.value = location.href;
  dummy.select();
  document.execCommand("copy");
  dummy.remove();
  alert("현재 주소가 복사되었습니다.");
};
