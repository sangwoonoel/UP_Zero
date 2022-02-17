const created = document.querySelectorAll(".post-created");
for (let creat of created) {
    time = creat.innerText
    if (time.slice(-3) === '분 전')
    {
        if(time.length === 4){
            creat.innerText = '\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0'+ time;
            console.log(time)
        }
        else {
            creat.innerText = '\u00a0\u00a0\u00a0\u00a0'+ time;
        }
    }
    else if (time.slice(-3) === '일 전')
    {
        creat.innerText = '\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0'+ time;

    }
    else if (time.slice(-4) === '방금 전')
    {
        creat.innerText = '\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0'+ time;

    }
}