(function () {
  var track = document.querySelector(".track");
  if (!track) return;

  // On narrow screens the line is vertical and ends at the last stop's dot.
  function measure() {
    track.style.setProperty("--last", track.lastElementChild.offsetHeight + "px");
  }
  measure();
  window.addEventListener("resize", measure);

  // Play the line once, the first time the track scrolls into view.
  if (!("IntersectionObserver" in window)) return;
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

  track.classList.add("waiting");
  var observer = new IntersectionObserver(
    function (entries) {
      if (!entries[0].isIntersecting) return;
      observer.disconnect();
      track.classList.remove("waiting");
      track.classList.add("playing");
    },
    { threshold: 0.35 }
  );
  observer.observe(track);
})();
