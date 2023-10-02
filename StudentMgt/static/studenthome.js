/* $(document).ready(function(){
    $("#myin").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      console.log(value)
      $("#tbo tr").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });

    $("#myin2").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#tbo1 tr").filter(function() {
          $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
      });

  }); */
  var t = document.querySelectorAll('.r')
  //console.log(t)
/* for (let i=0; i<t.length;i++)
{
  console.log(t[i].innerText)
  t[i].style.display="none"
} */
  var v = document.getElementById('myin')

  v.addEventListener("keyup", function()
  {
    var val = this.value.toLowerCase() 
    console.log(val)
    for (let i=0; i<t.length;i++)
{
  b = t[i].innerText.toLowerCase()
 // console.log(b)
 console.log(b.indexOf(val))
  if (t[i].innerText.indexOf(val) > 1)
  {
    t[i].style.display="none"
  }
  
}
    //console.log(this.value)
  }
  )