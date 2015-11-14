/* strip tashkeel*/
var CHARCODE_SHADDA = 1617;
var CHARCODE_SUKOON = 1618;
var CHARCODE_SUPERSCRIPT_ALIF = 1648;
var CHARCODE_TATWEEL = 1600;
var CHARCODE_ALIF = 1575;


$().ready(function() {
  $('#btn1').click(function() {
    $.getJSON(script + "/ajaxGet", {}, function(d) {
      $("#rnd").text(d.rnd);
      $("#result").text(d.result);
      $("#t").text(d.time);
    });
  });
  $('#randomMaqola').click(function() {
    $.getJSON("http://maqola.org/site/widget?nolayout", function(d) {
      // $("#InputText").text(d.result+"Taha");
      if (d) document.NewForm.InputText.value = d.body.replace(/<\/?[^>]+(>|$)/g, " ");
      else document.NewForm.InputText.value = "TZA";;
      //"#result").text(d.time);
    });
  });
  $('#random').click(function() {
    $.getJSON(script + "/ajaxGet", {
      text: '',
      action: "RandomText"
    }, function(data) {
      if (data) document.NewForm.InputText.value = data.result;
      else document.NewForm.InputText.value = "TZA";
    });
  });
  $('#stripharakat').click(function() {
    //  $("#result").html("<pre>TATAH\nNTATAH</pre>");
    $.getJSON(script + "/ajaxGet", {
      text: document.NewForm.InputText.value,
      action: "StripHarakat"
    }, function(d) {
      $("#result").html("<p>" + d.result + "</p>");
      //"#result").text(d.time);
    });
  });

  $('#conjugate2').click(function() {
    //  $("#result").html("<pre>TATAH\nNTATAH</pre>");
    $.getJSON(script + "/ajaxGet", {
      text: document.NewForm.InputText.value,
      action: "Conjugate"
    }, function(d) {
      $("#result").html("<p>" + d.result + "</p>");
      //"#result").text(d.time);
    });
  });

	// stem
  $('#conjugate').click(function() {
    $("#loading").slideDown();
    var $table = $('<table/>');
     $table.attr("border", "1")[0];
     var table = $table.attr("class", "conjugate")[0];
    /* headers = ["<tr>", "<th>المدخل</th>", "<th>تشكيل</th>", "<th>الأصل</th>",
      "<th>الزوائد</th>", "<th>الجذع</th>",
      "<th style='white-space:nowrap;'>الحالة الإعرابية</th>",
      "<th>النوع</th><th>النحوي</th>", "<th>شيوع</th>", "</tr>"
    ].join('');
    $table.append(headers);
*/
    var item = "";
    $("#result").html("");
    $.getJSON(script + "/ajaxGet", {
      text: document.NewForm.InputText.value,
      action: "Conjugate"
    }, function(d) {
        var tbody = document.createElement('tbody');
      for (k  in d.result) {

        if (k == 0) {
          var tr = document.createElement('tr');
          var td = document.createElement('th');
          //td.appendChild(document.createTextNode(k));
          //tr.appendChild(td);
          for (j in d.result[k]) {
            var td = document.createElement('th');
            td.appendChild(document.createTextNode(d.result[k][j]));
            tr.appendChild(td);
          }
          tbody.appendChild(tr);
        } 
		else {
          var tr = document.createElement('tr');
          for (i in d.result[k])
			 {
			
            //tr = document.createElement('tr');
            item = d.result[k][i];
            var td = document.createElement('td');
            td.appendChild(document.createTextNode(item));
            tr.appendChild(td);

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

