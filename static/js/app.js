$('form input[type="file"]').change(event => {
  let arquivos = event.target.files;
  if (arquivos.length === 0) {
    console.log('sem imagem pra mostrar')
  } else {
      if(arquivos[0].type == 'image/png') {
        $('img').remove();
        let imagem = $('<img class="img-responsive">');
        imagem.attr('src', window.URL.createObjectURL(arquivos[0]));
      elif(arquivos[0].type == 'image/jpeg') {
        $('img').remove();
        let imagem = $('<img class="img-responsive">');
        imagem.attr('src', window.URL.createObjectURL(arquivos[0]));
        $('figure').prepend(imagem);
      elif(arquivos[0].type == 'image/jpg') {
        $('img').remove();
        let imagem = $('<img class="img-responsive">');
        imagem.attr('src', window.URL.createObjectURL(arquivos[0]));
      } else {
        alert('Formato não suportado')
      }
  }
});