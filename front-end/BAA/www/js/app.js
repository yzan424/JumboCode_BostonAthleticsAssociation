// Ionic Starter App

// angular.module is a global place for creating, registering and retrieving Angular modules
// 'starter' is the name of this angular module example (also set in a <body> attribute in index.html)
// the 2nd parameter is an array of 'requires'
angular.module('starter', ['ionic'])

.run(function($ionicPlatform) {
    $ionicPlatform.ready(function() {
        if (window.cordova && window.cordova.plugins.Keyboard) {
            // Hide the accessory bar by default (remove this to show the accessory bar above the keyboard
            // for form inputs)
            cordova.plugins.Keyboard.hideKeyboardAccessoryBar(true);

            // Don't remove this line unless you know what you are doing. It stops the viewport
            // from snapping when text inputs are focused. Ionic handles this internally for
            // a much nicer keyboard experience.
            cordova.plugins.Keyboard.disableScroll(true);

        }
        if (window.StatusBar) {
            StatusBar.styleDefault();
        }

    });
})

checkCredentials = function(){
    var user = document.getElementById("user").value;
    var pass = document.getElementById("pass").value;

    var url = "api-token-auth";
    request = new XMLHttpRequest();
    request.open("POST", url);
    request.setRequestHeader("content-type", "application/x-www-form-urlencoded");

    request.onreadystatechange = function() {
        if (request.readyState == 4 && request.status == 200) {
            var token = request.responseText;
            localStorage.setItem('token',token)
            console.log(token);
            //window.location.href = "list.html";
        }

        if (request.readyState == 4 && request.status == 400) {
            alert("invalid login");
        }
    }

    request.send("username=" + user + "&password=" + pass);
};

