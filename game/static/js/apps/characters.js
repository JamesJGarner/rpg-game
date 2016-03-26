var selected = null;

$(".cd-spells li").click(function(e){
	selected = $('#' + this.id + '-dropdown ul').html();
	$('#sidebar').html(selected)
	e.preventDefault();
});


$(".cd-spells li").hover(
  function() {
    $('#sidebar').html($('#' + this.id + '-dropdown ul').html())
  }, function() {
  	if (selected != null) {
  		$('#sidebar').html(selected);
  	}
  	else {
    	$('#sidebar').empty();
	}
  }
);

var inv_selected = null;

$(".cd-inventory-bag li").click(function(e){
	inv_selected = $('#' + this.id + '-dropdown ul').html();
	$('#inv-sidebar').html(inv_selected)
	e.preventDefault();

  something(this.id);
});


function something(id) {
  // do the thing
}


$(".cd-inventory-bag li").hover(
  function() {
    $('#inv-sidebar').html($('#' + this.id + '-dropdown ul').html())
  }, function() {
  	if (inv_selected != null) {
  		$('#inv-sidebar').html(inv_selected);
  	}
  	else {
    	$('#inv-sidebar').empty();
	}
  }
);