* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AudioFiles.html

  * [Audio](https://docs.unity3d.com/6000.0/Documentation/Manual/Audio.html)
  * Audio files


[](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioOverview.html)
Audio overview
[](https://docs.unity3d.com/6000.0/Documentation/Manual/TrackerModules.html)
Tracker Modules
# Audio files
As with Meshes or Textures, the workflow for **Audio File** assets is designed to be smooth and simple. Unity can import almost every common file format, but there are a few details that are useful to be aware of when you work with audio files.
For a list of the audio formats Unity supports, refer to [Supported audio file formats](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioFiles.html#supported-audio-file-formats). 
For an extensive description of the **compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride), [Animation Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html#AssetProperties), [Audio Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html), [Build Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#compression) formats and other options available for encoding audio data, refer to [AudioClip](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html). 
## Audio data and AudioClips
Unity audio data is separate from the actual AudioClips. Audio data is the raw information about an audio file. It contains information such as length, channel count, sample rate, and compression format. 
AudioClips are assets that contain the audio data and processes the audio data for use with Unity Engine.
## Import your audio files
To import an audio file to Unity, click and drag your file into your project. Unity imports the audio file as an AudioClip. 
## Alter the settings of your audio file
Use the settings in the AudioClip importer to determine how the clips will load at runtime. These settings let you decide which audio assets will stay in memory. This is ideal for frequent or unpredictable sounds like footsteps, weapons, or impacts.
For other assets, such as speech, background music, or ambient loops, you can set them to load on-demand or as the player progresses. This approach optimizes memory usage and improves performance.
## How Unity compresses audio
When Unity encodes audio, the main compression formats for how Unity stores the audio on disk are the following: * _PCM_ * _ADPCM_ * _Compressed_. 
Additionally there are a few platform-specific formats but they work in similar ways. The default mode is _Compressed_ , where Unity compresses the audio data with either the Vorbis or MP3 format for standalone and mobile platforms.
## Use audio files in your scripts
Any audio file imported into Unity is available from **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) as an AudioClip instance. This provides a way for the game runtime of the audio system to access the encoded audio data. The game might access meta-information about the audio data via the AudioClip even before the actual audio data loads. 
The import process extracts information such as length, channel count and sample rate from the encoded audio data and stores these details in the AudioClip. This information can be useful for automatic dialog or music sequencing systems, because the music engine can use the length to schedule music playback before the data loads. It also helps to reduce memory usage because it only keeps the **audio clips** A container for audio data in Unity. Unity supports mono, stereo and multichannel audio assets (up to eight channels). Unity can import .aif, .wav, .mp3, and .ogg audio file format, and .xm, .mod, .it, and .s3m tracker module formats. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioClip) in memory the application needs at a certain time.
## Supported audio file formats
Unity supports the following audio file formats. 
**_Format_** | **_Extensions_**  
---|---  
MPEG layer 3 | .mp3  
Ogg Vorbis | .ogg  
Microsoft Wave | .wav  
Free Lossless Audio Codec (FLAC) | .flac  
Audio Interchange File Format | .aiff / .aif  
Ultimate Soundtracker module | .mod  
Impulse Tracker module | .it  
Scream Tracker module | .s3m  
FastTracker 2 module | .xm  
For more information about how to use sound in Unity, refer to [Audio Overview](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioOverview.html).
## Additional references
  * [Audio Overview](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioOverview.html)
  * [AudioClip](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioOverview.html)
Audio overview
[](https://docs.unity3d.com/6000.0/Documentation/Manual/TrackerModules.html)
Tracker Modules
