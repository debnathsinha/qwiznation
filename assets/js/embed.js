angular.module('quiz', [])
.controller('EmbedQuizController', function( $scope, $http, $location ) {
    $scope.startQuiz = false;

    $scope.launchQuiz = function() {
	$scope.startQuiz = true;
    }

    var regex = /\/quiz\/([a-zA-Z0-9\/]+)$/;
    var match = regex.exec($location.absUrl());
    
    $http.get("/api/quiz/" + match[1])
		.success(function(response) {
    		    console.log(response);
    		    $scope.quiz = response;
    		    $scope.currentQuestion = $scope.quiz.questions[0];
		});

});
