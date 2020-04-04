build-app:
	DOCKER_BUILDKIT=1 docker build \
	-t mysite_v2 \
	.