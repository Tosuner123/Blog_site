 
 const galleryItems=document.querySelector(".gallery-items").children;
 const prev=document.querySelector(".prev");
 const next=document.querySelector(".next");
 const page=document.querySelector(".page-num");
 const maxItem=4;
 let index=1;
  
  const pagination=Math.ceil(galleryItems.length/maxItem);
  console.log(pagination)

  prev.addEventListener("click", function() {
	index--;
	check();
	showItems();
	if (window.innerWidth <= 767) {
	  window.scrollBy(0, -1000);
	}
  });
  
  next.addEventListener("click", function() {
	index++;
	check();
	showItems();
	
	if (window.innerWidth <= 767) {
	  window.scrollBy(0, -1500); 
	}
  });

  function check(){
	
  	 if(index==pagination){
  	 	next.classList.add("disabled");
  	 }
  	 else{
  	   next.classList.remove("disabled");	
  	 }

  	 if(index==1){
  	 	prev.classList.add("disabled");
  	 }
  	 else{
  	   prev.classList.remove("disabled");	
  	 }
	 
	
	  
	
  }

  function showItems() {
  	 for(let i=0;i<galleryItems.length; i++){
  	 	galleryItems[i].classList.remove("show");
  	 	galleryItems[i].classList.add("hide");


  	    if(i>=(index*maxItem)-maxItem && i<index*maxItem){
          galleryItems[i].classList.remove("hide");
          galleryItems[i].classList.add("show");
  	    }
		console.log(galleryItems[i]);
  	    page.innerHTML=index;
  	 }

  	 	
  }
  

  
  window.onload=function(){
	setTimeout(function() {
		deneme = document.getElementById('loading').style.display = 'none';
		 document.querySelector(' .gallery-items ').style.display = 'flex';
		 const galleryItems = document.querySelector('.gallery-items');
    	galleryItems.style.justifyContent = '';
    	galleryItems.style.alignItems = '';
	   }, 1000);
  	showItems();
  	check();
	  
  }



 




