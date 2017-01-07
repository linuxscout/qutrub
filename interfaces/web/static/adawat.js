/* strip tashkeel*/
var script ="";

$().ready(function() {
  $('#btn1').click(function() {
    $.getJSON(script + "/ajaxGet", {}, function(d) {
      $("#rnd").text(d.rnd);
      $("#result").text(d.result);
      $("#t").text(d.time);
    });
  });
  
  $('#more').click(function() {
    $("#MoreOptions").slideToggle();
  });
  $('#all').click(function() {
    $("#tenses").toggle(!this.checked);
  });

    // stem
  $('#conjugate').click(function() {
    $("#loading").slideDown();
    var $table = $('<table/>');
     $table.attr("border", "1")[0];
     var table = $table.attr("class", "conjugate")[0];
    var item = "";
    // separate active and passive voice
    var tab_active_voice =[];
    var tab_passive_voice =[];
    $("#result").html("");
    $.getJSON(script + "/ajaxGet", {
      text: document.NewForm.InputText.value,
      action: "Conjugate",
        all: (document.NewForm.all.checked == 1 ),
        past: (document.NewForm.past.checked == 1 ),
        transitive: (document.NewForm.transitive.checked == 1 ),
        future: (document.NewForm.future.checked == 1 ),
        imperative: (document.NewForm.imperative.checked == 1 ),
        future_moode: (document.NewForm.future_moode.checked == 1 ),
        confirmed: (document.NewForm.confirmed.checked == 1 ),
        passive: (document.NewForm.passive.checked == 1 ),
        past: (document.NewForm.past.checked == 1 ),  
        future_type: document.NewForm.haraka.value,

    }, function(d) {
        var tbody = document.createElement('tbody');
      for (k  in d.result) {

        if (k == 0) {
        
          var tr = document.createElement('tr');
          var td = document.createElement('th');
            var count = 0;
          for (j in d.result[k]) {
            if (j.indexOf("ع") > -1)
                tab_passive_voice.push(count);
            else
                tab_active_voice.push(count);
            var td = document.createElement('th');
            td.appendChild(document.createTextNode(d.result[k][j]));
            tr.appendChild(td);
            count =count+1;
          }
          tbody.appendChild(tr);
        } 
        else {
          var tr = document.createElement('tr');
        var count =0;
          for (i in d.result[k])
             {
            
            if (count in tab_active_voice)
            {item = d.result[k][i];
            var td = document.createElement('td');
            td.appendChild(document.createTextNode(item));
            tr.appendChild(td);
}
          count = count +1;
          }
            
        }
        tbody.appendChild(tr);
      }
        table.appendChild(tbody);
      $("#result").append($table);
    });
    $("#loading").slideUp();
  });

});

