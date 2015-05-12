angular.module('qw', [])
.controller('QwController', function($scope) {
    $scope.name = "Game of Thrones";
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
