const deletePost = (url) => {
    if(confirm('게시글을 삭제하시겠습니까?')) {
        location.href = url;
    }}