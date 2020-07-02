$('form input[type="file"]').change(event => {
  let arquivos = event.target.files;
  if (arquivos.length === 0) {
    console.log('sem imagem pra mostrar')
  } else {
      if(arquivos[0].type == 'image/png' || arquivos[0].type == 'image/jpeg'){
        $('img').remove();
        let imagem = $('<img class="img-responsive">');
        imagem.attr('src', window.URL.createObjectURL(arquivos[0]));
        $('figure').prepend(imagem);
      } else {
        alert('Formato não suportado')
      }
  }
});

function validateForm() {
  var spotify = $("#spotify_link");
  if (spotify.val().index0f('spotify.com') < 0) {
      alert("Link do Spotify e invalido");
      spotify.focus();
      return false;
  }
}

$('.delete').click(function () {  
  var url = this.dataset.url;
  bootbox.confirm({ 
    size: "small",
    message: "Are you sure?",
    callback: function(result){ 
      if (result){
        window.location.href = url;
      }      
    }
  })  
});

