const questions = [

{
question:"Which keyword is used to define a class in Java?",
options:["Object","Class","New","Define"],
answer:"Class"
},

{
question:"Which method is the entry point of Java program?",
options:["start()","run()","main()","init()"],
answer:"main()"
},

{
question:"Which data type is used to store decimal numbers in Java?",
options:["int","double","char","boolean"],
answer:"double"
},

{
question:"Which operator is used for comparison?",
options:["=","==","!=","Both B and C"],
answer:"Both B and C"
},

{
question:"Which loop is guaranteed to run at least once?",
options:["for","while","do-while","foreach"],
answer:"do-while"
},

{
question:"Which of these is not a Java keyword?",
options:["static","void","main","final"],
answer:"main"
},

{
question:"Which keyword is used to stop a loop in Java?",
options:["stop","exit","break","continue"],
answer:"break"
},

{
question:"Which of the following is not a primitive data type?",
options:["int","float","String","char"],
answer:"String"
}

];

let currentQuestion = 0;
let score = 0;

function loadQuestion(){

    if(currentQuestion >= questions.length){

        let performance="";

        if(score===questions.length){
            performance="🏆 Excellent Performance";
        }
        else if(score>=6){
            performance="✅ Good Performance";
        }
        else{
            performance="📚 Need Improvement";
        }

        document.getElementById("question").innerHTML =
        "Quiz Completed";

        document.getElementById("options").innerHTML = "";

        document.getElementById("result").innerHTML =
        performance;

        document.getElementById("score").innerHTML =
        "Score : " + score + "/" + questions.length;

        return;
    }

    document.getElementById("question").innerHTML =
    questions[currentQuestion].question;

    let html = "";

    questions[currentQuestion].options.forEach(option=>{

        html +=
        `<button onclick="checkAnswer('${option}')">
        ${option}
        </button><br>`;
    });

    document.getElementById("options").innerHTML =
    html;
}

function checkAnswer(option){

    if(option===questions[currentQuestion].answer){

        document.getElementById("result").innerHTML =
        "✅ Correct";

        score++;
    }
    else{

        document.getElementById("result").innerHTML =
        "❌ Wrong";
    }

    currentQuestion++;

    setTimeout(loadQuestion,1000);
}

loadQuestion();