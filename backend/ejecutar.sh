#!/usr/bin/env sh

psql -d project_dbp -a -f "sql/script_uuid.sql"

export FLASK_APP=app/
export FLASK_DEBUG=true
flask run --port=5002
