const path =
    (msg.payload || '').trim();

if (!path) {
    msg.payload =
        msg.originalPayload;

    msg.payload.audioUrl =
        null;

    return msg;
}

const filename =
    path.split('/').pop();

msg.payload =
    msg.originalPayload;

msg.payload.audioUrl =
    "http://192.168.178.47:8123/local/tts/" +
    filename;

return msg;
