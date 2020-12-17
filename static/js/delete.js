$('.delete').click(function () {
  var url = this.dataset.url;
  if (confirm("Confirma delete?")) {
    window.location.href = url;
  };  
});