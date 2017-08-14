console.log("#MAGA");

var Twit = require('twit');
var firstline = require('firstline');
var config = require('./config');
var fs = require('fs');

var T = new Twit(config);
var stream = T.stream('user');
stream.on('tweet', tweetEvent);

newline = "FUCK.";

function sendTweet(txt){
	var tweet = {
		status:txt
	}  

	T.post('statuses/update',tweet,tweeted);
}

function tweetEvent(eventMsg){

        var toWhom  = eventMsg.in_reply_to_screen_name;
        var tweetGot = eventMsg.text;tweetGot
        var other = eventMsg.user.screen_name;

        if (toWhom  == 'markovtrump_'){
                var newTweet = ".@"+other+" "+"We're gonna make that wall America again!";
                sendTweet(newTweet);
        }
}

function tweeted(error, data, response){
	if (error){
		console.log(data);
	} else {
		console.log("I just tweeted ;D");
	}
}


function wait(){
	console.log(getMarkov);
	console.log("waiting over.");
}

function getMarkov(){
	var json = JSON.parse(fs.readFileSync('./currentTweet.json', 'utf8'));
	return json["theTweet"]; 
}

function tweetTimer(){
	time = 1000*5;
	while (true){
		setTimeout(function(){console.log(getMarkov());},time);	
	}
}

//tweetTimer();
//

var interval = setInterval(function() {
	newline = getMarkov();
	console.log(newline);
	sendTweet(newline);
}, 1000*60*15);



//while (true){
//	newline = getMarkov();
//	console.log(newline);
//	setTimeout(wait, 3000);
//}
