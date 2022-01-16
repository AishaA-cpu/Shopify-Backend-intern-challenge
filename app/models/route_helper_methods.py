from http import HTTPStatus


class Route_helpers:
    def record_not_found(record, record_id):
        return {
            "message" : f"{record} {record_id} not found"
        }, HTTPStatus.NOT_FOUND

