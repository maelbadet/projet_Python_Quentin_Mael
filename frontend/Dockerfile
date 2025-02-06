# Base image
FROM nginx:alpine

# Set the working directory
WORKDIR /usr/share/nginx/html

# Copy HTML files to the root of the Nginx HTML directory
COPY src/pages/ .

# Copy CSS files to a "styles" directory
COPY src/styles/ ./styles

# Copy custom Nginx configuration
COPY default.conf /etc/nginx/conf.d/default.conf

# Expose port for frontend
EXPOSE 80