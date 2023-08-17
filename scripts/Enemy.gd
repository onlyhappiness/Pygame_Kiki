extends Area2D


var speed = 400

func _physics_process(delta):
	global_position.x +=  -speed * delta
