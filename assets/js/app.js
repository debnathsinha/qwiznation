angular.module('qw', [])
.controller('QwController', function($scope, $http, $location, $window) {
    $scope.name = "Game of Thrones";
    // $http.get('quiz')
    // .success(function(data) {
    // 	console.log(data);
    // })
    // .error(function(msg) {
    // 	console.log(msg);
    // });

    $scope.quiz = {
	name: 'Enter the name of the quiz',
	result: 'Enter the question result',
	questions: [
	    {
		text: 'Enter the question',
		pictureUrl: 'http://www.keenthemes.com/preview/metronic/theme/assets/global/plugins/jcrop/demos/demo_files/image2.jpg',
		correctAnswer: 1,
		answers: [
		    'Answer 1',
		    'Answer 2',
		    'Answer 3',
		    'Answer 4'
		]
	    }]
    }

    

    $scope.currentQuestion = $scope.quiz.questions[0];
    var regex = /\/quiz\/([a-zA-Z0-9\/]+)$/;
    var match = regex.exec($location.absUrl());
    if (match[1] === "new") {
	// This is a new quiz
    } else {
	// This is an existing quiz, pull the questions
	regex = /\/quiz\/([a-zA-Z0-9]+)\/edit$/;
	match = regex.exec($location.absUrl());
	if (match) {
	    $http.get("/api/quiz/" + match[1])
		.success(function(response) {
    		    console.log(response);
    		    $scope.quiz = response;
    		    $scope.currentQuestion = $scope.quiz.questions[0];
		});
	    console.log(match[1]);	
	}
    }

    console.log($location.url());

    function isCurrentQuestionActive(question) {
	return $scope.currentQuestion == question;
    }

    function setCurrentQuestion(question) {
	$scope.currentQuestion = question;
    }

    $scope.isCurrentQuestionActive = isCurrentQuestionActive;
    $scope.setCurrentQuestion = setCurrentQuestion;

    $scope.createNewQuestion = function() {
	var question = {
	    text: "Enter Question Text here",
	    pictureUrl: "http://www.keenthemes.com/preview/metronic/theme/assets/global/plugins/jcrop/demos/demo_files/image2.jpg",
	    correctAnswer: 1,
	    answers: [
		'Answer 1',
		'Answer 2',
		'Answer 3',
		'Answer 4'
	    ]
	}
	$scope.quiz.questions.push(question);
	$scope.setCurrentQuestion(question);
    }

    $scope.saveQuiz = function() {
	console.log($scope.quiz);
	$http.post("/api/quiz/1", $scope.quiz)
	.success(function(data) {
	    console.log(data);
	    $window.location.href = "/quiz/"+data;
	});
    }

    function answerSelected(index) {
	console.log("Answer selected" + index); 
    }

    $scope.answerSelected = answerSelected;

    $scope.selectQuizTitleSection = function() {
	$scope.quizTitleSelected = true;
	$scope.questionSectionSelected = false;
	$scope.shareSectionSelected = false;
	$scope.sectionTitle = "Quiz Start Template";
    }
    
    $scope.selectQuestionSection = function() {
	$scope.quizTitleSelected = false;
	$scope.questionSectionSelected = true;
	$scope.shareSectionSelected = false;
	$scope.sectionTitle = "Questions";
    }

    $scope.selectShareSection = function() {
	$scope.quizTitleSelected = false;
	$scope.questionSectionSelected = false;
	$scope.shareSectionSelected = true;
	$scope.sectionTitle = "Sharing";
    }

    $scope.selectQuizTitleSection();

})
.controller("IndexPageController", function($scope, $http) { 
    $http.get("/api/quiz")
    .success(function(data) {
	$scope.quizzes = data;
    });
});
