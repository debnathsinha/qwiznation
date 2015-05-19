angular.module('quiz', [])
.controller('QuizController', function($scope, $http) {
    $scope.foo = "bar";
    $http.get("/api/quiz")
    .success(function(response) {
	$scope.quizzes = response;
	$scope.quizzes = [ 
	    {
		"name": "Game of Thrones"
	    },
	    {
		"name": "Dexter"
	    }, 
	    {
		"name": "Blacklist"
	    }];
    });
});
