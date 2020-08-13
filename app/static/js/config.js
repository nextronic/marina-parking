
//Variable
var socket = io.connect('http://localhost:5000'),
	data = {
		"devices": [],
		"lines": [],
		"capteurs": []
	},
	deviceModal = document.querySelector('#device'),
	list_icones = document.querySelector('#icones'),
	colors = ['#1E90FF', '#FF1493'],
	selectedColor,
	customColor,
	colorButtons = {},
	polyline ="",
	x = 0,
	y = 0,
	coordinates,
	modalId = 0,
	format="",
	formDev = $("#formDevice"),
	formLine = $("#FormLines"),
	formCap = $("#FormCapteur"),
	map = L.map('map').setView([31.58831, -7.11138], 6);
	L.tileLayer('https://via.placeholder.com/{z}/{x}/{y}.png').addTo(map);

	//change Image Device By Socket
	socket.on('data_devices', function (result) {
		clearBtn.onclick = (e) => {
			let res_device = result.filter(res => res.id === id_layer.value)
			let _id = res_device[0].id
			id_layer.value !== _id ? drawnItems._layers[id_layer.value]._icon.src : drawnItems._layers[id_layer.value]._icon.src = document.querySelector("#image_1").src
		};
		useBtn.onclick = (e) => {
			let res_device = result.filter(res => res.id === id_layer.value)
			let _id = res_device[0].id
			id_layer.value !== _id ? drawnItems._layers[id_layer.value]._icon.src : drawnItems._layers[id_layer.value]._icon.src = document.querySelector("#image_2").src
		};
		warBtn.onclick = (e) => {
			let res_device = result.filter(res => res.id === id_layer.value)
			let _id = res_device[0].id
			id_layer.value !== _id ? drawnItems._layers[id_layer.value]._icon.src : drawnItems._layers[id_layer.value]._icon.src = document.querySelector("#image_3").src
		};
	})

//Initial Map
var drawnItems = new L.FeatureGroup();
map.addLayer(drawnItems);
var drawControl = new L.Control.Draw({
	edit: {
		featureGroup: drawnItems,
		remove: false
	}
});//End Draw Control

var customMarker = L.Icon.extend({
	options: {
		iconSize: new L.Point(30, 30),
		iconUrl: "https://img.icons8.com/dusk/64/000000/garage--v1.png",
	}
});

L.Draw.Capteur = L.Draw.Marker.extend({
	statics : {
		TYPE :'capteur'
	},
	options: {
		icon: new customMarker(),
		repeatMode: false,
		zIndexOffset: 2000 // This should be > than the highest z-index any markers
	},
	initialize: function (map, options) {
		// Save the type so super can fire, need to do this as cannot do this.TYPE :(
		this.type = L.Draw.Capteur.TYPE;

		L.Draw.Feature.prototype.initialize.call(this, map, options);
	}
})//End Draw Capteur

//Custom Icon Toolbar
L.DrawToolbar.prototype.getModeHandlers = function(map){
	return [{
		enabled: true,
		handler: new L.Draw.Polygon(map, {
			allowIntersection: false,
			showArea: true,
			metric: true,
			repeatMode: false,
			shapeOptions: {
				color: "#F2F2F2",
				weight: 5,
				fillOpacity: .5
			}
		}),
		title: 'Add Line ',
	},
	{
		enabled: true,
		handler: new L.Draw.Marker(map, { icon: new L.Icon.Default() }),
		title: 'Add Device'
	},
	{
		enabled: true,
		handler: new L.Draw.Capteur(map, this.options.capteur),
		title: 'Add Capteur',
	}
	];
};
map.addControl(drawControl);


$.validator.addMethod('ip', function(value) {
	var ip = /^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/;
	return value.match(ip);
}, 'Invalid IP address');


$.validator.addMethod('index', function(value) {
	var index =/^[-+]?[0-9]+$/
	return value.match(index);
}, 'Invalid Index');


