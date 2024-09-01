/* jshint esversion: 6 */
/* global $ */
const publishButtons = document.getElementsByClassName("btn-publish");
const publishConfirm = document.getElementById("publishConfirm");
const publishModal = new bootstrap.Modal(document.getElementById("publishModal"));
const publishModalLabel = document.getElementById("publishModalLabel");
const modalBody = document.getElementById("modalbody-innertext");

/*STATUS = ((0, "Draft"), (1, "Published"), )*/
for (let button of publishButtons) {
  button.addEventListener("click", (e) => {
    let postId = e.currentTarget.getAttribute("data-post-id");
    let postStatus = e.currentTarget.getAttribute("post_status");
    
    console.log("this is the post status", postStatus);
    console.log("this is the post id", postId);

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
}

const deleteModal = new bootstrap.Modal(document.getElementById("deletePostModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let postId = e.target.getAttribute("post_id");
    console.log("this is the comment id", postId);
    deleteConfirm.href = `delete_post/${postId}`;
    deleteModal.show();
  });
}

$(document).ready(function() {
  $('#postTable').DataTable({
    columnDefs: [
      {
        targets: '_all', // apply searchability to all columns
        searchable: true 
      },
      {
        targets: [0],
        orderData: [0, 2]
      },
      {
        targets: [1],
        orderData: [1, 3]
      },
      {
        targets: [2],
        orderData: [2, 3]
      },
      {
        targets: [3],
        orderData: [3, 0]
      },
      {
        targets: [4],
        orderable: false, // disable sorting, search for the button column (index 4)
        searchable: false 
      }
    ]
  });
});
