angular.module('quiz', [])
.controller('QuizController', function($scope, $http) {
    $scope.foo = "bar";
    $http.get("/api/quiz")
    .success(function(response) {
	$scope.quizzes = response;
	for (quiz in $scope.quizzes) {
	    $scope.quizzes[quiz].url = "/quiz/" + $scope.quizzes[quiz].id + "/edit";
	}
    });
    QuizService.sayHello();
});
