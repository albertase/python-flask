function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

// WINDOW LOAD MODAL
window.onload = function () {
  let time = new Date();
  let greetingElement = document.getElementById("greeting");
  let greeting = "Good";

  // if the hour is before 12pm = morning

  if (time.getHours() < 12) {
    greeting = greeting + " Morning";

    //if the hour is after 12pm but before 6pm = afternoon
  } else if (time.getHours() < 16) {
    greeting = greeting + " Afternoon";
    // if time is after 6pm = evening
  } else {
    greeting = greeting + " Evening";
  }
  greetingElement.innerText = greeting;
};

// Also For the window popup that's it causes modal plugin to popup when Loaded

let setMe = $(window).on("load", function () {
  setTimeout(function () {
    $("#myModal").modal("show");
  }, 1000);
});

if (setMe) {
  setInterval(function () {
    $("#myModal").modal("hide");
  }, 7000);
}

