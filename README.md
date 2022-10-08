# crud_django
## API endpoints
status: ["id","name","created_at","updated_at"]

todo: ["id", "name", "status", "crested_at", "updated_at", "is_completed"] status is FK of status table.

## CRUD operation status table

CREATE -> /api/status/(POST) 

READ -> all, id->status detail -> /api/status/(GET), /api/status/{status_id}/(GET particular status)

UPDATE -> /api/status/{status_id}/(PUT)

DELETE -> /api/status/{status_id}/(DELETE)

## CRUD operation todo table

CREATE -> /api/todo/(POST) // no required

READ -> all, id->status detail -> /api/todo/(GET), /api/todo/{todo_id}/(GET particular status)

UPDATE -> /api/todo/{todo_id}/(PUT)

DELETE -> /api/todo/{todo_id}/(DELETE)

/api/status/{status_id}/todos -> GET(List of all todos under status) POST(create todo under status)


```
GET - {
 id: "",
 name: "",
 created_at: "",
 updated_at: "",
 todo: [
   {}, {}, {}
 ]
}
```

```
POST - {
 name: "",
 is_completed: ""
}
```
