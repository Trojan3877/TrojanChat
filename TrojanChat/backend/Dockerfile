# Dockerfile for TrojanChat Go Microservice
# Author: Corey Leath

FROM golang:1.20-alpine AS builder

# Install git for fetching modules
RUN apk add --no-cache git

WORKDIR /app

# Copy go.mod and go.sum, download dependencies
COPY backend/go.mod backend/go.sum ./
RUN go mod download

# Copy the source
COPY backend/*.go ./

# Build the binary
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o trojanchat_service

# --- Final image ---
FROM scratch

# Copy the binary
COPY --from=builder /app/trojanchat_service /usr/local/bin/trojanchat_service

# Copy Firebase credentials (mounted at runtime via Kubernetes secret or Docker volume)
# COPY credentials/serviceAccountKey.json /etc/secrets/serviceAccountKey.json

# Expose port
EXPOSE 8080

# Entry point
ENTRYPOINT ["/usr/local/bin/trojanchat_service"]


git add TrojanChat/backend/Dockerfile
git commit -m "Add Dockerfile for TrojanChat Go microservice"
git push
