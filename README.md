I/flutter (17369): [VOICE] Status: notListening
D/SpeechToTextPlugin(17369): Notify status:done
I/flutter (17369): [VOICE] Status: done
D/SpeechToTextPlugin(17369): Stop listening done
W/AidlConversionCppNdk(17369): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(17369): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): Results null or empty
I/flutter (17369): [VOICE] Ergebnis: "gebe mir doch Informationen zum Licht" | final=true
I/flutter (17369): [JARVIS] Final STT: gebe mir doch Informationen zum Licht
I/flutter (17369): [VOICE] Listening gestoppt
I/flutter (17369): [VOICE] Status: done
I/flutter (17369): [JARVIS] Speech Mode: nodeRedAudio
I/flutter (17369): [JARVIS] Response Text: light.living_room wurde über den Jarvis Router verarbeitet (turn_on).
I/flutter (17369): [JARVIS] Audio URL: http://192.168.178.47:8123/local/jarvis/d542b8a69180b2d70b1f7148ddedf072bd33300c_de-de_db0e2e9c25_tts.piper_2.mp3
D/JARVIS_WAKEWORD(17369): Wakeword STOP
I/flutter (17369): [SPEECH OUTPUT] Ausgabe über Node-RED-Audio
I/flutter (17369): [AUDIO] Node-RED-Audio startet: http://192.168.178.47:8123/local/jarvis/d542b8a69180b2d70b1f7148ddedf072bd33300c_de-de_db0e2e9c25_tts.piper_2.mp3
I/ExoPlayerImpl(17369): Init cd231b7 [AndroidXMedia3/1.4.1] [serenity, 25028RN03Y, Xiaomi, 35]
I/mple.jarvis_app(17369): hiddenapi: Accessing hidden method Landroid/media/AudioTrack;->getLatency()I (runtime_flags=0, domain=platform, api=unsupported) from Landroidx/media3/exoplayer/audio/AudioTrackPositionTracker; (domain=app) using reflection: allowed
W/AudioCapabilities(17369): Unsupported mime audio/ima-adpcm
W/AudioCapabilities(17369): Unsupported mime audio/mpeg-L1
W/AudioCapabilities(17369): Unsupported mime audio/mpeg-L2
W/VideoCapabilities(17369): Unsupported mime video/jpeg
W/VideoCapabilities(17369): Unsupported mime video/jpeg
I/DMCodecAdapterFactory(17369): Creating an asynchronous MediaCodec adapter for track type audio
W/libc    (17369): Access denied finding property "persist.unipnp.video_mediacodec_fps_upload.enabled"
W/ExoPlayer:Playb(17369): type=1400 audit(0.0:18215): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c247,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/CCodec  (17369): allocate(c2.unisoc.mp3.decoder)
I/Codec2-HalSelection(17369): selection: hidl
I/Codec2Client(17369): Available Codec2 services: "default" "software"
I/Codec2-HalSelection(17369): selection: hidl
I/CCodec  (17369): setting up 'default' as default (vendor) store
I/Codec2-HalSelection(17369): selection: hidl
I/CCodec  (17369): Created component [c2.unisoc.mp3.decoder]
D/CCodecConfig(17369): read media type: audio/mpeg
D/ReflectedParamUpdater(17369): extent() != 1 for single value type: algo.buffers.max-count.values
D/ReflectedParamUpdater(17369): extent() != 1 for single value type: output.subscribed-indices.values
D/ReflectedParamUpdater(17369): extent() != 1 for single value type: input.buffers.allocator-ids.values
D/ReflectedParamUpdater(17369): extent() != 1 for single value type: output.buffers.allocator-ids.values
D/ReflectedParamUpdater(17369): extent() != 1 for single value type: algo.buffers.allocator-ids.values
D/ReflectedParamUpdater(17369): extent() != 1 for single value type: output.buffers.pool-ids.values
D/ReflectedParamUpdater(17369): extent() != 1 for single value type: algo.buffers.pool-ids.values
I/CCodecConfig(17369): query failed after returning 9 values (BAD_INDEX)
D/CCodecConfig(17369): c2 config diff is Dict {
D/CCodecConfig(17369):   c2::i32 algo.priority.value = -1
D/CCodecConfig(17369):   c2::float algo.rate.value = -1
D/CCodecConfig(17369):   c2::u32 coded.bitrate.value = 64000
D/CCodecConfig(17369):   c2::u32 input.buffers.max-size.value = 8192
D/CCodecConfig(17369):   c2::u32 input.delay.value = 0
D/CCodecConfig(17369):   string input.media-type.value = "audio/mpeg"
D/CCodecConfig(17369):   string output.media-type.value = "audio/raw"
D/CCodecConfig(17369):   c2::u32 raw.channel-count.value = 2
D/CCodecConfig(17369):   c2::u32 raw.sample-rate.value = 44100
D/CCodecConfig(17369): }
I/MediaCodec(17369): MediaCodec will operate in async mode
D/CCodec  (17369): [c2.unisoc.mp3.decoder] buffers are bound to CCodec for this session
D/CCodecConfig(17369): no c2 equivalents for log-session-id
D/CCodecConfig(17369): no c2 equivalents for importance
D/CCodecConfig(17369): no c2 equivalents for flags
D/CCodecConfig(17369): config failed => CORRUPTED
D/CCodecConfig(17369): c2 config diff is   c2::i32 algo.priority.value = 0
D/CCodecConfig(17369):   c2::u32 raw.channel-count.value = 1
D/CCodecConfig(17369):   c2::u32 raw.sample-rate.value = 22050
W/Codec2Client(17369): query -- param skipped: index = 1107298332.
D/CCodec  (17369): client requested max input size 4096, which is smaller than what component recommended (8192); overriding with component recommendation.
W/CCodec  (17369): This behavior is subject to change. It is recommended that app developers double check whether the requested max input size is in reasonable range.
D/CCodec  (17369): encoding statistics level = 0
D/CCodec  (17369): setup formats input: AMessage(what = 0x00000000) = {
D/CCodec  (17369):   int32_t bitrate = 64000
D/CCodec  (17369):   int32_t channel-count = 1
D/CCodec  (17369):   int32_t max-input-size = 8192
D/CCodec  (17369):   string mime = "audio/mpeg"
D/CCodec  (17369):   int32_t priority = 0
D/CCodec  (17369):   int32_t sample-rate = 22050
D/CCodec  (17369): }
D/CCodec  (17369): setup formats output: AMessage(what = 0x00000000) = {
D/CCodec  (17369):   int32_t channel-count = 1
D/CCodec  (17369):   string mime = "audio/raw"
D/CCodec  (17369):   int32_t priority = 0
D/CCodec  (17369):   int32_t sample-rate = 22050
D/CCodec  (17369):   int32_t android._config-pcm-encoding = 2
D/CCodec  (17369): }
I/CCodecConfig(17369): query failed after returning 9 values (BAD_INDEX)
D/MediaCodec(17369): keep callback message for reclaim
W/AString (17369): ctor got NULL, using empty string instead
W/Codec2Client(17369): query -- param skipped: index = 1342179345.
W/Codec2Client(17369): query -- param skipped: index = 2415921170.
W/Codec2Client(17369): query -- param skipped: index = 2684356609.
D/C2Store (17369): Using DMABUF Heaps
I/Codec2-HalSelection(17369): selection: hidl
D/CCodecBufferChannel(17369): [c2.unisoc.mp3.decoder#334] Created input block pool with allocatorID 16 => poolID 17 - OK (0)
I/CCodecBufferChannel(17369): [c2.unisoc.mp3.decoder#334] Created output block pool with allocatorID 16 => poolID 19 - OK
D/CCodecBufferChannel(17369): [c2.unisoc.mp3.decoder#334] Configured output block pool ids 19 => OK
I/DMABUFHEAPS(17369): Using DMA-BUF heap named: system
I/AudioTrack(17369): set(): streamType -1, sampleRate 22050, format 0x1, channelMask 0x1, frameCount 7120, flags 0, notificationFrames 0, sessionId 6097, transferType 3, uid 10247, pid 17369, packageName com.example.jarvis_app
D/AudioTrack(17369): set() fadeEnabled:1, isWhiteApp: 0
D/AudioTrack(17369): set(): Building AudioTrack with attributes: usage=1 content=0 flags=0xa00 tags=[]
D/AudioTrack(17369): set(), create sync notify, streamType 3
D/AudioNotifyPnp(17369): createAudioNotify()
D/mple.jarvis_app(17369): createAudioNotifyPnpFactory(), create unisoc AudioNotifyPnpInterface 0xb4000070731a72c0
D/AudioNotifyPnp(17369): checkWriterThreadName(), notify start to pnp, mWriterTid 26905, name ExoPlayer:Playb
I/AudioTrack(17369): stop(1226): prior state:STATE_FLUSHED
D/AudioTrack(17369): destructor portId(1226)
I/AudioTrack(17369): stop(1226): prior state:STATE_FLUSHED
I/AudioTrack(17369): set(): streamType -1, sampleRate 22050, format 0x1, channelMask 0x1, frameCount 7120, flags 0, notificationFrames 0, sessionId 6097, transferType 3, uid 10247, pid 17369, packageName com.example.jarvis_app
D/AudioTrack(17369): set() fadeEnabled:1, isWhiteApp: 0
D/AudioTrack(17369): set(): Building AudioTrack with attributes: usage=1 content=2 flags=0xa00 tags=[]
D/AudioTrack(17369): set(), create sync notify, streamType 3
D/AudioNotifyPnp(17369): createAudioNotify()
D/mple.jarvis_app(17369): createAudioNotifyPnpFactory(), create unisoc AudioNotifyPnpInterface 0xb400007075316a80
I/AudioTrack(17369): start(1227): prior state:STATE_STOPPED
D/AudioNotifyPnp(17369): checkWriterThreadName(), notify start to pnp, mWriterTid 26905, name ExoPlayer:Playb
W/AidlConversionCppNdk(17369): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/AudioTrack(17369): getTimestamp_l(1227): device stall time corrected using current time 38518775872986
D/AudioTrack(17369): getTimestamp_l(1227): stale timestamp time corrected, currentTimeNanos: 389391147528 < limitNs: 38518566682102 < mStartNs: 38518726682102
W/AudioTrack(17369): getTimestamp_l(1227): retrograde timestamp time corrected, 38518566682102 < 38518785993602
I/AudioTrack(17369): stop(1227): prior state:STATE_ACTIVE
D/AudioTrack(17369): stop(1227): called with 44305 frames delivered
D/AudioNotifyPnp(17369): setStateAndNotify(), state STATE_STOPPED, pid 17369, tid 26905
D/AudioNotifyPnp(17369): setStateAndNotify(), notify stop to pnp
I/flutter (17369): [AUDIO] Node-RED-Audio beendet
W/AidlConversionCppNdk(17369): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/BufferPoolAccessor2.0(17369): bufferpool2 0xb400007135ae9028 : 5(40960 size) total buffers - 0(0 size) used buffers - 84/89 (recycle/alloc) - 5/174 (fetch/transfer)
D/BufferPoolAccessor2.0(17369): evictor expired: 1, evicted: 1
D/JARVIS_WAKEWORD(17369): Listening gestartet
I/flutter (17369): [JARVIS] Wakeword aktiviert
D/AudioManager(17369): dispatching onAudioFocusChange(-2) to android.media.AudioManager@da7fd84com.ryanheise.audio_session.AudioManagerSingleton$$ExternalSyntheticLambda0@7dd596d
W/AidlConversionCppNdk(17369): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(17369): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(17369): Bereit für Wakeword
W/AidlConversionCppNdk(17369): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(17369): Wakeword STOP
I/flutter (17369): [JARVIS] Wakeword deaktiviert
D/AudioManager(17369): dispatching onAudioFocusChange(1) to android.media.AudioManager@da7fd84com.ryanheise.audio_session.AudioManagerSingleton$$ExternalSyntheticLambda0@7dd596d
W/AidlConversionCppNdk(17369): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(17369): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(17369): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/JARVIS_WAKEWORD(17369): Wakeword STOP
I/flutter (17369): [JARVIS] Wakeword-Stop angefordert
I/flutter (17369): [JARVIS] Mikrofon wird an Flutter übergeben
I/flutter (17369): [VOICE] startListening angefordert
D/SpeechToTextPlugin(17369): Start listening
D/SpeechToTextPlugin(17369): setupRecognizerIntent
D/SpeechToTextPlugin(17369): Notify status:listening
D/SpeechToTextPlugin(17369): Start listening done
I/flutter (17369): [VOICE] listen() abgeschlossen, isListening=true
I/flutter (17369): [JARVIS] VoiceService gestartet: true
D/AudioManager(17369): dispatching onAudioFocusChange(-2) to android.media.AudioManager@da7fd84com.ryanheise.audio_session.AudioManagerSingleton$$ExternalSyntheticLambda0@7dd596d
W/AidlConversionCppNdk(17369): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(17369): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/SpeechToTextPlugin(17369): rmsDB -2.0 / -2.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / -1.16
D/SpeechToTextPlugin(17369): rmsDB -2.0 / -1.16
D/SpeechToTextPlugin(17369): rmsDB -2.0 / -1.16
D/SpeechToTextPlugin(17369): rmsDB -2.0 / -1.16
D/SpeechToTextPlugin(17369): rmsDB -2.0 / -1.16
D/SpeechToTextPlugin(17369): rmsDB -2.0 / -1.16
D/SpeechToTextPlugin(17369): rmsDB -2.0 / -1.16
D/SpeechToTextPlugin(17369): rmsDB -2.0 / -1.16
D/SpeechToTextPlugin(17369): rmsDB -2.0 / -1.16
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 3.88
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 4.84
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 6.88
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 8.92
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 8.92
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 8.92
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 8.92
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 9.04
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 9.04
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 9.04
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 9.04
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 9.5199995
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 9.5199995
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 9.5199995
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 9.5199995
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 9.5199995
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 9.5199995
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 9.64
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): Calling results callback
I/flutter (17369): [VOICE] Ergebnis: "" | final=false
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): Calling results callback
I/flutter (17369): [VOICE] Ergebnis: "" | final=false
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): Calling results callback
I/flutter (17369): [VOICE] Ergebnis: "" | final=false
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): Calling results callback
I/flutter (17369): [VOICE] Ergebnis: "gebe" | final=false
I/flutter (17369): [JARVIS] Partial STT: gebe
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): Calling results callback
I/flutter (17369): [VOICE] Ergebnis: "gebe mir" | final=false
I/flutter (17369): [JARVIS] Partial STT: gebe mir
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): Calling results callback
I/flutter (17369): [VOICE] Ergebnis: "gebe mir" | final=false
I/flutter (17369): [JARVIS] Partial STT: gebe mir
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): Calling results callback
I/flutter (17369): [VOICE] Ergebnis: "gebe mir" | final=false
I/flutter (17369): [JARVIS] Partial STT: gebe mir
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): Calling results callback
I/flutter (17369): [VOICE] Ergebnis: "gebe mir" | final=false
I/flutter (17369): [JARVIS] Partial STT: gebe mir
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): Calling results callback
I/flutter (17369): [VOICE] Ergebnis: "gebe mir Informationen" | final=false
I/flutter (17369): [JARVIS] Partial STT: gebe mir Informationen
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): Calling results callback
I/flutter (17369): [VOICE] Ergebnis: "gebe mir Informationen zum" | final=false
I/flutter (17369): [JARVIS] Partial STT: gebe mir Informationen zum
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): Calling results callback
I/flutter (17369): [VOICE] Ergebnis: "gebe mir Informationen zum Licht" | final=false
I/flutter (17369): [JARVIS] Partial STT: gebe mir Informationen zum Licht
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
D/SpeechToTextPlugin(17369): Stop listening
D/SpeechToTextPlugin(17369): Notify status:notListening
I/flutter (17369): [VOICE] Status: notListening
D/SpeechToTextPlugin(17369): Notify status:done
I/flutter (17369): [VOICE] Status: done
D/SpeechToTextPlugin(17369): Stop listening done
D/AudioManager(17369): dispatching onAudioFocusChange(1) to android.media.AudioManager@da7fd84com.ryanheise.audio_session.AudioManagerSingleton$$ExternalSyntheticLambda0@7dd596d
D/SpeechToTextPlugin(17369): rmsDB -2.0 / 10.0
W/AidlConversionCppNdk(17369): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
W/AidlConversionCppNdk(17369): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/SpeechToTextPlugin(17369): Results null or empty
W/AidlConversionCppNdk(17369): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
I/flutter (17369): [VOICE] Ergebnis: "gebe mir Informationen zum Licht" | final=true
I/flutter (17369): [JARVIS] Final STT: gebe mir Informationen zum Licht
I/flutter (17369): [VOICE] Listening gestoppt
I/flutter (17369): [VOICE] Status: done
I/flutter (17369): [JARVIS] Speech Mode: nodeRedAudio
I/flutter (17369): [JARVIS] Response Text: light.living_room wurde über den Jarvis Router verarbeitet (turn_on).
I/flutter (17369): [JARVIS] Audio URL: http://192.168.178.47:8123/local/jarvis/d542b8a69180b2d70b1f7148ddedf072bd33300c_de-de_db0e2e9c25_tts.piper_2.mp3
D/JARVIS_WAKEWORD(17369): Wakeword STOP
I/ExoPlayerImpl(17369): Release cd231b7 [AndroidXMedia3/1.4.1] [serenity, 25028RN03Y, Xiaomi, 35] [media3.common, media3.exoplayer, media3.decoder, media3.datasource, media3.extractor]
D/MediaCodec(17369): keep callback message for reclaim
I/AudioTrack(17369): stop(1227): prior state:STATE_FLUSHED
I/CCodecConfig(17369): query failed after returning 9 values (BAD_INDEX)
D/BufferPoolAccessor2.0(17369): bufferpool2 0xb400007135ae9028 : 1(8192 size) total buffers - 1(8192 size) used buffers - 84/90 (recycle/alloc) - 5/174 (fetch/transfer)
D/AudioTrack(17369): destructor portId(1227)
I/AudioTrack(17369): stop(1227): prior state:STATE_FLUSHED
W/Codec2Client(17369): query -- param skipped: index = 1342179345.
W/Codec2Client(17369): query -- param skipped: index = 2415921170.
D/CCodecBufferChannel(17369): [c2.unisoc.mp3.decoder#334] MediaCodec discarded an unknown buffer
D/CCodecBufferChannel(17369): [c2.unisoc.mp3.decoder#334] MediaCodec discarded an unknown buffer
I/Codec2-HalSelection(17369): selection: hidl
D/CCodecBufferChannel(17369): [c2.unisoc.mp3.decoder#334] MediaCodec discarded an unknown buffer
D/CCodecBufferChannel(17369): [c2.unisoc.mp3.decoder#334] MediaCodec discarded an unknown buffer
I/hw-BpHwBinder(17369): onLastStrongRef automatically unlinking death recipients
I/flutter (17369): [SPEECH OUTPUT] Ausgabe über Node-RED-Audio
I/flutter (17369): [AUDIO] Node-RED-Audio startet: http://192.168.178.47:8123/local/jarvis/d542b8a69180b2d70b1f7148ddedf072bd33300c_de-de_db0e2e9c25_tts.piper_2.mp3
I/ExoPlayerImpl(17369): Init 7a54925 [AndroidXMedia3/1.4.1] [serenity, 25028RN03Y, Xiaomi, 35]
I/DMCodecAdapterFactory(17369): Creating an asynchronous MediaCodec adapter for track type audio
W/libc    (17369): Access denied finding property "persist.unipnp.video_mediacodec_fps_upload.enabled"
W/ExoPlayer:Playb(17369): type=1400 audit(0.0:18218): avc:  denied  { read } for  name="u:object_r:unipnp_prop:s0" dev="tmpfs" ino=427 scontext=u:r:untrusted_app:s0:c247,c256,c512,c768 tcontext=u:object_r:unipnp_prop:s0 tclass=file permissive=0 app=com.example.jarvis_app
D/CCodec  (17369): allocate(c2.unisoc.mp3.decoder)
I/Codec2-HalSelection(17369): selection: hidl
I/CCodec  (17369): setting up 'default' as default (vendor) store
I/CCodec  (17369): Created component [c2.unisoc.mp3.decoder]
D/CCodecConfig(17369): read media type: audio/mpeg
D/ReflectedParamUpdater(17369): extent() != 1 for single value type: algo.buffers.max-count.values
D/ReflectedParamUpdater(17369): extent() != 1 for single value type: output.subscribed-indices.values
D/ReflectedParamUpdater(17369): extent() != 1 for single value type: input.buffers.allocator-ids.values
D/ReflectedParamUpdater(17369): extent() != 1 for single value type: output.buffers.allocator-ids.values
D/ReflectedParamUpdater(17369): extent() != 1 for single value type: algo.buffers.allocator-ids.values
D/ReflectedParamUpdater(17369): extent() != 1 for single value type: output.buffers.pool-ids.values
D/ReflectedParamUpdater(17369): extent() != 1 for single value type: algo.buffers.pool-ids.values
I/CCodecConfig(17369): query failed after returning 9 values (BAD_INDEX)
D/CCodecConfig(17369): c2 config diff is Dict {
D/CCodecConfig(17369):   c2::i32 algo.priority.value = -1
D/CCodecConfig(17369):   c2::float algo.rate.value = -1
D/CCodecConfig(17369):   c2::u32 coded.bitrate.value = 64000
D/CCodecConfig(17369):   c2::u32 input.buffers.max-size.value = 8192
D/CCodecConfig(17369):   c2::u32 input.delay.value = 0
D/CCodecConfig(17369):   string input.media-type.value = "audio/mpeg"
D/CCodecConfig(17369):   string output.media-type.value = "audio/raw"
D/CCodecConfig(17369):   c2::u32 raw.channel-count.value = 2
D/CCodecConfig(17369):   c2::u32 raw.sample-rate.value = 44100
D/CCodecConfig(17369): }
I/MediaCodec(17369): MediaCodec will operate in async mode
D/CCodec  (17369): [c2.unisoc.mp3.decoder] buffers are bound to CCodec for this session
D/CCodecConfig(17369): no c2 equivalents for log-session-id
D/CCodecConfig(17369): no c2 equivalents for importance
D/CCodecConfig(17369): no c2 equivalents for flags
D/CCodecConfig(17369): config failed => CORRUPTED
D/CCodecConfig(17369): c2 config diff is   c2::i32 algo.priority.value = 0
D/CCodecConfig(17369):   c2::u32 raw.channel-count.value = 1
D/CCodecConfig(17369):   c2::u32 raw.sample-rate.value = 22050
W/Codec2Client(17369): query -- param skipped: index = 1107298332.
D/CCodec  (17369): client requested max input size 4096, which is smaller than what component recommended (8192); overriding with component recommendation.
W/CCodec  (17369): This behavior is subject to change. It is recommended that app developers double check whether the requested max input size is in reasonable range.
D/CCodec  (17369): encoding statistics level = 0
D/CCodec  (17369): setup formats input: AMessage(what = 0x00000000) = {
D/CCodec  (17369):   int32_t bitrate = 64000
D/CCodec  (17369):   int32_t channel-count = 1
D/CCodec  (17369):   int32_t max-input-size = 8192
D/CCodec  (17369):   string mime = "audio/mpeg"
D/CCodec  (17369):   int32_t priority = 0
D/CCodec  (17369):   int32_t sample-rate = 22050
D/CCodec  (17369): }
D/CCodec  (17369): setup formats output: AMessage(what = 0x00000000) = {
D/CCodec  (17369):   int32_t channel-count = 1
D/CCodec  (17369):   string mime = "audio/raw"
D/CCodec  (17369):   int32_t priority = 0
D/CCodec  (17369):   int32_t sample-rate = 22050
D/CCodec  (17369):   int32_t android._config-pcm-encoding = 2
D/CCodec  (17369): }
I/CCodecConfig(17369): query failed after returning 9 values (BAD_INDEX)
D/MediaCodec(17369): keep callback message for reclaim
W/AString (17369): ctor got NULL, using empty string instead
W/Codec2Client(17369): query -- param skipped: index = 1342179345.
W/Codec2Client(17369): query -- param skipped: index = 2415921170.
W/Codec2Client(17369): query -- param skipped: index = 2684356609.
D/CCodecBufferChannel(17369): [c2.unisoc.mp3.decoder#578] Created input block pool with allocatorID 16 => poolID 18 - OK (0)
I/CCodecBufferChannel(17369): [c2.unisoc.mp3.decoder#578] Created output block pool with allocatorID 16 => poolID 20 - OK
D/CCodecBufferChannel(17369): [c2.unisoc.mp3.decoder#578] Configured output block pool ids 20 => OK
I/AudioTrack(17369): set(): streamType -1, sampleRate 22050, format 0x1, channelMask 0x1, frameCount 7120, flags 0, notificationFrames 0, sessionId 6153, transferType 3, uid 10247, pid 17369, packageName com.example.jarvis_app
D/AudioTrack(17369): set() fadeEnabled:1, isWhiteApp: 0
D/AudioTrack(17369): set(): Building AudioTrack with attributes: usage=1 content=2 flags=0xa00 tags=[]
D/AudioTrack(17369): set(), create sync notify, streamType 3
D/AudioNotifyPnp(17369): createAudioNotify()
D/mple.jarvis_app(17369): createAudioNotifyPnpFactory(), create unisoc AudioNotifyPnpInterface 0xb4000070702b1dc0
D/AudioNotifyPnp(17369): checkWriterThreadName(), notify start to pnp, mWriterTid 27078, name ExoPlayer:Playb
I/AudioTrack(17369): start(1239): prior state:STATE_STOPPED
D/AudioNotifyPnp(17369): setStateAndNotify(), state STATE_ACTIVE, pid 17369, tid 27078
D/AudioNotifyPnp(17369): checkWriterThreadName(), notify start to pnp, mWriterTid 27078, name ExoPlayer:Playb
W/AidlConversionCppNdk(17369): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/AudioTrack(17369): getTimestamp_l(1239): device stall time corrected using current time 38594007844740
D/AudioTrack(17369): getTimestamp_l(1239): stale timestamp time corrected, currentTimeNanos: 38523871877521 < limitNs: 38593811045625 < mStartNs: 38593971045625
W/AudioTrack(17369): getTimestamp_l(1239): retrograde timestamp time corrected, 38593811045625 < 38594018007509
I/AudioTrack(17369): stop(1239): prior state:STATE_ACTIVE
D/AudioTrack(17369): stop(1239): called with 50112 frames delivered
D/AudioNotifyPnp(17369): setStateAndNotify(), state STATE_STOPPED, pid 17369, tid 27078
D/AudioNotifyPnp(17369): setStateAndNotify(), notify stop to pnp
I/flutter (17369): [AUDIO] Node-RED-Audio beendet
W/AidlConversionCppNdk(17369): aidl2legacy_AudioChannelLayout_audio_channel_mask_t: no legacy output audio_channel_mask_t found for AudioChannelLayout{layoutMask: 16}
D/BufferPoolAccessor2.0(17369): bufferpool2 0xb400007135ae9028 : 0(0 size) total buffers - 0(0 size) used buffers - 84/94 (recycle/alloc) - 5/174 (fetch/transfer)
D/BufferPoolAccessor2.0(17369): evictor expired: 1, evicted: 1
D/BufferPoolAccessor2.0(17369): bufferpool2 0xb4000070726d6c28 : 5(40960 size) total buffers - 0(0 size) used buffers - 84/89 (recycle/alloc) - 5/174 (fetch/transfer)
D/BufferPoolAccessor2.0(17369): evictor expired: 1, evicted: 1
