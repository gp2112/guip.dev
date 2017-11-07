 $.get('https://blockchain.info/ticker', function(data){
     $('.rate-usd').each(function(){
         $(this).text(data.USD.last);
     });
     var percent = Math.floor($('.rate-usd').text()/100);
     $('#percent').text(percent);
});

$('.bitcoin-logo').mouseover(function(){
    $('#info-btc').fadeIn(100);
});

$('.bitcoin-logo').mouseout(function(){
    $('#info-btc').fadeOut(100);
});
