const quizData = [

{
question:"Which keyword is used to define a class in Java?",
options:["object","class","new","define"],
answer:"class"
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
options:["=","==","!=","Both == and !="],
answer:"Both == and !="
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
},

{
question:"What is the largest planet in our solar system?",
options:["Earth","Jupiter","Saturn","Mars"],
answer:"Jupiter"
},
{
question:"Who wrote the national anthem of India?",
options:["Rabindranath Tagore","Bankim Chandra Chatterjee","Sarojini Naidu","Subhash Chandra Bose"],
answer:"Rabindranath Tagore"
},
{
question:"What is the smallest continent in the world?",
options:["Europe","Australia","Antarctica","South America"],
answer:"Australia"
},
{
question:"Who founded Indian National Army (INA) to fight against British rule?",
options:["Subhash Chandra Bose","Bhagat Singh","Sardar Vallabhbhai Patel","Lal Bahadur Shastri"],
answer:"Subhash Chandra Bose"
},
{
question:"Which is the longest river in India?",
options:["Amazon","Nile","Ganga","Mississippi"],
answer:"Ganga"
},
{
question:"What is the capital of India?",
options:["New Delhi","Kyoto","Washington DC","Tokyo"],
answer:"New Delhi"
},
{
question:"Which is the largest state in India by area?",
options:["Uttar Pradesh","Rajasthan","Madhya Pradesh","Maharashtra"],
answer:"Rajasthan"
},
{
question:"Who gave the slogan 'Jai Jawan Jai Kisan'?",
options:["Subhash Chandra Bose","Lal Bahadur Shastri","Homi Bhabha","Bhagat Singh"],
answer:"Lal Bahadur Shastri"
},

{
question:"A shopkeeper buys an item for ₹500 and sells it for ₹650. What is the profit percentage?",
options:["25%","30%","35%","40%"],
answer:"30%"
},
{
question:"A car travels 120 km in 2 hours. At the same speed how far will it travel in 5 hours?",
options:["250 km","300 km","350 km","400 km"],
answer:"300 km"
},
{
question:"The principal is ₹2000, rate is 5% per year and time is 3 years. What is the simple interest?",
options:["₹200","₹250","₹300","₹350"],
answer:"₹300"
},
{
question:"The average of 5 numbers is 20. If one number is 30, what is the average of the remaining 4 numbers?",
options:["15","17.5","20","22.5"],
answer:"17.5"
},
{
question:"If 5 pencils cost ₹25, how much will 12 pencils cost?",
options:["₹50","₹55","₹60","₹65"],
answer:"₹60"
},
{
question:"A can complete a task in 12 days and B in 18 days. Working together, how many days will they take?",
options:["6","7.2","8","9"],
answer:"7.2"
},
{
question:"If 3x + 5 = 20, what is the value of x?",
options:["3","4","5","6"],
answer:"5"
},
{
question:"A student scored 360 marks out of 500. What is the percentage?",
options:["70%","72%","75%","80%"],
answer:"72%"
}

];

let currentQuestion = 0;
let score = 0;

const question = document.getElementById("question");
const options = document.getElementById("options");
const nextBtn = document.getElementById("next-btn");
const result = document.getElementById("result");
const message = document.getElementById("message");
const questionNumber = document.getElementById("question-number");

function loadQuestion(){

    const q = quizData[currentQuestion];

    questionNumber.innerHTML =
    `Question ${currentQuestion + 1} of ${quizData.length}`;

    question.innerHTML = q.question;

    options.innerHTML = "";

    message.innerHTML = "";

    q.options.forEach(option => {

        const btn = document.createElement("button");

        btn.innerHTML = option;

        btn.classList.add("option-btn");

        btn.onclick = () => {

            Array.from(options.children).forEach(button=>{
                button.disabled = true;
            });

            if(option === q.answer){

                score++;

                message.innerHTML =
                "✅ Correct Answer";

                message.className = "correct";
            }
            else{

                message.innerHTML =
                "❌ Wrong Answer<br>Correct Answer : "
                + q.answer;

                message.className = "wrong";
            }
        };

        options.appendChild(btn);
    });
}

nextBtn.addEventListener("click",()=>{

    currentQuestion++;

    if(currentQuestion < quizData.length){

        loadQuestion();
    }
    else{

        let performance = "";

        if(score >= 20){
            performance = "Excellent Performance";
        }
        else if(score >= 15){
            performance = "Good Performance";
        }
        else{
            performance = "Need Improvement";
        }

        question.style.display="none";
        options.style.display="none";
        nextBtn.style.display="none";
        message.style.display="none";
        questionNumber.style.display="none";

        result.innerHTML =
        "Quiz Completed<br><br>" +
        "Final Score : " +
        score + "/" + quizData.length +
        "<br><br>" +
        performance;
    }
});

loadQuestion();