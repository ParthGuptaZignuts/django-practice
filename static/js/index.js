document.querySelector("button").addEventListener("click", function () {
  var paragraphs = document.querySelectorAll("p");
  paragraphs.forEach(function (paragraph) {
    paragraph.style.opacity = 0;
  });
});
