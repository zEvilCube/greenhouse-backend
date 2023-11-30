from flask import Blueprint, jsonify, make_response, request, abort
from database import auth, readings, references, statuses

blueprint = Blueprint("api", __name__)


@blueprint.route("/echo")
def echo_handler():
    return make_response(jsonify(request.args))


@blueprint.route("/auth", methods=["GET"])
def auth_handler():
    validate_api_key(request.args.get("api_key", None, str))
    return make_response({}, 200)


@blueprint.route("/readings", methods=["GET"])
def readings_handler():
    greenhouse_id = validate_api_key(request.args.get("api_key", None, str))
    readings_dict = readings.get(greenhouse_id)
    if readings_dict is None:
        return make_response({}, 404)
    return make_response(jsonify(readings_dict), 200)


@blueprint.route("/readings", methods=["PUT"])
def readings_updater():
    readings.update(
        validate_api_key(request.json.get("api_key")),
        request.json.get("light"),
        request.json.get("temperature"),
        request.json.get("humidity")
    )
    return make_response({}, 202)


@blueprint.route("/references", methods=["GET"])
def references_getter():
    greenhouse_id = validate_api_key(request.args.get("api_key", None, str))
    references_dict = references.get(greenhouse_id)
    if references_dict is None:
        return make_response({}, 404)
    return make_response(jsonify(references_dict), 200)


@blueprint.route("/references", methods=["PUT"])
def references_updater():
    references.update(
        validate_api_key(request.json.get("api_key")),
        request.json.get("light"),
        request.json.get("temperature"),
        request.json.get("humidity")
    )
    return make_response({}, 202)


@blueprint.route("/statuses", methods=["GET"])
def statuses_getter():
    greenhouse_id = validate_api_key(request.args.get("api_key", None, str))
    statuses_dict = statuses.get(greenhouse_id)
    if statuses_dict is None:
        return make_response({}, 404)
    return make_response(jsonify(statuses_dict), 200)


@blueprint.route("/statuses", methods=["PUT"])
def statuses_updater():
    statuses.update(
        validate_api_key(request.json.get("api_key")),
        request.json.get("lighting"),
        request.json.get("heating"),
        request.json.get("cooling"),
        request.json.get("watering")
    )
    return make_response({}, 202)


def validate_api_key(api_key: str | None) -> int:
    if api_key is None:
        return abort(400)
    greenhouse_id = auth.get(api_key)
    if greenhouse_id is None:
        return abort(401)
    return greenhouse_id
