var SpellAcquired_id = null;
var ItemAcquired_id = null;
var ItemAcquired = null;


/* Hover Events */

$(".cd-character-items li").hover(
    function() {
        if (!$('#' + this.id).hasClass("cd-selected")) { //Can this be improved in the future?
            HoverOn("item", "inv-" + $('#' + this.id + ' img')[0].id);
        }
    },
    function() {
      HoverOff("item");
  }
)


$(".cd-inventory-bag li").hover(
  function() {
    HoverOn("item", this.id)
  },
  function() {
    HoverOff("item");
  }
);  


$(".cd-spells li").hover(
  function() {
    HoverOn("spell", this.id)
  },
  function() {
    HoverOff("spell");
  }
);


function HoverOn(type, id) {
  $(elements(type)).html($('#' + id + '-dropdown ul').html())
}


function HoverOff(type, id) {
  var html = null;
  var element = elements(type);

  if (type == "item") {
    html = $('#inv-' + ItemAcquired_id + '-dropdown ul').html();
  }
  else if (type == "spell") {
    html = selected;
  }

  if (html != null) {
    $(element).html(html);
  }
  else {
    $(element).empty();
  }
}


function elements(type) {
  if (type == "item") {
    return "#inv-sidebar";
  }
  else if (type == "spell") {
    return "#sidebar";
  }
  else {
    throw "No type defined as " + type; 
  }  
}

/* Click Events */

$('.cd-character-items li').on("click", UnequipItem);
$(".cd-spells li").on("click", SelectSpell);


$(".cd-inventory-bag li").on("click", function(e){
  $('.cd-character-items li').removeClass("cd-selected").off("click");
  $('.cd-inventory-bag li').removeClass("inv-sidebar-selected");
  $('#' + this.id).addClass("inv-sidebar-selected");
	$('#inv-sidebar').html($('#' + this.id + '-dropdown ul').html())

  ItemAcquired_id = this.id.replace('inv-','');
  ItemLookup(ItemAcquired_id);
});



function SelectSpell() {
  SpellAcquired_id = this.id;
  $('#sidebar').html($('#' + SpellAcquired_id + '-dropdown ul').html())
}


function resetVars() {
  $('.cd-character-items li').removeClass("cd-selected").off("click").on("click", UnequipItem);
  $('.cd-inventory-bag li').removeClass("inv-sidebar-selected");
  ItemAcquired_id = null;
  $('#inv-sidebar').empty();
}


function ItemLookup(id) {
  $.getJSON( "/api/items/" + id, function( data ) {
    ItemAcquired = data;
    for (i in data.item.position) {
      $('#' + String(data.item.position[i]).replace(' ', '-').toLowerCase()).addClass("cd-selected").on('click', EquipItem);
    }
  });
};


function EquipItem() {
  var form = this.id
  var url = ItemAcquired_id;
  ItemForm(form, url, this.id, true)
}


function UnequipItem() {
  var form = "";
  var url = $('#' + this.id + ' img')[0].id;
  ItemForm(form, url, this.id, false)
}


function EquipItemSuccess(id, item) {
  $('#inv-' + item).addClass("cd-item-hide");
  $('#'+ ItemAcquired.equipped_to + ' img').attr('src', "");
  $('#' + id + ' img').attr('src', ItemAcquired.item.image).attr('id', item);
  resetVars(); 
}


function UnequipItemSuccess(id, item) {
  $('#'+ id + ' img').attr('src', "").attr('id', "");
  $('#inv-' + item).removeClass("cd-item-hide");
  resetVars();
}

function EquipItemFailed(xhr, status, error, form) {
  //TODO Make the box go red then disappear and show error message at the bottom of the character for a few seconds.
  console.log(form)
  var text = JSON.parse(xhr.responseText);
  $('#error').remove()
  $('.cd-character-items li').removeClass("cd-selected")
  $('#' + form).addClass("cd-error")

  $('#' + form).fadeOut("slow", function() {
      $(this).removeClass("cd-error");
  });


  $('.cd-character-items').append("<p id='error'>" + text.non_field_errors + "</p>");
}


function ItemForm(form, url, equipt) {
  $.ajax({
    beforeSend: function(xhr, settings) {
      xhr.setRequestHeader("X-CSRFToken",  getCookie('csrftoken'));
    },
    url: "/api/items/" + url + "/",
    type: "PATCH",
    data: "character=1&equipped_to=" + form,
    error: function(xhr, status, error) {
      EquipItemFailed(xhr, status, error, form);
    },
    success: function(data) {
      if (equipt) {
        EquipItemSuccess(this.id, url)
      }
      else {
        UnequipItemSuccess(this.id, url)
      }
    }
  }); 
}


$( document ).on( 'keydown', function ( e ) {
    if ( e.keyCode === 27 ) {
        resetVars();
    }
});


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