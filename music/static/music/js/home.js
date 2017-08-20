$(document).ready(function(){
    $('.view-details').popover({html:true})
});
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
			url:"/music/"+$(this).data('id')+"/favorite/",
			dataType: 'json',
        	success: function(response) {
        		console.log(response.status)
        	}
		})
	})
})