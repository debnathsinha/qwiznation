angular.module('quiz', [])
.controller('EmbedQuizController', function( $scope, $http, $location ) {
    $scope.startQuiz = false;

    $scope.launchQuiz = function() {
	$scope.startQuiz = true;
    }

    var regex = /\/embed\/([a-zA-Z0-9\/]+)$/;
    var match = regex.exec($location.absUrl());
    console.log(match[1]);
    
    $http.get("/api/quiz/" + match[1])
	.success(function(response) {
    	    console.log(response);
    	    $scope.quiz = response;
    	    $scope.currentQuestion = $scope.quiz.questions[0];
	    $scope.currentQuestionIndex = 0;
	})
	.error( function (response) {
	    console.log(response);
	});

    $scope.questionAnswered = function(answer) {
	if (answer == $scope.currentQuestion.correct_answer) {
	    console.log("Correct!");
	} else {
	    console.log("Wrong!");
	}
	$scope.currentQuestion = $scope.quiz.questions[++$scope.currentQuestionIndex];
    }
});
