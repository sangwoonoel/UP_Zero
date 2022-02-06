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

    const existingSearchTitle = document.querySelector(".search-title");
    if (existingSearchTitle) {
      existingSearchTitle.remove();
    } // 기존 검색 결과 안내 있었다면 삭제
    const searchTitle = document.createElement("p");
    searchTitle.classList.toggle("search-title"); // 새로운 검색 결과 안내

    const existingBrandsContainer = document.querySelector(".brands");
    if (existingBrandsContainer) {
      existingBrandsContainer.remove();
    } // 기존 브랜드 리스트 있었다면 삭제

    if (brands.length === 0) {
      // 검색 결과 없을 때
      searchTitle.innerHTML = "검색 결과가 없습니다.";
      brandListSection.prepend(searchTitle);
      return;
    }

    // 검색 결과 존재 시

    searchTitle.innerHTML = `<span class="search-title__keyword">${keyword}</span>에 대한
      <span class="search-title__cnt">${brands.length}</span>개의 브랜드 검색
      결과입니다.`;
    brandListSection.prepend(searchTitle);

    const brandsContainer = document.createElement("div");
    brandsContainer.classList.toggle("brands"); // 새로운 브랜드 리스트
    brandListSection.append(brandsContainer);

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
