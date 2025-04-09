# Use the official Caddy image from Docker Hub
FROM caddy:2

# Copy your Caddyfile to the container
COPY Caddyfile /etc/caddy/Caddyfile

# Expose the port Caddy will listen on
EXPOSE 8080

# Run Caddy with the Caddyfile
CMD ["caddy", "run", "--config", "/etc/caddy/Caddyfile", "--adapter", "caddyfile"]
