# Stage 1
FROM nginx:1.17.1-alpine
COPY --from=build /app/dist/budget-app /usr/share/nginx/html
