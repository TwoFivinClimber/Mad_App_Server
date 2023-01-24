UPDATE mad_api_event
SET public = 0
WHERE id=4

DELETE from mad_api_event
WHERE description = "This is a test"

DELETE from mad_api_photo
WHERE id = 20
