* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AmbisonicAudio.html

  * [Audio](https://docs.unity3d.com/6000.0/Documentation/Manual/Audio.html)
  * Ambisonic Audio


[](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerAudio.html)
Audio Profiler module
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioDevelopAmbisonicDecoder.html)
Develop an ambisonic audio decoder
# Ambisonic Audio
Ambisonics are a type of audio that provide a representation of sound that can completely surround a listener. They can provide an audio **skybox** A special type of Material used to represent skies. Usually six-sided. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sky-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Skybox) for distant ambient sounds, and are particularly useful for 360-degree videos and applications. 
Ambisonics are stored in a multi-channel format. Instead of mapping each channel to a specific speaker, ambisonics represent the soundfield in a more general way. You can rotate the soundfield based on the listener’s orientation (such as the user’s head rotation in VR). You can also decode the soundfield into a format that matches the speaker setup. 
## Selecting an ambisonic audio decoder
To select an ambisonic audio decoder in your project, open your project’s [Audio](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioManager.html) settings (menu: **Edit** > **Project Settings** > **Audio**). Select an **Ambisonic Decoder Plugin** from the list of available decoders in the project. 
![Ambisonic options in the Audio settings](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AmbisonicAudioSettings.png) Ambisonic options in the Audio settings
There are no built-in decoders included with Unity, but you can do one of the following options:
  * You can create your own ambisonic audio decoder **plug-in** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in). For more information, refer to [Ambisonic Audio Decoder](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioDevelopAmbisonicDecoder.html). 
  * Use external decoders. For instance, some **VR** Virtual Reality [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/VROverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#VR) hardware manufacturers provide them in their audio SDKs for Unity. Check your target platform manufacturer’s documentation to learn if this is available for your project.


## Importing an ambisonic audio clip
To import an ambisonic **audio clip** A container for audio data in Unity. Unity supports mono, stereo and multichannel audio assets (up to eight channels). Unity can import .aif, .wav, .mp3, and .ogg audio file format, and .xm, .mod, .it, and .s3m tracker module formats. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioClip), import a multi-channel B-format WAV file with ACN component ordering, and SN3D normalization. In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window for the audio clip, enable **Ambisonic**. 
![The Ambisonic option in the audio clip inspector](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AmbisonicAudioClipInspector.png) The Ambisonic option in the audio clip inspector
## Playing the ambisonic audio clip through an Audio Source
To play an ambisonic audio clip through an **Audio Source** A component which plays back an Audio Clip in the scene to an audio listener or through an audio mixer. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSource.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioSource): 
  * Assign the WAV file as an **Audio Clip** on an Audio Source.
  * Disable the **Spatialize** option. When you play an ambisonic audio clip, it is automatically decoded through the project’s selected ambisonic audio decoder. The decoder converts the clip from ambisonic format to the project’s selected speaker format. It also already handles spatialization as a part of this decoding operation, based on the orientation of the audio source and **audio listener** A component that acts like a microphone, receiving sound from Audio Sources in the scene and outputting to the computer speakers. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioListener.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioListener).


When Unity plays an ambisonic audio clip, it decompresses the file, if necessary, then decodes it to convert it to the project’s selected speaker mode. It then applies the Audio Source’s effects.
**Note:** Reverb zones are disabled for ambisonic audio clips.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerAudio.html)
Audio Profiler module
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioDevelopAmbisonicDecoder.html)
Develop an ambisonic audio decoder
