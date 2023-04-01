
# Address Book Application using FastApi

Address book application where API users can create, update and delete addresses. The API Users will also be able to retrieve the addresses that are within a given distance and location coordinates.


# FastAPI

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

The key features are:

* Fast: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic). One of the fastest Python frameworks available.
* Fast to code: Increase the speed to develop features by about 200% to 300%. 
* Fewer bugs: Reduce about 40% of human (developer) induced errors. *
* Intuitive: Great editor support. Completion everywhere. Less time debugging.
* Easy: Designed to be easy to use and learn. Less time reading docs.
* Short: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
* Robust: Get production-ready code. With automatic interactive documentation.
* Standards-based: Based on (and fully compatible with) the open standards for APIs: OpenAPI (previously known as Swagger) and JSON Schema.
[Documentation](https://fastapi.tiangolo.com/)


## Requirements

Python 3.7+


## Clone Project

```bash
 git clone https://github.com/rizwanshereef/Address_Book_application_FastApi
```

### Run local

### Install Dependencies

To install all the libraries

```bash
 pip install -r /path/to/requirements.txt
```

### Run Server

```bash
$ uvicorn main:app --reload

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.

```

### Interactive API docs

Now go to http://127.0.0.1:8000/docs

You will see the automatic interactive API documentation https://github.com/swagger-api/swagger-ui

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)



## API Reference

#### Get all addresses

```http
  GET /addresses
```


#### Add Address

```http
  POST /addresses
```

| Parameter       | Type     | Description                        |
| :---------------| :--------| :----------------------------------|
| `sl_no`         | `int`    | Id of item to address              |
| `name`          | `string` | **Required**. Name of the address  |
| `contact_number`| `int`    | **Required**. Contact number       |
| `address`       | `string` | **Required**. address              |
| `latitude`      | `float`  | **Required**. latitude of address  |
| `longitude`     | `float`  | **Required**. longitude of address |


#### Edit Address

```http
  PUT /addresses/{address_id}
```

| Parameter       | Type     | Description                        |
| :---------------| :--------| :----------------------------------|
| `sl_no`         | `int`    | Id of item to address              |
| `name`          | `string` | **Required**. Name of the address  |
| `contact_number`| `int`    | **Required**. Contact number       |
| `address`       | `string` | **Required**. address              |
| `latitude`      | `float`  | **Required**. latitude of address  |
| `longitude`     | `float`  | **Required**. longitude of address |

#### Delete Address

```http
  DELETE /addresses/{address_id}
```
| Parameter       | Type     | Description                        |
| :---------------| :--------| :----------------------------------|
| `address_id`    | `int`    | Id of address to be deleted              |

#### Find nearby Address

```http
  GET /addresses/nearby

  ```

| Parameter       | Type     | Description                        |
| :---------------| :--------| :----------------------------------|
| `latitude`      | `float`  | **Required**. latitude of address  |
| `longitude`     | `float`  | **Required**. longitude of address |
| `distance`      | `float`  | **Required**. nearby distance |

  