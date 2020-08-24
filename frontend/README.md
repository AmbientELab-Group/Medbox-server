This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Docerized Scripts

### `docker-compose build`

Builds the image used in development.

### `docker-compose up`

Starts the development image. Dev version allows for hot-reloading so dockerization is transparent for the normal react app workflow.

### `docker-compose -f docker-compose.prod.yml up -d --build`

Builds and runs the production version of the app. For deployment only.
