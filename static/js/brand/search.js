const keyword = document.querySelector(".keyword");
keyword.addEventListener("keydown", (e) => {
  if (e.keyCode !== 13) return;
  onClickSearch(); // 엔터 치면 onClickSearch 실행
});

const requestSearch = new XMLHttpRequest();
const onClickSearch = () => {
  const keyword = document.querySelector(".keyword");

  const url = "/brand/search/";
  requestSearch.open("POST", url, true);
  requestSearch.setRequestHeader(
    "Content-Type",
    "application/x-www-form-urlencoded"
  );
  requestSearch.send(
    JSON.stringify({
      keyword: keyword.value,
    })
  );
  keyword.value = null;
};

const searchResHandler = () => {
  if (requestSearch.status < 400) {
    let { keyword, brands } = JSON.parse(requestSearch.response);
    keyword = keyword.toLowerCase();

    const newURL = `?keyword=${keyword}`;
    history.replaceState(null, null, newURL);

    // if (typeof history.pushState != "undefined") {
    //   let baseURL = location.href.includes("?")
    //     ? location.href.split("?")[0]
    //     : location.href;
    //   baseURL = baseURL.slice(0, -1); // Remove trailing slash
    //   const newURL = baseURL + `?keyword=${keyword}`;
    //   history.pushState({ path: newURL }, null, newURL);
    // }

    const brandListSection = document.querySelector("#brand-list");
    const existingSearchResult = document.querySelector(".search-result");
    if (existingSearchResult) {
      existingSearchResult.remove();
    }
    const searchResult = document.createElement("p");
    searchResult.classList.toggle("search-result");
    searchResult.innerHTML = `<span class="search-result__keyword">${keyword}</span>에 대한
    <span class="search-result__cnt">${brands.length}</span>개의 브랜드 검색
    결과입니다.`;
    brandListSection.prepend(searchResult);

    const brandsContainer = document.querySelector(".brands");
    brandsContainer.innerHTML = "";

    for (const brand of brands) {
      const brandContainer = document.createElement("div");
      brandContainer.classList.toggle("brand");
      brandContainer.innerHTML = `<div class="brand__img">
      <a href="/brand/${brand.id}">
        <img
          src="/media/${brand.image}"
          alt="${brand.name}"
          width="300"
          height="150"
        />
      </a>
    </div>
    <div class="brand__name">
      <a href="/brand/${brand.id}">${brand.name}</a>
    </div>`; // brand.image = media 폴더 내부의 경로
      brandsContainer.append(brandContainer);
    }
  }
};

requestSearch.onreadystatechange = () => {
  if (requestSearch.readyState === XMLHttpRequest.DONE) {
    searchResHandler();
  }
};
