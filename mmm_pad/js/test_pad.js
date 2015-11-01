$(document).ready(function() {
	var hup = "hang_up";
	var pup = "pick_up";

	$("#mp_receiver")
		.html(pup)
		.click(function() {
			if($(this).html() == hup) {
				next_state = pup;
			} else if($(this).html() == pup) {
				next_state = hup;
			}

			$.ajax({
				url : $(this).html(),
				context : this
			}).done(function(json) {
				console.info(json);				
				$(this).html(next_state);
			});
		});
	
	for(var i=0; i<4; i++) {
		var tr = $(document.createElement('tr'));
		for(var j=0; j<4; j++) {
			var html = "<p class=\"num\">" + (((i * 4) + j) + 1) + "</p>";

			var td = $(document.createElement('td'));
			var a = $(document.createElement('a'))
				.html(html)
				.click(function() {
					var mapping = $($(this).find('.num')[0]).html();

					$.ajax({
						url : "mapping/" + (Number(mapping) - 1)
					}).done(function(json) {
						console.info(json);
					});
				});

			$(td).append(a);
			$(tr).append(td);
		}

		$("#mp_main").append(tr);
	}
});