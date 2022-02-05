const keyword = document.querySelector(".keyword");
keyword.addEventListener("keydown", (e) => {
  if (e.keyCode !== 13) return;
  onClickSearch(); // 엔터 쳐도 onClickSearch 실행
});

const requestSearch = new XMLHttpRequest();
const onClickSearch = () => {
  const keyword = document.querySelector(".keyword");

  if (!keyword.value) {
    // 검색어 없으면 브랜드 기본 리스트 페이지로 이동
    location.href = "/brand/list";
    return;
  }

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
    history.replaceState(null, null, newURL); // Querystring 형태로 URL 변경 (99% 완성..?)

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
    } // 기존 검색 결과 안내 있었다면 삭제
    const searchResult = document.createElement("p");
    searchResult.classList.toggle("search-result"); // 새로운 검색 결과 안내

    const brandsContainer = document.querySelector(".brands");
    brandsContainer.innerHTML = ""; // 브랜드 리스트 초기화

    if (brands.length === 0) {
      searchResult.innerHTML = "검색 결과가 없습니다.";
      brandListSection.prepend(searchResult);
      return;
    }

    searchResult.innerHTML = `<span class="search-result__keyword">${keyword}</span>에 대한
      <span class="search-result__cnt">${brands.length}</span>개의 브랜드 검색
      결과입니다.`;
    brandListSection.prepend(searchResult);

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
