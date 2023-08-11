Documentation for your Hacker News V2.0 API, including all available methods (GET, POST, PUT, PATCH, DELETE) for each endpoint:

## My Project API Documentation

Welcome to the API documentation for My Project. This API allows you to interact with items and perform various operations.

### Endpoints

#### List and Filter Items

Endpoint: `/api/items/`

- **GET**: List all items with optional filtering and searching.
  - **Parameters**:
    - `category`: Filter items by category (Choices: 'All', 'jobs', 'story', 'comment', 'poll').
    - `search_in_creator`: Search in item creator.
    - `search_in_score`: Search in item score.
    - `query`: Search query text (used with `search_in_creator` and `search_in_score`).

#### Retrieve, Update, and Delete Single Item

Endpoint: `/api/items/<uuid>/`

- **GET**: Retrieve details of a specific item.
- **PUT**: Update details of a specific item (all fields required).
- **PATCH**: Partially update details of a specific item (specific fields can be updated).
- **DELETE**: Delete a specific item.

### Item Fields

- `id`: Unique identifier of the item (UUID).
- `title`: Title of the item.
- `category`: Category of the item (Choices: 'jobs', 'story', 'comment', 'poll').
- `creator`: Creator of the item.
- `date`: Date of the item.
- `score`: Score of the item.
- `is_api_post`: Indicates if the item is from the API (Boolean).
- `is_editable`: Indicates if the item is editable (Boolean).

### List of Categories

- 'All': List items from all categories.
- 'jobs': List job-related items.
- 'story': List story-related items.
- 'comment': List comment items.
- 'poll': List poll items.

### How to Use

You can interact with this API using various HTTP methods:

- `GET`: Retrieve a list of items with optional filters and search queries.
- `POST`: Create a new item.
- `PUT`: Update all fields of a specific item.
- `PATCH`: Partially update specific fields of a specific item.
- `DELETE`: Delete a specific item.

### Authentication and Permissions

Authentication is not required for most API endpoints. However, some methods, such as creating, updating, or deleting items, may require appropriate permissions.

### API Response Format

Responses from the API are returned in JSON format and follow a structured pattern. Successful responses include a `data` field containing the requested information.

```json
{
    "data": {  }
}
```

Error responses include an `error` field containing details about the error.

```json
{
    "error": {
        "message": "Error message here"
    }
}
```

---

This documentation outlines the available endpoints, methods, and parameters for interacting with the My Project API. Feel free to reach out if you have any further questions or need assistance!