$.validator.addMethod("letters", function(value, element) {
	return this.optional(element) || value == value.match(/^[a-zA-Z\s]*$/);
});
/**************************** Start DEVICE  **********************************************/
$("#formDevice").validate({
	rules :{
		fname :{
      required: true,
      minlength: 3,
      letters: true
		},
		ip :{
			required: true,
			ip:true
		},
		serial_dev :{
			required:true,
			minlength:10,
			number:true
		},
		port :{
			required:true,
			minlength: 1,
			number: true
		}
	},//End if Rules
	messages: {
    fname: "Please specify your name (only letters and spaces are allowed)",
    ip: "Please specify a valid Ip",
    serial_dev: "Please specify a valid Serial number",
    port: "Please specify a valid Port",
	}
});
formDev.on("submit", function (e) {
	e.preventDefault();
		if(formDev.valid()) {
			let result = data.devices.filter(marker => marker.id === modalId);
			if (result.length == 0) {
				data.devices.push({
					id: modalId,
					fname: fname.value,
					x: x,
					y: y,
					ip:ip.value,
					serial_dev:serial_dev.value,
					port:port.value
				});
				this.reset()
				socket.emit('device', data.devices)
				$('#device').modal('toggle');
			} else {
				result[0].fname = fname.value;
				$('#device').modal('toggle');
			}
	}//End if
	});//End Form Device
/**************************** End DEVICE  **********************************************/

/**************************** Start Lines  **********************************************/
$("#FormLines").validate({
	rules :{
		nameL :{
      required: true,
      minlength: 3,
      letters: true
		},
		serial_cap :{
			required:true,
			minlength:10,
			number:true
		},
		index_queue :{
			required: true,
			index:true,
			number:true
		},
	},//End if Rules
	messages: {
    nameL: "Please specify your name (only letters and spaces are allowed)",
    serial_cap: "Please Valide Serial Number",
    index: "Please Valide Index",
	}
});
formLine.on("submit", function (e) {
	e.preventDefault();
		if(formLine.valid()) {
			let result = data.lines.filter(lines => lines.id === modalId);
			if (result.length == 0) {
				data.lines.push({
					id: modalId,
					nameL: nameL.value,
					index_queue: index_queue.value,
					coordinates :coordinates
				});
				this.reset()
				socket.emit('line', data.lines)
				$('#lines').modal('toggle');
			} else {
				result[0].nameL = nameL.value;
				$('#lines').modal('toggle');
			}
			}//End if
	});//End Form Line
/**************************** End Lines  **********************************************/

/**************************** Start Capteur  **********************************************/
$("#FormCapteur").validate({
	rules :{
		name_cap :{
      required: true,
      minlength: 3,
      letters: true
		},
		serial_cap :{
			required:true,
			minlength:10,
			number:true
		},
		index_cap :{
			required: true,
			index:true
		}
	},//End if Rules
	messages: {
    nameL: "Please specify your name (only letters and spaces are allowed)",
    index_queue: "Please Valide Index",
	}
});

formCap.on("submit", function (e) {
	e.preventDefault();
	if(formCap.valid()) {
		let result = data.capteurs.filter(capteur => capteur.id === modalId);
	if (result.length == 0) {
		data.capteurs.push({
			id: modalId,
			name_cap: name_cap.value,
			serial_cap: serial_cap.value,
			index_cap: index_cap.value,
			x: x,
      y: y
		});
		this.reset()
		socket.emit('capteur', data.capteurs)
		$('#capteur').modal('toggle');
	} else {
		result[0].nameC = nameC.value;
		$('#capteur').modal('toggle');
	}
	}

	});//End Form Cap
/**************************** End Capteur  **********************************************/





