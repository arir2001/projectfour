const publishButtons = document.getElementsByClassName("btn-publish");
const publishConfirm = document.getElementById("publishConfirm");
const publishModal = new bootstrap.Modal(document.getElementById("publishModal"));
const publishModalLabel = document.getElementById("publishModalLabel");
const modalBody = document.getElementById("modalbody-innertext");

/*STATUS = ((0, "Draft"), (1, "Published"), )*/
for (let button of publishButtons) {
  button.addEventListener("click", (e) => {
    let postId = e.currentTarget.getAttribute("post_id");
    let postStatus = e.currentTarget.getAttribute("post_status");
    
    console.log("this is the post status", postStatus)
    console.log("this is the post id", postId)

    if (postStatus == "1"){
        console.log("entered if 1");
        publishConfirm.innerText = "Unpublish?";
        modalBody.innerText = "Are you sure you wish to unpublish this post?";
        publishModalLabel.innerText = "Unpublish?";
  
        publishConfirm.href =  `draft_post/${postId}`;
        publishModal.show();
      }else{
        console.log("entered else 0");
        publishConfirm.innerText = "Publish?";
        modalBody.innerText = "Are you sure you wish to publish this post?";
        publishModalLabel.innerText = "Publish this post?";
  
        publishConfirm.href = `publish_post/${postId}`;
        publishModal.show();
    }
  });
};

$(document).ready(function() {
  $('#postTable').DataTable();
  columnDefs: [
    {
        targets: [0],
        orderData: [0, 1]
    },
    {
        targets: [1],
        orderData: [1, 0]
    },
    {
        targets: [4],
        orderData: [4, 0]
    }
]
});