$('document').ready(()=> {
  $("#formulario").submit(
    (f) => {
      var select = $("#select-form")
      var checkboxes = $(":checkbox:checked")
      var radios = $(":radio:checked")
      var email = $("#email")
      var texto = $("#texto")
      var checkTotal=checkboxes.length;

      var radioTotal = radios.length;
      if(!(radioTotal && checkTotal && email.val()!="" && texto.val()!= "")){
        f.preventDefault(f);
        alert("Preencha todos os campos!!!!!");
      }
    }
  )
});