map.on(L.Draw.Event.CREATED, function (event) {
	var thisLayer,
			getIdClick;
	var type = event.layerType,
			layer = event.layer;
			drawnItems.addLayer(layer),
			modalId = layer._leaflet_id
			if (type === 'polygon') {
				$("#lines").modal();
				$('#color-palette').css('display', 'none')
				console.log(layer.getLatLngs())
					coordinates =layer.getLatLngs()
					socket.on('data_lines',function(resLines){
						layer.addEventListener('click', function (e) {
							getIdClick =e.target._leaflet_id
							let result = resLines.filter(resL => resL.id == getIdClick);
							if (result.length != 0) {
								nameL.value = result[0].nameL;
								index_queue.value = result[0].index_queue;
							}
						})//End Layer Clicked
						$(document).on("click","path.leaflet-interactive", function(e){
							thisLayer = $(this);
							$('#color-palette').css('display', 'block')
							$('#lines').modal('show');
						})
						$(document).on('click','#color-palette .color-button',function(){
							var colorSelected = $(this).css("backgroundColor");
							changeColor(thisLayer, colorSelected)
						})
					})
					closeL.addEventListener('click', function (e) {
						if (nameL.value === '') {
							map.eachLayer(function (layer) {
								map.removeLayer(drawnItems._layers[modalId])
							})
						}
					})
			}
			if (type === 'marker') {
					id_layer.value = layer._leaflet_id
					x = layer._latlng.lat,
					y = layer._latlng.lng
				$("#device").modal();
				layer.addEventListener('click', function (e) {
					id_layer.value = modalId = e.target._leaflet_id
					$('#device').modal('show');
					let result = data.devices.filter(device => device.id == e.target._leaflet_id);
          if (result.length !== 0) {
						fname.value = result[0].fname;
						ip.value = result[0].ip;
						serial_dev.value = result[0].serial_dev;
						port.value = result[0].port;
					}
					$('#device').modal('toggle');
				})
				closeD.addEventListener('click', function (e) {
					if (fname.value === '') {
						map.eachLayer(function (layer) {
							map.removeLayer(drawnItems._layers[modalId])
						})
					}
				})
			}
			if (type === 'capteur') {
					id_layer.value = layer._leaflet_id
					x = layer._latlng.lat,
					y = layer._latlng.lng
				$("#capteur").modal();
				layer.addEventListener('click', function (e) {
					id_layer.value = modalId = e.target._leaflet_id
					$('#capteur').modal('show');
					let result = data.capteurs.filter(capteur => capteur.id == e.target._leaflet_id);
					if (result.length !== 0) {
						name_cap.value = result[0].name_cap;
						serial_cap.value = result[0].serial_cap;
						index_cap.value = result[0].index_cap;
					}
					$('#capteur').modal('toggle');
				})
				closeC.addEventListener('click', function (e) {
					if (name_cap.value === '') {
						map.eachLayer(function (layer) {
							map.removeLayer(drawnItems._layers[modalId])
						})
					}
				})
			}
});

map.on(L.Draw.Event.EDITED, function (e) {
	var layers = e.layers;

	SubmitFormDev.reset();
	layers.eachLayer(function (layer) {
		var LineId = L.stamp(layer);
		if (layers.toGeoJSON().features[0].geometry.type === 'Polygon') {
			let coordinates = layers.toGeoJSON().features[0].geometry.coordinates
			for (var i in data.lines) {
				if (LineId == data.lines[i].id) {
					data.lines[i].x1 = coordinates[0][0]
					data.lines[i].y1 = coordinates[0][1]
					data.lines[i].x2 = coordinates[0][2]
					data.lines[i].y2 = coordinates[0][3]
				}
			}
		}
	})

	values = drawnItems._layers;
	for (var key in values) {
		for (var i in data.devices) {
			if (key == data.devices[i].id) {
				data.devices[i].x = values[key]._latlng.lat
				data.devices[i].y = values[key]._latlng.lng
			}
		}
	}
	for (var key in values) {
		for (var i in data.capteurs) {
			if (key == data.capteurs[i].id) {
				data.capteurs[i].x = values[key]._latlng.lat
				data.capteurs[i].y = values[key]._latlng.lng
			}
		}
	}
});

//Get Data & Print if from html
document.querySelector('#data').addEventListener('click', function () {
	document.querySelector('.line').innerHTML = JSON.stringify(data)
})

//Show Icon from Marker Created
function ShowIcon(input, selector) {
	if (input.files && input.files[0]) {
		var reader = new FileReader();
		reader.onload = function (e) {
			$('#' + selector).attr('src', e.target.result)
		};
		reader.readAsDataURL(input.files[0]);
	}
}

function selectColor(color) {
	selectedColor = color;
	for (var i = 0; i < colors.length; i++) {
		let currentColor = colors[i]
		colorButtons[currentColor].style.border = currentColor == color ? '2px solid #333' : '2px solid #fff';
	}
}

buildColorPalette();

function buildColorPalette() {
	var colorPalette = document.getElementById('color-palette');
	for (var i = 0; i < colors.length; ++i) {
		var currColor = colors[i];
		var colorButton = makeColorButton(currColor);
		//Lines
		colorPalette.appendChild(colorButton);
		colorButtons[currColor] = colorButton;
	}
	selectColor(colors);
}

function makeColorButton(color) {
	var button = document.createElement('span');
	button.className = 'color-button';
	button.style.backgroundColor = color;

	L.DomEvent.addListener(button, 'click', function (e) {
		selectColor(color);
	});
	return button;
}

function changeColor(element, colorSelected) {
	element.attr({
		fill: colorSelected,
		stroke: colorSelected
	})
}