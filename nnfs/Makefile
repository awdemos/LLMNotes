# Binary name
BINARY_NAME=genesis

# Go related variables
GOBASE=$(shell pwd)
GOBIN=$(GOBASE)/bin

# Main package path
MAIN_PACKAGE=cmd/main.go

# Build the binary
build:
	@echo "Building $(BINARY_NAME)..."
	@go build -o $(GOBIN)/$(BINARY_NAME) $(MAIN_PACKAGE)

# Run the binary
run: build
	@echo "Running $(BINARY_NAME)..."
	@$(GOBIN)/$(BINARY_NAME)

# Clean build artifacts
clean:
	@echo "Cleaning..."
	@go clean
	@rm -rf $(GOBIN)

# Run tests
test:
	@echo "Running tests..."
	@go test ./...

# Build for multiple platforms
build-all:
	@echo "Building for multiple platforms..."
	@GOOS=linux GOARCH=amd64 go build -o $(GOBIN)/$(BINARY_NAME)-linux-amd64 $(MAIN_PACKAGE)
	@GOOS=darwin GOARCH=amd64 go build -o $(GOBIN)/$(BINARY_NAME)-darwin-amd64 $(MAIN_PACKAGE)
	@GOOS=windows GOARCH=amd64 go build -o $(GOBIN)/$(BINARY_NAME)-windows-amd64.exe $(MAIN_PACKAGE)

# Show help
help:
	@echo "Available targets:"
	@echo "  build       - Build the binary"
	@echo "  run         - Build and run the binary"
	@echo "  clean       - Remove build artifacts"
	@echo "  test        - Run tests"
	@echo "  build-all   - Build for multiple platforms"
	@echo "  help        - Show this help message"

.PHONY: build run clean test build-all help

