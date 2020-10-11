curl -X POST -d "username=check&password=check" http://127.0.0.1:8000/api/users/token/obtain/

curl --header "Content-Type: application/json" -X POST http://127.0.0.1:8000/api/users/token/refresh/ --data '{"refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU5OTg2MzI2MSwianRpIjoiZTZiYzgzYzc2ZGFhNDc5N2ExNDAzYTBhNzk5YTQ3YjgiLCJ1c2VyX2lkIjoxfQ.OiAudFYrO2i3DSt6q2_96lvag5WU9OhD_-bM5fwBQmU"}'

curl --header "Content-Type: application/json" -X POST http://127.0.0.1:8000/api/users/register/ --data '{"email":"check@user.com","email2":"check@user.com","username":"check","password":"check"}'

curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAwMDcxODYwLCJqdGkiOiI2MTM4YTg3NjZhNzY0MDk1YjQ1NTg1YjllMjAyZDNjMSIsInVzZXJfaWQiOjN9.t1xZAhboYkUFjQyKN5GDsqFLTmW4w_CUuhhatfPq8W8" http://127.0.0.1:8000/api/comments/4/like/

curl http://127.0.0.1:8000/api/users/hello/

curl -X POST -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTk4NjU3NjMzLCJqdGkiOiIyOTMyNjhmYzE0NzE0ZmMwYmRhOGVjNjM0ODBkMWVlYSIsInVzZXJfaWQiOjR9.ZJPzI72e-9X1oRalnDGRwTdCFobGa454h4hC9d8T4vI" -H "Content-Type: application/json" -d '{"content":"This is from curl"}' 'http://127.0.0.1:8000/api/comments/create/?slug=admin&type=post'

127.0.0.1:8000/api/profile/check/follow

curl --header "Content-Type: application/json" --header "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTk5MDYyMDEwLCJqdGkiOiI1ZjA2N2NiMDFlYzE0ZmEyYTJjOWI1MTExYWNlYTg3YSIsInVzZXJfaWQiOjd9.vten_aNdNUwGe1fJ3AbnaaMG7vQeoSqd1TUY_3vwtfs"  -X GET http://127.0.0.1:8000/api/users/hello/

# Curl for Follow

curl -X POST -d "username=teokoul&password=sirenakosone1" http://127.0.0.1:8000/api/users/token/obtain/

curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTk4OTkyOTYzLCJqdGkiOiI4MTJiNzMxNjUzMTA0N2VmYWViOWU3MTQ4NzY1NzU3ZSIsInVzZXJfaWQiOjJ9.IU8-KKWBxjyZjLCKsmRezyMx96zeTj43tjPI6XEM6Y8" 127.0.0.1:8000/api/profile/check/follow/

