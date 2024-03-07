$(document).ready(function() { 

    var iOS = /iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream;
    
    if (iOS) {
      
      
      $('nav').addClass('stickynav');  
      $('#navbarNavAltMarkup').removeClass('spy-class');
      $('nav').css('opacity',1);
      $('nav').css('background-color','rgba(0,0,0,0.3)')
      
      
    } else {
      $( '.stickynav' ).css('opacity',1);
      var prevScrollpos = window.pageYOffset;
      var navbar = document.querySelector(".stickynav");
      
      
      window.onscroll = function() {
        var currentScrollPos = window.pageYOffset;
        if (prevScrollpos > currentScrollPos) {
          navbar.style.top = "0";
        } else {
          navbar.style.top = "-100px"; 
        }
        prevScrollpos = currentScrollPos;
      }
   
    }
    
    });

function likeDislike() {
  const like = document.querySelector(".like");

  const liked = getCookie("liked");

  if (liked === "true") {
    like.classList.add("active");
  }

  like.addEventListener("click", function () {
    if (like.classList.contains("active")) {
      like.classList.remove("active");
      setCookie("liked", "false", 30); 
    } else {
      like.classList.add("active");
      setCookie("liked", "true", 30); 
    }
  });
}


function setCookie(name, value, days) {
  const date = new Date();
  date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
  const expires = "expires=" + date.toUTCString();
  document.cookie = name + "=" + value + ";" + expires + ";path=/";
}


function getCookie(name) {
  const decodedCookie = decodeURIComponent(document.cookie);
  const cookies = decodedCookie.split(";");
  for (let i = 0; i < cookies.length; i++) {
    const cookie = cookies[i].trim();
    if (cookie.startsWith(name + "=")) {
      return cookie.substring(name.length + 1);
    }
  }
  return "";
}
// spinner loading













// CLOCK
setInterval(() => document.getElementById("saat").textContent = new Date().toLocaleTimeString("tr"), 1000);

