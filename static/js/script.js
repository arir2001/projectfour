//timer adapted from: https://www.htmlcenter.com/blog/pausing-javascript-timers/
//slide show adapted from: https://www.w3schools.com/w3css/tryit.asp?filename=tryw3css_slideshow_auto
var t = null; /* Our timeout ID */
var startTimeout = new Date(); /* When the timer starts */
var timeLeft = 0; /* How much time is left */
var timeDelay = 2000; /* How long the timer should be */
var slideIndex = 0;

function startTimer() {
  carousel();

  /* time at which timer is started */
  startTimeout = new Date();

  /* set the timer to perform the thing again */
  t = setTimeout(startTimer, timeDelay);
}

function pauseTimeout() {
  /* the remaining time for the current testimonial*/
  timeLeft = timeDelay - (new Date() - startTimeout);

  /*clear the existing timeout */
  clearTimeout(t);
}

function resumeTimeout() {
  /*if timeLeft is not set, default to the full timeDelay */
  if (!timeLeft) { 
    timeLeft = timeDelay; 
  }

  /*resume the timer using the remaining timeLeft time*/
  t = setTimeout(startTimer, timeLeft);
}

function carousel() {
  var i;
  var x = document.getElementsByClassName("mySlides");

  /*hide all slides at beginning */
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }

  /*increment the slide index */
  slideIndex++;
  if (slideIndex > x.length) { 
    slideIndex = 1; 
  }

  /*show current slide slideIndex-1 */
  x[slideIndex - 1].style.display = "block";
}

/*start the function on page load */
window.onload = function() {
  /* mouseover and mouseout events to pause/resume at beginning of page load*/
  var x = document.getElementsByClassName("mySlides");

  for (var i = 0; i < x.length; i++) {
    x[i].addEventListener('mouseover', pauseTimeout);
    x[i].addEventListener('mouseout', resumeTimeout);
  }

  /*start the timer for the first time on page load.*/
  startTimer();
};