const requestComment = new XMLHttpRequest();
const requestDel = new XMLHttpRequest();
const requestUpdate = new XMLHttpRequest();


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
        const commentMain = document.createElement("div");
        const commentUser = document.createElement("span");    
        const commentMessage = document.createElement("span");    
        const delBtn = document.createElement("button");
        const editBtn = document.createElement("button");
        const commentEdit = document.createElement("div");
        const editInput = document.createElement("input");
        const updateBtn = document.createElement("button");

        newComment.setAttribute("class", `comment__${comment_id}`);
        commentMain.setAttribute("class", "comment__main");
        delBtn.setAttribute("onclick", `onClickDel(${comment_id})`);
        delBtn.setAttribute("class", "comment__del-btn");
        editBtn.setAttribute("class", "comment__edit-btn");
        editBtn.setAttribute("onclick", `onClickEdit(${comment_id})`);
        
        commentMessage.innerText = `${message} `;
        commentUser.innerText = `${user} `;

        commentEdit.setAttribute("class", "comment__edit");
        commentEdit.setAttribute("style", "display: none;");
        editInput.setAttribute("class", "comment__edit-input");
        editInput.setAttribute("value", `${message}`);
        editInput.setAttribute("type", "text");
        updateBtn.setAttribute("class", "comment__update-btn");
        updateBtn.setAttribute("onclick", `onClickUpdate(${comment_id})`);

        delBtn.innerText = "삭제";
        editBtn.innerText = "수정";
        updateBtn.innerText = "수정";
        const input = document.querySelector(`.comment-input__${post_id}`)
        input.value = '';
        
        element.append(newComment);
        newComment.append(commentMain);
        newComment.append(commentEdit);
        commentMain.appendChild(commentUser);
        commentMain.appendChild(commentMessage);
        commentMain.appendChild(editBtn);
        commentMain.appendChild(delBtn);
        commentEdit.appendChild(editInput);
        commentEdit.appendChild(updateBtn);

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
    if (requestDel.status < 400){
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

const onClickEdit = (commentId) => {
    const element = document.querySelector(`.comment__${commentId}`);
    const main = element.querySelector(".comment__main");
    const edit = element.querySelector(".comment__edit");

    main.style.display = "none";
    edit.style.display = "block";
}

const onClickUpdate = (postId, commentId) => {
    const url = "/post/update_comment/";
    const element = document.querySelector(`.comment__${commentId}`);
    const commentEdit = element.querySelector(".comment__edit")
    const message = commentEdit.querySelector(".comment__edit-input").value;
    requestUpdate.open("POST", url, true);
    requestUpdate.setRequestHeader(
        "Content-Type", "application/x-www-form-urlencoded"
    );
    requestUpdate.send(JSON.stringify({post_id: postId, message: message, comment_id: commentId}));
}

requestUpdate.onreadystatechange = () => {
    if(requestUpdate.readyState === XMLHttpRequest.DONE){
        UpdateHandleResponse();
    }
}


const UpdateHandleResponse = () => {
    if (requestUpdate.status < 400){
        const {message, comment_id} = JSON.parse(requestUpdate.response);
        console.log(message);
        const element = document.querySelector(`.comment__${comment_id}`);
        const commentMain = element.querySelector(".comment__main");
        const commentEdit = element.querySelector(".comment__edit");
        const comment = commentMain.querySelector(".comment__message");

        commentMain.style.display = "block";
        commentEdit.style.display = "none";
        comment.innerText = `${message}`;            
    };
};