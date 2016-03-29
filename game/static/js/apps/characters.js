var selected = null;

$(".cd-spells li").on("click", function(e){
	selected = $('#' + this.id + '-dropdown ul').html();
	$('#sidebar').html(selected)
	e.preventDefault();
});


$(".cd-spells li").hover(
  function() {
      $('#sidebar').html($('#' + id + '-dropdown ul').html())
  }, function() {
  	if (selected != null) {
  		$('#sidebar').html(selected)
  	}
  	else {
    	$('#sidebar').empty();
	}
  }
);

var inv_selected = null;
var item_selected = null;
var item_id = null;
var item_image = null;
var equipped_to = null;

$(".cd-inventory-bag li").on("click", function(e){
  $('.cd-character-items li').removeClass("cd-selected").off("click");
  $('.cd-inventory-bag li').removeClass("inv-sidebar-selected");
	inv_selected = $('#' + this.id + '-dropdown ul').html();
  item_selected = this.id.replace('inv-','');
	$('#inv-sidebar').html(inv_selected)
  $('#' + this.id).addClass("inv-sidebar-selected");
	e.preventDefault();
  ItemLookup(item_selected);
});


function ItemLookup(id) {
  $.getJSON( "/api/item/" + id, function( data ) {
    var items = [];
    $.each(data, function( key, val ) {
      if (key == "equipped_to") {
        equipped_to = val;
      }
    });
    $.each(data.item, function( key, val ) {
      if (key == "image") {
        item_image = val;
      }
      if (key == "id") {
        item_id = val;
      }
      if (key == "position") {
        for (i in val) {
          $('#' + String(val[i]).replace(' ', '-').toLowerCase()).addClass("cd-selected").on('click', myFunction);
        }
      }
    });
  });
};


function myFunction() {
  var that = this;
  var form = "character=1&equipped_to=" + this.id
  $.ajax({
    beforeSend: function(xhr, settings) {
      xhr.setRequestHeader("X-CSRFToken",  getCookie('csrftoken'));
    },
    url: "/api/items/" + item_selected + "/",
    type: "PATCH",
    data: form,
    success: function(data) {
      $('#inv-' + item_selected).addClass("cd-item-hide");
      $('#'+ equipped_to + ' img').attr('src', "");
      $('#' + that.id + ' img').attr('src', item_image).attr('id', item_selected);
      resetVars();
    }
  });
}


function UnequipItem(current, itemid) {
  var form = "character=1&equipped_to=";
  $.ajax({
    beforeSend: function(xhr, settings) {
      xhr.setRequestHeader("X-CSRFToken",  getCookie('csrftoken'));
    },
    url: "/api/items/" + itemid + "/",
    type: "PATCH",
    data: form,
    success: function(data) {
      $('#'+ current + ' img').attr('src', "");
      $('#inv-' + itemid).removeClass("cd-item-hide");
      //$('#' + that.id + ' img').attr('src', item_image);
      resetVars();
    }
  });
}


$( document ).on( 'keydown', function ( e ) {
    if ( e.keyCode === 27 ) {
        resetVars();
    }
});


function resetVars() {
  $('.cd-character-items li').removeClass("cd-selected").off("click").on("click", dothething);
  $('.cd-inventory-bag li').removeClass("inv-sidebar-selected");
  item_selected = null;
  $('#inv-sidebar').empty();
  inv_selected = null;
}


$(".cd-character-items li").hover(
    function() {
        if (!$('#' + this.id).hasClass("cd-selected")) { //Can this be improved in the future?
            hoverid("inv-" + $('#' + this.id + ' img')[0].id);
        }
    },
    function() {
      unhover()
    }
)


$('.cd-character-items li').on("click", dothething);


function dothething() {
      if (!$('#' + this.ifd).hasClass("cd-selected")) { //Can this be improved in the future?
        var itemid = $('#' + this.id + ' img')[0].id;
        UnequipItem(this.id, itemid);
    }
}


$(".cd-inventory-bag li").hover(
  function() {
    hoverid(this.id)
  }, function() {
      unhover();
  }
);  


function unhover() {
      if (inv_selected != null) {
      $('#inv-sidebar').html(inv_selected);
    }
    else {
      $('#inv-sidebar').empty();
   }
}


function hoverid(id) {
  $('#inv-sidebar').html($('#' + id + '-dropdown ul').html())
}


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}