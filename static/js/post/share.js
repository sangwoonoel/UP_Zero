function CopyUrlToClipboard() {
  const t = document.createElement("input");
  t.style.display = "hidden";
  document.body.appendChild(t);

  t.value = window.document.location.href; // 현재 URL 을 세팅해 줍니다.

  t.select(); // 해당 값이 선택되도록 select() 합니다
  document.execCommand("copy"); // 클립보드에 복사합니다.

  t.blur(); // 선택된 것을 다시 선택안된것으로 바꿈니다.

  alert("URL이 클립보드에 복사되었습니다");
}
