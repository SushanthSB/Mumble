$(document).ready(function(){
	$(".signup-btn").click(function(){
		var y=$(".signup").offset().top
		//window.scrollTo(0,y)
		$("html, body").animate({ scrollTop: y}, 700);
	})
})