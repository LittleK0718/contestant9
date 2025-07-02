FROM python:alpine AS build
WORKDIR /build
COPY app.py .
RUN pip install flask -t /build/libs


FROM python:alpine AS app
WORKDIR /app
COPY --from=build /build/libs /app/libs
COPY --from=build /build /app
ENV PYTHONPATH=/app/libs
EXPOSE 80
CMD [ "python", "app.py" ]