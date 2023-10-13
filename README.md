**Retrieve User Information**
----
  Retrieve specific user details by their unique ID, mobile number, or email address..
* **URL Params**
  None
* **Data Params**
  None
* **Headers**
  Content-Type: application/json
  Authorization: Bearer `<OAuth Token>`
* **Success Response:**
* **Code:** 200
  **Content:**  `{ <user_object> }`
* **Error Response:**
  * **Code:** 404
  **Content:** `{ error : "User doesn't exist" }`
  OR
  * **Code:** 401
  **Content:** `{ error : error : "You are unauthorized to make this request." }`
**Update User Information**
----
  Modify user information, including first name, last name, email, mobile number, password, and activation status..
* **URL Params**
  None
* **Data Params**
  ```json
{
  "content": {
    "application/json": {
      "schema": {
        "type": "object",
        "properties": {
          "first_name": {
            "type": "string"
          },
          "last_name": {
            "type": "string"
          },
          "email": {
            "type": "string",
            "description": "Providing a new email temporarily sets the email verification status to false.",
            "format": "email"
          },
          "mobile": {
            "type": "string",
            "description": "Providing a new email temporarily sets the email verification status to false."
          },
          "password": {
            "type": "string",
            "format": "password"
          },
          "is_active": {
            "type": "boolean",
            "default": true
          }
        }
      },
      "examples": {
        "Update First Name": {
          "value": {
            "first_name": "Updated Jane"
          }
        },
        "Update Last Name": {
          "value": {
            "last_name": "Updated Smith"
          }
        },
        "Update Email and Mobile": {
          "value": {
            "email": "updated.jane.smith@gmail.com",
            "mobile": "347-123-9876"
          }
        },
        "Update Password": {
          "value": {
            "password": "newSecretPwd"
          }
        },
        "Update Activation Status": {
          "value": {
            "is_active": false
          }
        },
        "Combined Updates": {
          "value": {
            "first_name": "Combined",
            "last_name": "Updates",
            "email": "combined.updated@gmail.com",
            "mobile": "347-987-1234",
            "password": "complexPassword",
            "is_active": true
          }
        }
      }
    }
  }
}
  ```
* **Headers**
  Content-Type: application/json
  Authorization: Bearer `<OAuth Token>`
* **Success Response:**
* **Code:** 200
  **Content:**  `{ <user_object> }`
* **Error Response:**
  * **Code:** 404
  **Content:** `{ error : "User doesn't exist" }`
  OR
  * **Code:** 401
  **Content:** `{ error : error : "You are unauthorized to make this request." }`
**Delete User**
----
  Permanently remove an existing user and their associated data..
* **URL Params**
  None
* **Data Params**
  ```json
{
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/User"
      },
      "examples": {
        "Delete User Example": {
          "value": {
            "id": 136,
            "first_name": "Jane",
            "last_name": "Smith",
            "email": "jane.smith@gmail.com",
            "mobile": "347-123-4567",
            "username": "janesmith",
            "password": "s3cretPwd",
            "email_verified": true,
            "is_active": true
          }
        }
      }
    }
  }
}
  ```
* **Headers**
  Content-Type: application/json
  Authorization: Bearer `<OAuth Token>`
* **Success Response:**
* **Code:** 200
  **Content:**  `{ <user_object> }`
* **Error Response:**
  * **Code:** 404
  **Content:** `{ error : "User doesn't exist" }`
  OR
  * **Code:** 401
  **Content:** `{ error : error : "You are unauthorized to make this request." }`
**Create New User**
----
  Add a new user.
* **URL Params**
  None
* **Data Params**
  ```json
{
  "content": {
    "application/json": {
      "schema": {
        "type": "object",
        "x-examples": {
          "Example 1": {
            "first_name": "David",
            "last_name": "Gavin",
            "email": "davidg@gmail.com",
            "mobile": "347-123-4567",
            "username": "davidg",
            "password": "s3cr3tp@assw0rd"
          }
        },
        "properties": {
          "first_name": {
            "type": "string"
          },
          "last_name": {
            "type": "string"
          },
          "email": {
            "type": "string"
          },
          "mobile": {
            "type": "string"
          },
          "username": {
            "type": "string"
          },
          "password": {
            "type": "string",
            "format": "password"
          }
        }
      },
      "examples": {
        "Create User David Gavin": {
          "value": {
            "first_name": "David",
            "last_name": "Gavin",
            "email": "davidg@gmail.com",
            "mobile": "347-123-4567",
            "username": "davidg",
            "password": "s3cr3tp@assw0rd"
          }
        }
      }
    }
  },
  "description": "Create a new user with the specified details."
}
  ```
