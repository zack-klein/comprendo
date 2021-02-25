set -e

cd frontend

echo "Building frontend..."
yarn build

echo "Syncing with S3..."
aws s3 sync build/ s3://comprendo.zacharyjklein.com/ --delete
