$('document').ready(() => {
  var botaoLike = $("#botao-like");
  var botaoDislike = $("#botao-dislike");
  var qtdLike = $("#contador-like");
  var qtdDislike = $("#contador-dislike");
  botaoLike.on('click',() => {
    if (botaoLike.hasClass("btn-success")) {
      botaoLike.removeClass("btn-success");
      botaoLike.addClass("btn-primary");
      qtdLike.html((Number(qtdLike.html()) - 1))
    } else {
      botaoLike.removeClass("btn-primary");
      botaoLike.addClass("btn-success");
      qtdLike.html((Number(qtdLike.html()) + 1));
      if (botaoDislike.hasClass("btn-success")) {
        botaoDislike.removeClass("btn-success");
        botaoDislike.addClass("btn-primary");
        qtdDislike.html((Number(qtdDislike.html()) - 1))
      }
    }
  })
  botaoDislike.on('click',() => {
    if (botaoDislike.hasClass("btn-success")) {
      botaoDislike.removeClass("btn-success");
      botaoDislike.addClass("btn-primary");
      qtdDislike.html((Number(qtdDislike.html()) - 1))
    } else {
      botaoDislike.removeClass("btn-primary");
      botaoDislike.addClass("btn-success");
      qtdDislike.html((Number(qtdDislike.html()) + 1));
      if (botaoLike.hasClass("btn-success")) {
        botaoLike.removeClass("btn-success");
        botaoLike.addClass("btn-primary");
        qtdLike.html((Number(qtdLike.html()) - 1))
      }
    }
  })
})