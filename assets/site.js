// Draws the run line once, the first time it scrolls into view.
(function () {
  var track = document.querySelector(".track");
  if (!track || !("IntersectionObserver" in window)) return;
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

  track.classList.add("waiting");
  var observer = new IntersectionObserver(
    function (entries) {
      if (!entries[0].isIntersecting) return;
      observer.disconnect();
      track.classList.remove("waiting");
      track.classList.add("playing");
    },
    { threshold: 0.3 }
  );
  observer.observe(track);
})();
