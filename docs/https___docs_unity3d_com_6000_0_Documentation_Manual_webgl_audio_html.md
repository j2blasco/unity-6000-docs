* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-audio.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Web](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl.html)
  * [Web development](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-develop.html)
  * Audio in Web


[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-graphics.html)
Web graphics
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-video.html)
Video playback in Web
# Audio in Web
This page only provides information about audio capabilities in the Web platform. To learn how to use audio in your Unity project, refer to [Audio Overview](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioOverview.html). 
Because Unity uses [FMOD](https://www.fmod.com)Audio in Unity is built on top of a middleware called FMOD. FMOD is integrated with the Unity engine for creating and playing back interactive audio.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#FMOD) to manage audio for platforms, the Web platform supports limited audio functionality, which only includes the basic features. FMOD relies on threads, which the **WebGL** A JavaScript API that renders 2D and 3D graphics in a web browser. The Unity Web build option allows Unity to publish content as JavaScript programs which use HTML5 technologies and the WebGL rendering API to run Unity content in a web browser. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#WebGL) API doesn’t support. For this reason, Unity uses an implementation based on the internal Web Audio API, which enables the browser to handle audio playback and mixing. 
**Note:** Google Chrome’s new Autoplay policy prevents autoplay of audio and video under certain conditions. For example, while your game might be set to autoplay some background music soon after the game loads, it won’t play automatically unless you click or tap on the website. For more information on how to enable or disable this policy, refer to Google Chrome’s documentation on [Autoplay policy in Chrome](https://developer.chrome.com/blog/autoplay/).
## Supported classes
Unity Web supports the following API classes: 
**Class** | **WebGL Support status**  
---|---  
**[AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)** | WebGL supports some APIs. Refer to [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) for specific support details.  
**[AudioListener](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioListener.html)** | All APIs supported.  
**[AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html)** | WebGL supports some APIs. Refer to [AudioClip](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-audio.html#audioclip) for specific support details.  
**[AudioMixer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Audio.AudioMixer.html)** | WebGL supports some APIs. Refer to [Audio Mixer](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-audio.html#audio-mixer) for specific support details.  
**[SystemInfo.supportsAudio](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsAudio.html)** | The browser provides audio support for WebGL. For this reason, `SystemInfo.supportsAudio` is always true.  
**[Microphone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Microphone.html)** | Not supported.  
## AudioSource
The [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) API supports basic positional audio playback, including: 
  * Pausing and resuming
  * Rolloff
  * Pitch setting
  * Doppler effect support


Unity WebGL supports the following AudioSource APIs: 
**Settings** | **Description**  
---|---  
**[Clip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-clip.html)** | Determines the **audio clip** A container for audio data in Unity. Unity supports mono, stereo and multichannel audio assets (up to eight channels). Unity can import .aif, .wav, .mp3, and .ogg audio file format, and .xm, .mod, .it, and .s3m tracker module formats. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioClip) that plays next.  
**[dopplerLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-dopplerLevel.html)** | Sets the Doppler scale for the AudioSource.  
**[ignoreListenerPause](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-ignoreListenerPause.html)** | Allows AudioSource to ignore `AudioListener.pause` and continue to play audio.  
**[ignoreListenerVolume](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-ignoreListenerVolume.html)** | Ignores the end-user’s AudioSource volume.  
**[isPlaying](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-isPlaying.html)** | Returns true if the `AudioSource.clip` is playing.  
**[loop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-loop.html)** | Allows the application to loop the `AudioSource.clip`.  
**[maxDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-maxDistance.html)** | Sets the maximum distance at which the `AudioSource.clip` stops attenuating or becomes inaudible.  
**[minDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-minDistance.html)** | Sets the minimum distance at which the AudioSource.clip no longer rises in volumes. The sound starts to attenuate beyond the minimum distance.  
**[mute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-mute.html)** | Mutes the AudioSource.  
**[pitch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-pitch.html)** | Sets the pitch of the `AudioSource.clip`. WebGL only supports positive pitch values.  
**[playOnAwake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-playOnAwake.html)** | Plays the AudioSource on Awake.  
**[rolloffMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-rolloffMode.html)** | Sets the AudioSource attenuation over distance.  
**[time](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-time.html)** | Sets the playback position in seconds.  
**[timeSamples](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-timeSamples.html)** | Sets the playback position in Pulse-code modulation (PCM) samples.  
**[velocityUpdateMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-velocityUpdateMode.html)** | Sets whether the AudioSource updates in the fixed or dynamic update loop.  
**[volume](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-volume.html)** | Sets the volume of the AudioSource (0.0 to 1.0).  
**[Pause](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.Pause.html)** | Pauses the `AudioSource.clip`.  
**[Play](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.Play.html)** | Plays the `AudioSource.clip`.  
**[PlayDelayed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.PlayDelayed.html)** | Plays the `AudioSource.clip` with a delay you specify in seconds.  
**[PlayOneShot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.PlayOneShot.html)** | Plays an [AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-clip.html) and scales the AudioSource volume by volumeScale.  
**[PlayScheduled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.PlayScheduled.html)** | Plays the AudioSource at a time you specify.  
**[SetScheduledEndTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.SetScheduledEndTime.html)** | Sets a time that a scheduled `AudioSource.clip` ends.  
**[SetScheduledStartTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.SetScheduledStartTime.html)** | Sets the time that a scheduled `AudioSource.clip` starts.  
**[Stop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.Stop.html)** | Stops playing the `AudioSource.clip`.  
**[UnPause](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.UnPause.html)** | Unpauses a paused `AudioSource.clip`.  
**[PlayClipAtPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.PlayClipAtPoint.html)** | Plays an `AudioSource.clip` at a given position in the worldspace.  
**Note:** Because audio data is decoded in the browser with [`decodeAudioData`](https://webaudio.github.io/web-audio-api/#dom-baseaudiocontext-decodeaudiodata), it is possible that the runtime sampling rate of the audio file is different from the serialized audio data (44100Hz) as the browser will match the `BaseAudioContext` sampling rate, generally aligned with the device audio driver setup. Considering this, we recommend validating the [`AudioClip.frequency`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip-frequency.html) value at runtime or using [`AudioSource.time`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-time.html) when performing seeking operations.
## AudioClip 
Unity WebGL imports [AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html) files in the AAC Format, which is supported by most browsers. Unity WebGL supports the following AudioClip APIs: 
**Properties** | **Description**  
---|---  
**[frequency](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip-frequency.html)** | The sample frequency of the clip in Hertz.  
**[length](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip-length.html)** | The length of the AudioClip in seconds.  
**[loadState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip-loadState.html)** | Returns the current load state of the audio data associated with an AudioClip.  
**[samples](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip-samples.html)** | The length of the AudioClip in samples.  
**[loadType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip-loadType.html)** | The load type of the clip. You can set the AudioClip load type in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector).  
**Method** | **Description** | **Additional information**  
---|---|---  
**[AudioClip.Create](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.Create.html)** | Creates an AudioClip with a name and length you specify. | Unity WebGL partially supports `AudioClip.Create`. Browsers don’t support dynamic streaming, so to use `AudioClip.Create`, set the Stream to false.  
**[AudioClip.SetData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.SetData.html)** | Sets sample data in an AudioSource.clip. | Unity WebGL partially supports `AudioClip.SetData`. You can use this method only on compressed audio files with **Load Type** set to **Decompress on Load**. Refer to [Compressed audio](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-audio.html#compressed-audio).  
**[AudioClip.GetData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.GetData.html)** | Retrieves an array with sample data from an AudioSource.clip. | Unity WebGL partially supports `AudioClip.GetData`. You can use this method only on compressed audio files with **Load Type** set to **Decompress on Load**. Refer to [Compressed audio](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-audio.html#compressed-audio).  
**Note:** For audio clip support on Linux, make sure you’ve installed the [ffmpeg](https://ffmpeg.org/) package.
## Audio Mixer 
Unity Web supports some functionality of [Audio Mixer](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioMixer.html) assets. 
You can do the following with Audio Mixers on Web:
  * Create an Audio Mixer asset.
  * Add AudioMixerGroups to the hierarchy.
  * Adjust the volume of each group. To expose or change the volume with scripting, use [AudioMixer.SetFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Audio.AudioMixer.SetFloat.html).


**Note** : Volume is the only property you can change on Web. Other properties and sound effects aren’t supported.
## Compressed audio 
To use compressed audio with WebGL in Unity, set the AudioClip [loadType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip-loadType.html) to one of the following options: 
  * [CompressedInMemory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClipLoadType.CompressedInMemory.html)
  * [DecompressOnLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClipLoadType.DecompressOnLoad.html)

****Compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride), [Animation Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html#AssetProperties), [Audio Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html), [Build Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#compression) method** | **Description** | **Considerations**  
---|---|---  
**CompressedInMemory** | Use this to compress the audio on disk and have it remain compressed after it loads into your application memory. | Compressed audio can cause latency and is less precise when it comes to audio playback. However, compressed audio uses less memory in your application than decompressed audio. It’s best practice to use `CompressedInMemory` for audio that’s unaffected by precision for example, background music.  
**DecompressOnLoad** | Use this to compress the audio on disk, similar to CompressedInMemory, and decompress when it loads into your application memory. | Decompressed audio uses a significant amount of memory compared to compressed audio but has lower latency and more audio flexibility. Use `DecompressedOnLoad` for audio that’s affected by precision (for example, character dialog or sound effects).  
## Audio playback and browser security
For security reasons, browsers don’t allow audio playback until an end user interacts with your application webpage via a mouse click, touch event, or key press. Use a loading screen to allow the end user to interact with your application and start audio playback before your main content begins. 
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-graphics.html)
Web graphics
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-video.html)
Video playback in Web
