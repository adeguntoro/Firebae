var ref = firebase.database().ref();
var sensorRef = ref.child("Sensor1");
function simpan() {
//    sensorRef.set({
//        Level       : "300",
//        Presentase  : "500"
//    });
//    console.log();
}
function lihat() {
    sensorRef.child("Sensor1/Level").on("value", function(snapshot) {
        console.log(snapshot.val());
    });
}