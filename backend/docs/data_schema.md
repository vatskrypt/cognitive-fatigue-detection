## MongoDB Schemas

### `sessions` collection

```json
{
  "_id": ObjectId,
  "start_time": ISODate,
  "end_time": ISODate or null,
  "metadata": {}
}
```

### `features` collection

```json
{
  "_id": ObjectId,
  "session_id": ObjectId,
  "timestamp": ISODate,
  "typing_speed": float,
  "error_rate": float,
  "mouse_click_rate": float,
  "created_at": ISODate
}
```