* **Headers**
  Content-Type: application/json
  Authorization: Bearer `<OAuth Token>`
* **Success Response:**
* **Code:** 200
  **Content:**  `{ <user_object> }`
* **Error Response:**
  * **Code:** 404
  **Content:** `{ error : "User doesn't exist" }`
  OR
  * **Code:** 401
  **Content:** `{ error : error : "You are unauthorized to make this request." }`
**Get All Users**
----
  Retrieve a list of all users.
* **URL Params**
  None
* **Data Params**
  None
* **Headers**
  Content-Type: application/json
  Authorization: Bearer `<OAuth Token>`
* **Success Response:**
* **Code:** 200
  **Content:**  `{ <user_object> }`
* **Error Response:**
  * **Code:** 404
  **Content:** `{ error : "User doesn't exist" }`
  OR
  * **Code:** 401
  **Content:** `{ error : error : "You are unauthorized to make this request." }`
**Retrieve User Information**
----
  Retrieve specific user details by their unique ID..
* **URL Params**
  None
* **Data Params**
  None
* **Headers**
  Content-Type: application/json
  Authorization: Bearer `<OAuth Token>`
* **Success Response:**
* **Code:** 200
  **Content:**  `{ <user_object> }`
* **Error Response:**
  * **Code:** 404
  **Content:** `{ error : "User doesn't exist" }`
  OR
  * **Code:** 401
  **Content:** `{ error : error : "You are unauthorized to make this request." }`
**Update User Information**
----
  Modify user information, including first name, last name, email, mobile number, password, and activation status..
* **URL Params**
  None
* **Data Params**
  ```json
{
  "content": {
    "application/json": {
      "schema": {
        "type": "object",
        "properties": {
          "first_name": {
            "type": "string"
          },
          "last_name": {
            "type": "string"
          },
          "email": {
            "type": "string",
            "description": "Providing a new email temporarily sets the email verification status to false.",
            "format": "email"
          },
          "mobile": {
            "type": "string",
            "description": "Providing a new email temporarily sets the email verification status to false."
          },
          "password": {
            "type": "string",
            "format": "password"
          },
          "is_active": {
            "type": "boolean",
            "default": true
          }
        }
      },
      "examples": {
        "Update First Name": {
          "value": {
            "first_name": "Rebecca"
          }
        },
        "Update Email": {
          "value": {
            "email": "rebecca@gmail.com"
          }
        },
        "Update Last Name & Date of Birth": {
          "value": {
            "last_name": "Baker",
            "mobile": "347-122-1209"
          }
        },
        "Update Password": {
          "value": {
            "password": "s3cr3tpaswword"
          }
        }
      }
    }
  },
  "description": "Customize user information according to your requirements."
}
  ```
* **Headers**
  Content-Type: application/json
  Authorization: Bearer `<OAuth Token>`
* **Success Response:**
* **Code:** 200
  **Content:**  `{ <user_object> }`
* **Error Response:**
  * **Code:** 404
  **Content:** `{ error : "User doesn't exist" }`
  OR
  * **Code:** 401
  **Content:** `{ error : error : "You are unauthorized to make this request." }`
**Create New User**
----
  Add a new user to your system effortlessly..
* **URL Params**
  None
* **Data Params**
  ```json
{
  "content": {
    "application/json": {
      "schema": {
        "type": "object",
        "x-examples": {
          "Example 1": {
            "first_name": "David",
            "last_name": "Gavin",
            "email": "davidg@gmail.com",
            "mobile": "347-123-4567",
            "username": "davidg",
            "password": "s3cr3tp@assw0rd"
          }
        },
        "properties": {
          "first_name": {
            "type": "string"
          },
          "last_name": {
            "type": "string"
          },
          "email": {
            "type": "string"
          },
          "mobile": {
            "type": "string"
          },
          "username": {
            "type": "string"
          },
          "password": {
            "type": "string",
            "format": "password"
          }
        }
      },
      "examples": {
        "Create User David Gavin": {
          "value": {
            "first_name": "David",
            "last_name": "Gavin",
            "email": "davidg@gmail.com",
            "mobile": "347-123-4567",
            "username": "davidg",
            "password": "s3cr3tp@assw0rd"
          }
        }
      }
    }
  },
  "description": "Create a new user with the specified details."
}
  ```
* **Headers**
  Content-Type: application/json
  Authorization: Bearer `<OAuth Token>`
* **Success Response:**
* **Code:** 200
  **Content:**  `{ <user_object> }`
* **Error Response:**
  * **Code:** 404
  **Content:** `{ error : "User doesn't exist" }`
  OR
  * **Code:** 401
  **Content:** `{ error : error : "You are unauthorized to make this request." }`
