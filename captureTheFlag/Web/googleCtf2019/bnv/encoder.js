function AjaxFormPost(message) {
  var datasend;
  message = message.toLowerCase();

  var blindvalues = [
    '10',    '120',   '140',    '1450',   '150',   '1240',  '12450',
    '1250',  '240',   '2450',   '130',    '1230',  '1340',  '13450',
    '1350',  '12340', '123450', '12350',  '2340',  '23450', '1360',
    '12360', '24560', '13460',  '134560', '13560', 
  ];

  var braille_convert = {
    'a': '10',
    'b': '120',
    'c': '140',
    'd': '1450',
    'e': '150',
    'f': '1240',
    'g': '12450',
    'h': '1250',
    'i': '240',
    'j': '2450',
    'k': '130',
    'l': '1230',
    'm': '1340',
    'n': '13450',
    'o': '1350',
    'p': '12340',
    'q' : '123450',
    'r': '12350',
    's': '2340',
    't': '23450',
    'u': '1360',
    'v': '12360',
    'w': '24560',
    'x': '13460',
    'y': '134560',
    'z': '13560',
    ' ': ' ',
    ';': '560',
    '*': '160',
    '$': '12460',
    '2': '230',
    '&': '123460'
  }

  var blindmap = new Map();
  var i;
  var message_new = '';
  var newi = '';

  for (i = 0; i < blindvalues.length; i++) {
    blindmap[i + 97] = blindvalues[i];
  }

  console.log(blindmap);

  for (i = 0; i < message.length; i++) {
    console.log(message[i].charCodeAt(0));
    message_new += blindmap[(message[i].charCodeAt(0))];
    newi += braille_convert[message[i]];
  }

  datasend = JSON.stringify({
    'message': message_new,
  });

  console.log(datasend);
  console.log(newi);
}

AjaxFormPost("self");

