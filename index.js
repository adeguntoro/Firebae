var firePersen  = document.querySelector('persenan');
var fireLevel   = document.querySelector('level');

var firePersenRef = firebase.database().ref('Sensor1').child('Persentase');
firePersenRef.on('value', function (datasnapshot) {
    firePersen.innerHTML = datasnapshot.val()
});

var fireLevelRef = firebase.database().ref('Sensor1').child('Level');
fireLevelRef.on('value', function (datasnapshot) {
    fireLevel.innerHTML = datasnapshot.val()
});