//apprearance
$("input.variation").on("click", function() {
	if ($(this).val() > 3) {
		$("body").css("background", "#111");
		$("footer").attr("class", "dark");
	} else {
		$("body").css("background", "#f9f9f9");
		$("footer").attr("class", "");
	}
});

// toggle list vs card view
$(".option__button").on("click", function() {
	$(".option__button").removeClass("selected");
	$(this).addClass("selected");
	if ($(this).hasClass("option--grid")) {
		$(".results-section").attr("class", "results-section results--grid");
	} else if ($(this).hasClass("option--list")) {
		$(".results-section").attr("class", "results-section results--list");
	}
});
