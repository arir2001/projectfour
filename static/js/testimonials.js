const publishButtons = document.getElementsByClassName("btn-publish");
const publishConfirm = document.getElementById("publishConfirm");
const publishModal = new bootstrap.Modal(document.getElementById("publishModal"));
const publishModalLabel = document.getElementById("publishModalLabel");
const modalBody = document.getElementById("modalbody-innertext");

/*STATUS = ((0, "Draft"), (1, "Published"), (2, "Archived"))*/
for (let button of publishButtons) {
  button.addEventListener("click", (e) => {
    let testimonialId = e.currentTarget.getAttribute("data-testimonial-id");
    let testimonialStatus = e.currentTarget.getAttribute("data-testimonial-status");
    
    console.log("this is the testimonial status", testimonialStatus);
    console.log("this is the testimonial id", testimonialId);

    if (testimonialStatus == "1") {
        console.log("entered if 1");
        publishConfirm.innerText = "Unpublish";
        modalBody.innerText = "Are you sure you wish to unpublish this testimonial?";
        publishModalLabel.innerText = "Unpublish Testimonial";
        publishConfirm.href = `draft_testimonial/${testimonialId}`;  // Unpublish action
    } else {
        console.log("entered else 0");
        publishConfirm.innerText = "Publish";
        modalBody.innerText = "Are you sure you wish to publish this testimonial?";
        publishModalLabel.innerText = "Publish Testimonial";
        publishConfirm.href = `publish_testimonial/${testimonialId}`;  // Publish action
    }
    publishModal.show();
  });
}

const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let testimonialId = e.currentTarget.getAttribute("data-testimonial-id");  // Fixed the attribute
    console.log("this is the testimonial id", testimonialId);
    deleteConfirm.href = `delete_testimonial/${testimonialId}`;  // Updated href for delete action
    deleteModal.show();
  });
}
