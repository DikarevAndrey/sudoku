$('#solution-btn').click(function() {
  $('#solution-table').toggle();
  if ($(this).html()=="Показать ответ") {
    $(this).html("Скрыть ответ");
  } else {
    $(this).html("Показать ответ");
  }
});

$('#clear-btn').click(function() {
  var i;
  for (i = 0; i < 81; i++) {
    $cell = $('#cell-' + i.toString());
    if ($cell.attr('data-user') == "true") {
      $cell.val('');
      $cell.css("background-color", "#FFFFFF");
    }
  }
});

$('#check-btn').click(function() {
  var i;
  var is_correct = true;
  for (i = 0; i < 81; i++) {
    $quiz_cell = $('#cell-' + i.toString());
    $solution_cell = $('#solution-cell-' + i.toString());
    if ($quiz_cell.attr('data-user') == "true") {
      if ($quiz_cell.val() == $solution_cell.val()) {
        $quiz_cell.css("background-color", "#a4fc71");
      } else {
        is_correct = false;
        $quiz_cell.css("background-color", "#fc7070");
      }
    }
  }
  if (is_correct == true) {
    $('#myModal').modal();
  }
});

$('[id^=cell]').bind("change paste keyup", function() {
   $(this).css("background-color", "#FFFFFF");
});