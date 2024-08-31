const editButtons = document.getElementsByClassName("btn-edit");

const approveButtons = document.getElementsByClassName("btn-approve");
const approveConfirm = document.getElementById("approveConfirm");
const approveModal = new bootstrap.Modal(document.getElementById("approveModal"));
const approveModalLabel = document.getElementById("approveModalLabel");
const modalBody = document.getElementById("modalbody-innertext");

const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");


const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");


console.log("logged");
console.log(editButtons.length);
/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Fetches the content of the corresponding comment.
* - Populates the `commentText` input/textarea with the comment's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("comment_id");
    let commentContent = document.getElementById(`comment${commentId}`).innerText;
    console.log('commentConect.', commentContent)
    commentText.value = commentContent;
    document.getElementById(`comment${commentId}`).innerText = "Updating comment...";
    submitButton.innerText = "Update";
    commentForm.setAttribute("action", `edit_comment/${commentId}`);
  });
}

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
    let commentId = e.currentTarget.getAttribute("comment_id");  
    console.log("this is the comment id", commentId);
    deleteConfirm.href = `delete_comment/${commentId}`;
    deleteModal.show();
    });
};



for (let button of approveButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.currentTarget.getAttribute("comment_id");
    let commentapproved = e.currentTarget.getAttribute("comment_approved");
    
    console.log("this is the comment apr", commentapproved)
    console.log("this is the comment apr", commentId)

    if (commentapproved == "True"){
      console.log("entered if statement");
      console.log('approve confirm', approveConfirm);
      console.log("modal body", modalBody);

      approveConfirm.innerText = "Unapprove?";
      modalBody.innerText = "Are you sure you wish to unapprove this comment?";
      approveModalLabel.innerText = "Unapprove this comment?";

      approveConfirm.href = `approve_comment/${commentId}`;
      approveModal.show();
    }else{
      console.log("entered else");
      console.log('approve confirm', approveConfirm);
      console.log("modal body", modalBody);

      approveConfirm.innerText = "Approve?";
      modalBody.innerText = "Are you sure you wish to approve this comment?";
      approveModalLabel.innerText = "Approve this comment?";

      approveConfirm.href = `approve_comment/${commentId}`;
      approveModal.show();
    }
  });
};
