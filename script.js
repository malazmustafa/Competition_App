
function checkhtml(){

	var question1 = document.quiz-html.question1.value;
	var question2 = document.quiz-html.question2.value;
	var question3 = document.quiz-html.question3.value;
	var correct = 0;


	if (question1 == "Hyper text markup language") {
		correct++;
}
	if (question2 == "Creating webpages") {
		correct++;
}	
	if (question3 == "") {
		correct++;
	}
	
	var pictures = ["success.gif", "img/meh.gif", "img/lose.gif"];
	var messages = ["Great job!", "That's just okay", "You really need to do better"];
	var score;

	if (correct == 0) {
		score = 2;
	}

	if (correct > 0 && correct < 3) {
		score = 1;
	}

	if (correct == 3) {
		score = 0;
	}

	document.getElementById("after_submit").style.visibility = "visible";

	document.getElementById("message").innerHTML = messages[range];
	document.getElementById("number_correct").innerHTML = "You got " + correct + " correct.";
	document.getElementById("picture").src = pictures[range];
	}

function checkpython(){

		var question1 = document.quiz-python.question1.value;
		var question2 = document.quiz-python.question2.value;
		var question3 = document.quiz-python.question3.value;
		var correct = 0;
	
	
		if (question1 == "Front end") {
			correct++;
	}
		if (question2 == "Explicit is better than implicit") {
			correct++;
	}	
		if (question3 == "") {
			correct++;
		}
		
		var pictures = ["img/success.gif", "img/meh.gif", "img/lose.gif"];
		var messages = ["Great job!", "That's just okay", "You really need to do better"];
		var score;
	
		if (correct == 0) {
			score = 2;
		}
	
		if (correct > 0 && correct < 3) {
			score = 1;
		}
	
		if (correct == 3) {
			score = 0;
		}
	
		document.getElementById("after_submit").style.visibility = "visible";
	
		document.getElementById("message").innerHTML = messages[range];
		document.getElementById("number_correct").innerHTML = "You got " + correct + " correct.";
		document.getElementById("picture").src = pictures[range];
		}