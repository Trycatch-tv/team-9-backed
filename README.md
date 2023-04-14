
# Backend Team 9

Put skills to the test in a productive environment very similar to that of a technology company.

We decided to deploy our REST API at https://render.com/. This allows us to quickly deploy our product, we try to follow a pepline using github actions in order to do continuous deployment.

The workflow was made up as follows:
- [x]  Fork the repository
- [x]  Clone repository locally
- [x]  Create new branch. Example (feat/apianddbconection)
- [x]  make changes to it
- [x]  Push to the contributor's repository
- [x]  Request Poll Request using industry standards.
- [x]  User with high knowledge approves Merge and the REST API is deployed


## Installation


Install my-project with npm

```bash
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  uvicorn main:app --reload
```

If the terminal throws the following error

```bash
  sudo lsof -t -i tcp:8000 | xargs kill -9
  python3 -m venv venv
  source venv/bin/activate
  uvicorn main:app --reload
```


## 🚀 About Me

#### Anderson Arévalo - Backend role 1


I am an electronic engineer. Passionate about creating products that can impact thousands of people.

I know how to program C, Vue js, Python ( FastApi ), NoSql ( MongoDb ) and good fundamentals in operating product launches based on beautiful and highly useful designs.

I study data sciences with a specialization in data engineering, I understand and want companies to be able to make decisions based on data.


## Deployment

To deploy this project run

```bash
  Runtime: Python3
  Build Command: pip install -r requirements.txt
  Start Command: uvicorn main:app --host 0.0.0.0 --port 10000
```


## API Reference

#### Create a new reservation


```https://back-team9.onrender.com/reservation/
  POST
```

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/reservation/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "date_reserve": "2023-04-12",
  "id_table": "6438bf0e12a189b6a5c34f4a",
  "number_people_reserve": 10,
  "name_reserve_titular": "Anderson Arévalo",
  "phone_reserve_titular": 3142058934,
  "email_reserve_titular": "hola@warocol.com",
  "active_reserve": false,
  "time_reserve": "12345678"
}'
```

#### Create table restaurant

```https://back-team9.onrender.com/reservation/
  POST
```

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/restaurant/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "location_table": "3A",
  "capacity_table": 10,
  "active_table": false
}'
```



