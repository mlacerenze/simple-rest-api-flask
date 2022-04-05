from flask import Flask, jsonify, request, Blueprint
from datetime import datetime
from database import tasks, setup
# from database import tasks, setup

task_bp = Blueprint('routes-tasks', __name__)
setup.create_tables()

@task_bp.route('/tasks', methods=['POST'])
def add_task():
  title = request.json['title']  # request.json is a dict
  created_date = datetime.now().strftime("%x")

  data = (title, created_date)
  task_id = tasks.insert_task(data)

  if task_id:
    task = tasks.select_task_by_id(task_id)
    return jsonify({'message': task})
  return jsonify({'message': 'An error occurred'})


@task_bp.route('/tasks', methods=['GET'])
def get_tasks():
  data = tasks.select_all_tasks()
  if data: 
    return jsonify({'tasks': data})
  elif data == False:
    return jsonify({'message': 'An error occurred'})
  else:
    return jsonify({'message': {}})


@task_bp.route('/tasks', methods=['PUT'])
def update_task(): 
  title = request.json['title']
  id_arg = request.args.get('id')
  
  if tasks.update_task(id_arg, (title,)):
    task = tasks.select_task_by_id(id_arg)
    return jsonify({'message': task})
  return jsonify({'message': 'An error occurred'})  


@task_bp.route('/tasks', methods=['DELETE'])
def delete_task():
  id_arg = request.args.get('id')
  if tasks.delete_task(id_arg):
    return jsonify({'message': 'Task deleted'})
  return jsonify({'message': 'An error occurred'})


@task_bp.route('/tasks/completed', methods=['PUT'])
def completed_task():
  id_arg = request.args.get('id')
  completed = request.args.get('completed')
  if tasks.complete_task(id_arg, completed):
    task = tasks.select_task_by_id(id_arg)
    return jsonify({'message': 'Successfully completed task'})
  return jsonify({'message': 'An error occurred'})


@task_bp.route('/')
def index():
  return '<h1>Welcome to my REST API!</h1>'