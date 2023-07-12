# blog-web-app
A REST API that handles CRUD requests for articles and their comments.
Built using [Django REST Framework (DRF)](https://www.django-rest-framework.org/) using Postgres DB as the backend database.

## Running locally
Simply run `docker compose up` to spin up the database and API locally.
This will:
1. Build the DRF app image.
2. Instantiate a local Postgres database.
3. Run model migrations and create the app's first user (see [docker-compose.yml](./docker-compose.yml) for credentials).
4. Start the DRF app on port 8000.

## Endpoints
- `GET/POST /articles`: List existing articles / Create a new article.
- `GET/PUT/DELETE /articles/<article-id>`: Get/Update/Delete an existing article.
- `GET/POST /articles/<article-id>/comments`: List existing comments for an article / Create a new comment under an article.
- `GET/PUT/DELETE /articles/<article-id>/comments/<comment-id>`: Get/Update/Delete an existing comment under an article.
