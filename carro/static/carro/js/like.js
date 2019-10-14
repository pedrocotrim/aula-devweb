$('document').ready(() => {
  var botaoLike = $("#botao-like");
  var botaoDislike = $("#botao-dislike");
  var qtdLike = $("#contador-like");
  var qtdDislike = $("#contador-dislike");
  qtdLike.html(qtdLike.attr("data"));
  qtdDislike.html(qtdDislike.attr("data"));
  botaoLike.on('click',() => {
    if (botaoLike.hasClass("btn-success")) {
      botaoLike.removeClass("btn-success");
      botaoLike.addClass("btn-primary");
      let likes = Number(qtdLike.attr("data"));
      qtdLike.attr("data", String(likes-1));
      qtdLike.html(qtdLike.attr("data"));
    } else {
      botaoLike.removeClass("btn-primary");
      botaoLike.addClass("btn-success");
      let likes = Number(qtdLike.attr("data"));
      qtdLike.attr("data", String(likes+1));
      qtdLike.html(qtdLike.attr("data"));
      if (botaoDislike.hasClass("btn-success")) {
        botaoDislike.removeClass("btn-success");
        botaoDislike.addClass("btn-primary");
        let dislikes = Number(qtdDislike.attr("data"));
        qtdDislike.attr("data", String(dislikes-1));
        qtdDislike.html(qtdDislike.attr("data"));
      }
    }
  })
  botaoDislike.on('click',() => {
    if (botaoDislike.hasClass("btn-success")) {
      botaoDislike.removeClass("btn-success");
      botaoDislike.addClass("btn-primary");
      let dislikes = Number(qtdDislike.attr("data"));
      qtdDislike.attr("data", String(dislikes-1));
      qtdDislike.html(qtdDislike.attr("data"));
    } else {
      botaoDislike.removeClass("btn-primary");
      botaoDislike.addClass("btn-success");
      let dislikes = Number(qtdDislike.attr("data"));
      qtdDislike.attr("data", String(dislikes+1));
      qtdDislike.html(qtdDislike.attr("data"));
      if (botaoLike.hasClass("btn-success")) {
        botaoLike.removeClass("btn-success");
        botaoLike.addClass("btn-primary");
        let likes = Number(qtdLike.attr("data"));
        qtdLike.attr("data", String(likes-1));
        qtdLike.html(qtdLike.attr("data"));
      }
    }
  })
})