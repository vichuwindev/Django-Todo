$(document).ready(function(){
	var csrfToken = $("input[name=csrfmiddlewaretoken").val();
	$("#create_button").on("click",function(){
		var values = $("#create_form").serialize();
		
		$.ajax({
			url: $("#create_form").data('url'),
			data: values,
			type: 'post',
			success:function(response) {

				$("#tasks_list").append('<div class="card mb-1" id="task_card" data-id="'+response.tasks.id+'"><div class="card-body">'+response.tasks.title+'<button type="button" class="close float-right" data-dismiss="close" data-id="'+response.tasks.id+'" aria-label="close"><span aria-hidden="true">&times;</span></button></div></div>');
			}
		})
		$("#create_form")[0].reset();
	})

	$("#tasks_list").on('click','.card',function(){
		var dataid = $(this).data('id')
		console.log(csrfToken);
		$.ajax({
			url:'/tasks/'+dataid+'/completed/',
			data:{
				csrfmiddlewaretoken: csrfToken,
				id: dataid,
			
			},
			type:'post',
			success:function() {
				var cardItem = $('#task_card[data-id="'+dataid+'"]');
				cardItem.css('text-decoration','line-through').hide().slideDown();
				$("tasks_list").append(cardItem);
			}
		})
	}).on('click','button.close', function(e){
		// e.stopPropagation();
		var dataid = $(this).data('id');
		$.ajax({
			url:'/tasks/'+dataid+'/delete/',
			data:{
				csrfmiddlewaretoken: csrfToken,
				id: dataid,
			
			},
			type:'post',
			dataType:'json',
			success:function(){
				var x = $("#task_card[data-id='"+dataid+'"]')
				x.remove();
			}
		})
	})
})