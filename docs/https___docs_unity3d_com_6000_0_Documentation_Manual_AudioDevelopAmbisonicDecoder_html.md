* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AudioDevelopAmbisonicDecoder.html

  * [Audio](https://docs.unity3d.com/6000.0/Documentation/Manual/Audio.html)
  * [Ambisonic Audio](https://docs.unity3d.com/6000.0/Documentation/Manual/AmbisonicAudio.html)
  * Develop an ambisonic audio decoder


[](https://docs.unity3d.com/6000.0/Documentation/Manual/AmbisonicAudio.html)
Ambisonic Audio
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioReference.html)
Audio Reference
# Develop an ambisonic audio decoder
An ambisonic decoder is an audio component that decodes the ambisonic audio format into a specific output format, such as stereo or surround sound. This format depends on your speaker configuration (menu: **Edit** > **Project Settings** > **Audio** > **Default Speaker Mode**), unless your platform overrides this. 
Although Unity supports ambisonic audio, it doesn’t provide built-in decoders by default. Instead, you must either select a third-party decoder, or use your own decoder **plug-in** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in). 
## Set up an ambisonic audio decoder plug-in
You can set up an ambisonic audio decoder in the same way as you’d set up an [Audio Spatializer](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSpatializerSDK.html)A plug-in that changes the way audio is transmitted from an audio source into the surrounding space. It takes the source and regulates the gains of the left and right ear contributions based on the distance and angle between the AudioListener and the AudioSource. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSpatializerSDK.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioSpatializer). However, the following parameters in the `AudioPluginInterface.h` file are specific to ambisonic audio decoder plug-ins:
  * The [`UnityAudioEffectDefinitionFlags_IsAmbisonicDecoder`](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioDevelopAmbisonicDecoder.html#unityaudioeffectdefinitionflags_isambisonicdecoder) effect definition flag
  * The [`UnityAudioAmbisonicData`](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioDevelopAmbisonicDecoder.html#unityaudioambisonicdata-struct) data struct


### UnityAudioEffectDefinitionFlags_IsAmbisonicDecoder
During the plug-in scanning phase, the `UnityAudioEffectDefinitionFlags_IsAmbisonicDecoder` flag notifies Unity that this is an ambisonic decoder effect. To enable a plug-in to operate as an ambisonic decoder, set a flag in the description bit-field of the effect: 
```
definition.flags |= UnityAudioEffectDefinitionFlags_IsAmbisonicDecoder;

```

Unity lists your plug-in as an option in the Project Settings window (menu: **Edit** > **Project Settings** > **Audio** > **Ambisonic Decoder Plugin**).
### UnityAudioAmbisonicData struct
The `UnityAudioAmbisonicData` struct is similar to the [`UnityAudioSpatializerData`](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSpatializerSDK.html#SpatializerMetaData) struct that Unity passes into spatializers, and contains an `ambisonicOutChannels` integer.
#### The ambisonicOutChannels integer
The Ambisonic decoders run early in the audio pipeline in Unity, and the `ambisonicOutChannels` variable tells the plug-in how many of the output channels Unity needs to use. `ambisonicOutChannels` is automatically set to the `DefaultSpeakerMode`’s channel count.
For example, if you play back a first order ambisonic **audio clip** A container for audio data in Unity. Unity supports mono, stereo and multichannel audio assets (up to eight channels). Unity can import .aif, .wav, .mp3, and .ogg audio file format, and .xm, .mod, .it, and .s3m tracker module formats. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioClip) that has 4 channels, and your speaker mode is stereo (which has only 2 channels):
  * An ambisonic decoder’s process callback passes in 4 for the in and out channel count. 
  * The `ambisonicOutChannels` field is automatically set to 2. 
  * The plug-in outputs its spatialized data to the first 2 channels and zero out the other 2 channels.


## Steps to develop an ambisonic audio decoder plug-in
Follow these steps to develop your own ambisonic audio decoder plug-in for Unity:
  1. Create a custom audio plug-in using the [Native audio plug-in SDK](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioMixerNativeAudioPlugin.html).
  2. Set a flag in the description bit-field of the effect: 
```
definition.flags |= UnityAudioEffectDefinitionFlags_IsAmbisonicDecoder;

```

  3. When you are done configuring your plug-in, compile your file. Make sure it is compilable on your preferred platforms. 
  4. Optionally, convert your file to a .dll file.
  5. Move your plug-in file into your Unity project’s Asset folder. 


For more information on how to work with your ambisonic audio plug-in in Unity, see [Ambisonic Audio](https://docs.unity3d.com/6000.0/Documentation/Manual/AmbisonicAudio.html).
## Formats that Unity ambisonics support
The Unity ambisonic sources framework can support first order ambisonics. The plug-in interface includes information to support binaural stereo and **quad** A primitive object that resembles a plane but its edges are only one unit long, it uses only 4 vertices, and the surface is oriented in the XY plane of the local coordinate space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PrimitiveObjects.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Quad) output, but the plug-in itself determines which outputs are supported. 
Initially, ambisonic decoder plug-ins support first order ambisonic sources and binaural stereo output. There is no support for second order ambisonics.
There is nothing in the framework that’s specific to any of the different ambisonic formats available. If the clip’s format matches the ambisonic decoder plug-in’s expected format, then ambisonic audio should work without issue. Unity’s preferred ambisonic format is B-format, with ACN component ordering, and SN3D normalization.
## Further information
For information on how to develop a plug-in, refer to [Native audio plug-in SDK](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioMixerNativeAudioPlugin.html) and [Audio spatializer SDK](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSpatializerSDK.html). You must also download the [Audio plug-in SDK](https://github.com/Unity-Technologies/NativeAudioPlugins). 
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AmbisonicAudio.html)
Ambisonic Audio
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioReference.html)
Audio Reference
