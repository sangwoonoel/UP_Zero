const requestComment = new XMLHttpRequest();
const requestDel = new XMLHttpRequest();
const requestUpdate = new XMLHttpRequest();

const onClickEdit = (commentId) => {
    const element = document.querySelector(`.comment__${commentId}`);
    const message = element.querySelector(".comment__message").textContent;
        
    const updateInput =  document.createElement("input");
    const updateBtn =  document.createElement("button");

    updateInput.setAttribute("class", "comment-edit-input");
    updateInput.setAttribute("type", "text");
    updateInput.value = `${message}`;

    updateBtn.setAttribute("class", "comment__up-btn");
    updateBtn.setAttribute("type", "button");
    updateBtn.setAttribute("onclick", `onClickUpdate(${commentId})`);
    updateBtn.innerText = "수정";
    
    element.innerHTML = '';
    element.appendChild(updateInput);
    element.appendChild(updateBtn);
}

const onClickComment = (postId, userId) => {
    const url = "/post/create_comment/";
    const message = document.querySelector(`.comment-input__${postId}`).value;
    requestComment.open("POST", url, true);
    requestComment.setRequestHeader(
        "Content-Type", "application/x-www-form-urlencoded"
    );
    requestComment.send(JSON.stringify({user_id:userId, post_id:postId, message: message}));
}

requestComment.onreadystatechange = () => {
    if(requestComment.readyState === XMLHttpRequest.DONE){
        CreateHandleResponse();
    }
}


const CreateHandleResponse = () => {
    if (requestComment.status < 400){
        let {user, post_id, message, comment_id} = JSON.parse(requestComment.response);
        const element = document.querySelector(`.post-comment__${post_id}`);
        const newComment = document.createElement("li");
        const commentUser = document.createElement("span");    
        const commentMessage = document.createElement("span");    
        const delBtn = document.createElement("button");
        
        newComment.setAttribute("class", `comment__${comment_id}`);
        delBtn.setAttribute("onclick", `onClickDel(${comment_id})`);
        
        commentMessage.innerText = `${message} `;
        commentUser.innerText = `${user} `;

        delBtn.innerText = "삭제";
        const input = document.querySelector(`.comment-input__${post_id}`)
        console.log(input)
        input.value = '';
        

        element.append(newComment);
        newComment.appendChild(commentUser);
        newComment.appendChild(commentMessage);
        newComment.appendChild(delBtn);

        const commentNum = document.querySelector(".post-comment__cnt");
        const commentCnt = parseInt(commentNum.innerText);
        commentNum.innerText = commentCnt + 1;
    };
};



const onClickDel = (id) => {
    const url = "/post/delete_comment/";
    requestDel.open("POST", url, true);
    requestDel.setRequestHeader(
        "Content-Type", "application/x-www-form-urlencoded"
    );
    requestDel.send(JSON.stringify({id: id}))
}

const DelHandleResponse = () => {
    if (requestComment.status < 400){
        const {id} = JSON.parse(requestDel.response)

        const element = document.querySelector(`.comment__${id}`)
        element.remove();

        const commentNum = document.querySelector(".post-comment__cnt");
        const commentCnt = parseInt(commentNum.innerText);
        commentNum.innerText = commentCnt - 1;
    }
}

requestDel.onreadystatechange = () => {
    if(requestDel.readyState === XMLHttpRequest.DONE){
        DelHandleResponse();
    }
}

// const onClickUpdate = (commentId) => {
//     const url = "/post/update_comment/";
//     const message = document.querySelector(`.comment-up-input__${postId}`).value;
//     requestComment.open("POST", url, true);
//     requestComment.setRequestHeader(
//         "Content-Type", "application/x-www-form-urlencoded"
//     );
//     requestComment.send(JSON.stringify({comment_id: commentId, message: message}));
// }

// requestUpdate.onreadystatechange = () => {
//     if(requestUpdate.readyState === XMLHttpRequest.DONE){
//         UpdateHandleResponse();
//     }
// }


// const UpdateHandleResponse = () => {
//     if (requestUpdate.status < 400){
//         let {comment_id, user, message} = JSON.parse(requestUpdate.response);
//         const element = document.querySelector(`.comment__${comment_id}`);
        
//         const updateInput =  document.createElement("input");
//         const updateBtn =  document.createElement("button");

//         updateInput.setAttribute("class", `.comment-up-input__${postId}`);
//         updateInput.setAttribute("type", "text");
//         updateInput.value = `${message}`;

//         updateBtn.setAttribute("class", "comment__up-btn");
//         updateBtn.setAttribute("type", "button");
//         updateBtn.setAttribute("onclick", `onClickUpdate(${comment_id})`);
//         updateBtn.innerText = "수정";
        
//         element.appendChild(updateInput);
//         element.appendChild(updateBtn);
        
        
//     };
// };