var firePersen  = document.querySelector('persenan');
//var database = firebase.database();
var firePersenRef = firebase.database().ref().child('Sensor1/Level');
firePersenRef.on('value', function (datasnapshot) {
    firePersen.innerHTML = datasnapshot.val()
});