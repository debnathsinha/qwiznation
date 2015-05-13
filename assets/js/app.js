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
		text: 'Is winter coming?',
		pictureUrl: 'http://www.keenthemes.com/preview/metronic/theme/assets/global/plugins/jcrop/demos/demo_files/image2.jpg',
		correctAnswer: 1,
		answers: [
		    'Yes',
		    'No'
		]
	    },
	    {
		text: 'Who is the Kingslayer?',
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
		text: 'What is the name of the Bank?',
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
})
.controller('QwHeaderController', function($scope) {
    $scope.yourName = "Debnath";
});
