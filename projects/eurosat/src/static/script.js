function clicked_img(img, fp) {
  console.log(img.src);

  var top = document.getElementById('top')

  top.src = img.src;
  top.hidden = false;

  if (img.naturalWidth < screen.width * 0.6 && img.naturalHeight < screen.height * 0.6) {

    top.width = 5 * img.naturalWidth;
    top.height = 5 * img.naturalHeight;

  } else {
    top.width = screen.width * 0.6;
    top.height = img.naturalHeight / img.naturalWidth * top.width;

  }

  document.getElementById('close').hidden = false;

}

function do_close() {
  document.getElementById('top').hidden = true;
  document.getElementById('close').hidden = true;

}
