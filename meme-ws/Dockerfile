# -------------------------------------------------------------------
# Stage 1: Golang Builder: Healthcheck Application
# -------------------------------------------------------------------
FROM golang:1.16.4 as golang-builder

WORKDIR /healthcheck
COPY healthcheck/healthcheck.go .
RUN go mod init healthcheck && \
	CGO_ENABLED=0 go build -a -installsuffix cgo -o healthcheck "/healthcheck"

# -------------------------------------------------------------------
# Stage 3: Release Image
# -------------------------------------------------------------------
FROM python:3.9

# Copy Application
ENV PORT=8999 

WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt

# Copy Healthcheck
COPY --from=golang-builder /healthcheck/healthcheck /app/healthcheck

# Healthchecks
HEALTHCHECK --interval=5s --timeout=1s --start-period=10s --retries=3 CMD [ "/app/healthcheck" ]

# Command
EXPOSE $PORT
CMD ["gunicorn" ,"--bind" ,"0.0.0.0:8999", "wsgi:app"]
