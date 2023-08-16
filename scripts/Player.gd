extends KinematicBody2D

var speed = 300
var screen_size = get_viewport_rect().size

func _physics_process(delta):
	var velocity = Vector2(0,0)
	
	if Input.is_action_pressed("ui_left"):
		velocity.x = -speed
	if Input.is_action_pressed("ui_right"):
		velocity.x = speed
	if Input.is_action_pressed("ui_up"):
		velocity.y = -speed
	if Input.is_action_pressed("ui_down"):
		velocity.y = speed
		
	velocity = velocity.normalized() * speed
	move_and_slide(velocity)
	
	if global_position.x < 0:
		global_position.x = 0
	if global_position.y < 0:
		global_position.y = 0
	if global_position.x > 1280:
		global_position.x = 1280
	if global_position.y > 720:
		global_position.y = 720
		

		
#	if global_position.x > screen_size.x:
#		global_position.x = screen_size.x
#	if global_position.y > screen_size.y:
#		global_position.y = screen_size.y
	
	
