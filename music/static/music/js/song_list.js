$(document).ready(function(){
	$('.btn-favorite').hover(function(){
		$(this).css({'color':'orange'})
	}, function(){
		$(this).css({'color':'initial'})
	})
})

$(document).ready(function(){
	$('.btn-favorite').click(function(){
		$(this).toggleClass('add-fav')
		$.ajax({
			type:"GET",
			url:"/music/songs/"+$(this).data('id')+"/",
			dataType: 'json',
        	success: function(response) {
        		console.log(response.status)
        	}
		})
	})
})

$(document).ready(function(){
	$('.play-song').click(function(){
		url=$(this).data("song")
		$('.player-div').css({"display":"block"})
		$('.song-play').attr({"src":url,"autoplay":true,})
	})
})