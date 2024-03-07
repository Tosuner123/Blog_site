const quotes = [
  "“Yemin ederim ki her şeyi fazlasıyla anlamak bir hastalıktır.”",
  "Duvarı yıkmaya gücüm yetmiyorsa, kendimi parçalayacak değilim elbette. Ama önümde duvar var diye boyun eğmeyi de kabullenemem.",
  "Einstein der ki, “Sorunun formüle edilmesi, çoğu kez yalnızca matematiksel ya da deneyimsel beceriler gerektiren çözümden daha önemlidir.”",
  "“Başarısızlığa uğradınız ana kadar, başarıp başaramadığınızı bilemezsiniz.”",
  "“Bugün düşündüğün şeye yarın dönüşürsün.”",
  "“Düşünceni istediğin yöne çevirdiğinde inançların kısa sürede değişir. İnançların değiştiğinde hayatın değişir.”",
  "“Korku zihindedir, tehlike ise gerçektir. Korku duyguların esiridir, tehlike dikkat edilmesi gereken bir şeydir.”",
];

let currentQuotes = [...quotes];
const quoteElement = document.getElementById("quote");

function getRandomQuote() {
  if (currentQuotes.length === 0) {
      currentQuotes = [...quotes]; 
  }
  const randomIndex = Math.floor(Math.random() * currentQuotes.length);
  const randomQuote = currentQuotes[randomIndex];
  currentQuotes.splice(randomIndex, 1);
  return randomQuote;
}

function changeQuote() {
  quoteElement.style.opacity = 0;
  setTimeout(() => {
      const newQuote = getRandomQuote();
      quoteElement.innerHTML = newQuote;
      quoteElement.style.opacity = 1;
  }, 1000);
}


quoteElement.innerHTML = getRandomQuote();
quoteElement.style.opacity = 1;


setInterval(changeQuote, 6000);
