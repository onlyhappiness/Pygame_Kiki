extends Node2D

var enemy_scene = preload("res://screens/Enemy.tscn")

onready var spawn_positions = $SpawnPositions

func _on_Timer_timeout():
	spawn_enemy()

func spawn_enemy():
	var spawn_position_array = [
		'50',
		'175',
		'300',
		'425',
		'550',
		'675'
	]
	
	
	var enemy_instance = enemy_scene.instance()
	enemy_instance.global_position = Vector2(1350, 300)
	
	add_child(enemy_instance)
