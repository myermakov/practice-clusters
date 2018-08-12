var camera = new THREE.PerspectiveCamera( 
    75, 
    window.innerWidth/window.innerHeight, 
    1, 500 );
camera.position.set(0,0,100);
camera.lookAt( new THREE.Vector3(0,0,0));


var scene = new THREE.Scene();

var renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

var geometry = new THREE.Geometry();

geometry.vertices.push( new THREE.Vector3(-10,0,0));
geometry.vertices.push( new THREE.Vector3(0,10,0));
geometry.vertices.push( new THREE.Vector3(10,0,0));


//var material = new THREE.MeshBasicMaterial( { color: 0x00ffaa } );
var material = new THREE.LineBasicMaterial({
            color: 0x0000ff
        });

var line = new THREE.Line( geometry, material);
//var cube = new THREE.Mesh( geometry, material );
//scene.add( cube );
scene.add( line ); 
//camera.position.z = 2;
renderer.render( scene, camera );




