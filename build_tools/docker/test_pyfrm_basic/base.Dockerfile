ARG BASE_IMAGE
FROM $BASE_IMAGE

ARG UPDATE_CMD
ARG INSTALL_CMD
RUN set -ex && $UPDATE_CMD && $INSTALL_CMD && python3 -V

CMD ["sh"]
