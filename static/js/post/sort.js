const params = new URL(location.href).searchParams;

if (params.get("sort") === "like") {
    const sort = document.querySelector(".sort-btn");
    sort.innerHTML = `<select class="sort" name="sort" id="sort">
    <option class="sort=like" value="like" id="like" {% if sort == 'like' %}selected {% endif %} >좋아요순</option>
    <option class="sort=latest" value="latest" id="latest" {% if sort == 'latest' %}selected {% endif %} >최신순</option>
    <option class="sort=past" value="past" id="past" {% if sort == 'past' %}selected {% endif %} >과거순</option>
    </select>
    <button type="submit" value="">정렬</button>`;
}
else if (params.get("sort") === "past") {
    const sort = document.querySelector(".sort-btn");
    sort.innerHTML = `<select class="sort" name="sort" id="sort">
    <option class="sort=past" value="past" id="past" {% if sort == 'past' %}selected {% endif %} >과거순</option>
    <option class="sort=like" value="like" id="like" {% if sort == 'like' %}selected {% endif %} >좋아요순</option>
    <option class="sort=latest" value="latest" id="latest" {% if sort == 'latest' %}selected {% endif %} >최신순</option>
    </select>
    <button type="submit" value="">정렬</button>`;
}
else {
    const sort = document.querySelector(".sort-btn");
    sort.innerHTML = `<select class="sort" name="sort" id="sort">
    <option class="sort=latest" value="latest" id="latest" {% if sort == 'latest' %}selected {% endif %} >최신순</option>
    <option class="sort=past" value="past" id="past" {% if sort == 'past' %}selected {% endif %} >과거순</option>
    <option class="sort=like" value="like" id="like" {% if sort == 'like' %}selected {% endif %} >좋아요순</option>
    </select>
    <button type="submit" value="">정렬</button>`;
}