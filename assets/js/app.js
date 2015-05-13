angular.module('qw', [])
.controller('QwController', function($scope, $http) {
    $scope.name = "Game of Thrones";
    // $http.get('quiz')
    // .success(function(data) {
    // 	console.log(data);
    // })
    // .error(function(msg) {
    // 	console.log(msg);
    // });

    $scope.question = {
	title: "Is Winter coming?",
	picUrl: "http://www.online-image-editor.com//styles/2014/images/example_image.png",
	answers: [
	    "Yes",
	    "No",
	    "Maybe",
	    "Never"
	]
    };
    console.log($scope.question.title);

    $scope.quiz = {
	name: 'Game of Thrones',
	result: 'Winter is coming!',
	questions: [
	    {
		text: 'Which house does Joffrey belong to?',
		pictureUrl: 'http://www.keenthemes.com/preview/metronic/theme/assets/global/plugins/jcrop/demos/demo_files/image2.jpg',
		correctAnswer: 1,
		answers: [
		    'Yes',
		    'No'
		]
	    },
	    {
		text: 'What is the name of the central Bank?',
		pictureUrl: 'http://www.keenthemes.com/preview/metronic/theme/assets/global/plugins/jcrop/demos/demo_files/image2.jpg',
		correctAnswer: 3,
		answers: [
		    'Tywin Lannister',
		    'Tyrion Lannister',
		    'Jamie Lannister',
		    'Cersei Lannister'
		]
	    },
	    {
		text: "What is Sean Bean's name in the series?",
		pictureUrl:'http://www.keenthemes.com/preview/metronic/theme/assets/global/plugins/jcrop/demos/demo_files/image2.jpg',
		correctAnswer: 1,
		answers: [
		    'Iron Bank',
		    'Gold Bank',
		    'Lannister Bank',
		    'Bank of America'
		]
	    }]
    }

    $scope.currentQuestion = $scope.quiz.questions[0];

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

})
.controller('QwHeaderController', function($scope) {
    $scope.yourName = "Debnath";
});
