#!/bin/bash

PROJECT_ID="ai-hangsik"
REGION="us-central1"
SERVICE_NAME="mcp-streamable-http"

gcloud run deploy $SERVICE_NAME \
    --platform managed \
    --project $PROJECT_ID \
    --region $REGION \
    --allow-unauthenticated \
    --source .