$(".navBtn").click(function () {
  $(".menu").addClass("Etd");
});
$(".closeBtn").click(function () {
  $(".menu").removeClass("Etd");
});
$(".closeBtnblack").click(function () {
  $(".Lightbox").removeClass("visible");
});
$(".toTimeLine").click(function () {
  history.back();
});
let sliderConatainer = $(".LightBox");
$(function () {
  $images = $(".eventImage");
  $captions = $("figurecaption");
  let slider = $("<div class='sliders'></div>");
  let imgCap;
  for (let index = 0; index < $images.length; index++) {
    let imgTag = $images[index];
    if ($captions[index].outerText != "") {
      imgCap = $captions[index].outerHTML;
    }
    let imgUrl = imgTag.src;
    console.log(imgUrl);
    console.log(imgCap);
    let imgDom = '<img class="postImg" src=' + imgUrl + ">";
    let imgCapDom = '<span class="postCap">' + imgCap + "</span>";
    let oneSlide = $(
      '<div class="gallery-cell"> <div class="wrapImg">' +
        imgDom +
        "</div>" +
        imgCapDom +
        "</div>"
    );
    console.log(oneSlide);
    oneSlide.appendTo(slider);
  }

  <div class="Lightbox">
    <div class="sliders">
      <div class="gallery-cell">
        <div class="wrapImg"> <img class="postImg" src=""><span></span></div>
      </div>
            <div class="gallery-cell">
        <div class="wrapImg"> <img class="postImg" src=""><span></span></div>
      </div>
  </div>
</div>

  console.log(slider);
  slider.appendTo($(".Lightbox"));
  $(".sliders").slick({
    dots: true,
    infinite: true,
    autoplay: false,
    speed: 200,
    fade: true,
    cssEase: "ease-in-out",
  });
  
  $("a[data-slide]").click(function (e) {
    $(".Lightbox").addClass("visible");
    e.preventDefault();
    var slideno = $(this).data("slide");
    console.log(slideno);
    $(".sliders").slick("slickGoTo", slideno - 1);
  });


});
function setYear(year){
  let yearPast = year - 1990;
  console.log(yearPast);
  let yearPOS = yearPast/34 * $('.parent').width();
  console.log(yearPast/30);
  $(".currentTime").css('left',yearPOS + 'px');
}