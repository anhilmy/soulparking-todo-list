from flask import Flask, Response, jsonify, request, Blueprint
from flask.views import MethodView
from component.error import ValidationError

from model.todo_list import TodoListModel

SUCCESS_MSG = "Success"
FAILED_MSG = "Failed"


class ItemTodoListController(MethodView):
    init_every_request = False

    def __init__(self, model: TodoListModel):
        self.model = model

    def get(self, id):
        item = self.model.get_by_id(id)
        if not item:
            return jsonify({"data": {}, "message": FAILED_MSG}), 400
        else:
            return jsonify({"data": item.detail(), "message": SUCCESS_MSG})

    def patch(self, id):
        try:
            body = request.json
            self.model.validate(**body)
            todo = self.model.get_by_id(id)
            if not todo:
                raise TypeError("Not Found")
        except ValidationError as e:
            return jsonify({"data": {}, "message": str(e)}), 400
        except TypeError:
            return jsonify({"data": {}, "message": FAILED_MSG}), 400

        todo.update(**body)
        return jsonify({"data": {"id": todo.id}, "message": SUCCESS_MSG}), 200

    def delete(self, id):
        item = self.model.get_by_id(id)
        if not item:
            return jsonify({"data": {}, "message": FAILED_MSG}), 400

        item.delete()
        return jsonify({"data": {}, "message": SUCCESS_MSG}), 200


class GroupTodoListController(MethodView):
    init_every_request = False

    def __init__(self, model):
        self.model = model

    def get(self):
        items = self.model.get_all()
        return jsonify(
            {"data": [item.detail() for item in items], "message": SUCCESS_MSG}
        )

    def post(self):
        try:
            body = request.json
            self.model.validate(**body)
        except ValidationError as e:
            return jsonify({"data": {}, "message": str(e)}), 400

        todo_inst = self.model.create(**request.json)

        return jsonify({"data": {"id": todo_inst.id}, "message": SUCCESS_MSG}), 201


class DoneTodoListController(MethodView):
    init_every_request = False

    def __init__(self, model):
        self.model = model

    def post(self, id):
        try:
            todo = self.model.get_by_id(id)
            if not todo:
                raise TypeError("Not Found")
        except TypeError:
            return jsonify({"data": {}, "message": FAILED_MSG}), 400

        todo.complete()
        return jsonify({"data": {"id": todo.id}, "message": SUCCESS_MSG}), 200


def register_todo_list():
    blueprint = Blueprint("todo_list", __name__, url_prefix="/todo")

    item_todo = ItemTodoListController.as_view(f"todo-item", TodoListModel)
    group_todo = GroupTodoListController.as_view(f"group-todo", TodoListModel)
    complete_todo = DoneTodoListController.as_view("completed_todo", TodoListModel)
    blueprint.add_url_rule(f"/<int:id>", view_func=item_todo)
    blueprint.add_url_rule(f"/", view_func=group_todo)
    blueprint.add_url_rule(f"/<int:id>/finish", view_func=complete_todo)

    return blueprint
