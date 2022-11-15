package main

import (
	"fmt"
	"net/http"
	"os"
)

func main() {
	_, err := http.Get(fmt.Sprintf("http://0.0.0.0:8999/healthcheck"))
	if err != nil {
		os.Exit(1)
	}
}
