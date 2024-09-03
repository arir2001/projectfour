/* jshint esversion: 6 */
/* const buttons for deleting, editing and approving coomments */
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
    let commentId = e.currentTarget.getAttribute("data-comment-id");
    let commentContent = document.getElementById(`comment${commentId}`).innerText;
    commentText.value = commentContent;
    submitButton.innerText = "Update";
    commentForm.setAttribute("action", `edit_comment/${commentId}/`);
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
    let commentId = e.currentTarget.getAttribute("data-comment-id");  
    deleteConfirm.href = `delete_comment/${commentId}`;
    deleteModal.show();
    });
}

/**
* Initializes approve functionality
gets commentId and whether or not it is approved
if it is approved, we enter 'if true statement'
here the buttoons are changed to 'unapprove?"
if the unapprove button is pressed, then the href is brought to 'apprve cmment' view
this view checks if the comment is approved or not, enters the correct if statement, and chaanges 
the approval accordingly. 
The same is done for the 'approve?' in else. 
*/

for (let button of approveButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.currentTarget.getAttribute("data-comment-id");
    let commentapproved = e.currentTarget.getAttribute("comment_approved");
    
    if (commentapproved == "True"){
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
}
