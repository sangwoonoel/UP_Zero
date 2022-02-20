const deleteBrandLike = (url) => {
  if (confirm("찜 목록에서 제외하시겠습니까?")) {
    location.href = url;
  }
};
const deletePostLike = (url) => {
  if (confirm("좋아요를 취소하시겠습니까?")) {
    location.href = url;
  }
};
const deletePost = (url) => {
  if (confirm("게시글을 삭제하시겠습니까?")) {
    location.href = url;
  }
};
const deleteComment = (url) => {
  if (confirm("댓글을 삭제하시겠습니까?")) {
    location.href = url;
  }
};
