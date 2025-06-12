* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSource-overview.html

  * [Audio](https://docs.unity3d.com/6000.0/Documentation/Manual/Audio.html)
  * [Audio Reference](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioReference.html)
  * [Audio Source](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSource.html)
  * Introduction to the Audio Source component


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSource.html)
Audio Source
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSource-reference.html)
Audio Source component reference
# Introduction to the Audio Source component
Attach an **Audio Source** component to a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) to control how and where sounds play in your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). 
Audio sources are components that let you integrate sound effects, music, commentary, and other audio features into your application. 
They interact with other audio components in Unity that allow you to edit, enhance, and output sound in your scene, including: 
  * Audio Clips
  * Audio Random Containers
  * Audio Listeners
  * Audio Mixers


This page covers how the audio source interacts with these audio components. For more information about the **Audio Source** component’s properties and how to set up the component, refer to [Audio Source component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSource-reference.html) and [Set up an Audio Source component](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSource-create.html).
## Audio resources
The **Audio Source** component requires an audio resource to play sound in your scene. Audio resources are containers that hold the actual audio data, so you must assign one to the Audio Source so it has audio data to edit and play. For instructions, refer to [Assign an audio resource to your audio source](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSource-create.html#assign-an-audio-resource-to-your-audio-source).
The following Unity file types are audio resources: 
  * [Audio Clip](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html)A container for audio data in Unity. Unity supports mono, stereo and multichannel audio assets (up to eight channels). Unity can import .aif, .wav, .mp3, and .ogg audio file format, and .xm, .mod, .it, and .s3m tracker module formats. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioClip)
  * [Audio Random Container](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioRandomContainer.html)


Refer to those pages for more information about each type and for the audio file formats Unity supports. 
## Output method of the audio source
In the **Audio Source** component, the **Output** property specifies where the audio source will send the audio signal in the audio processing pipeline.
This property accepts an **Audio Mixer Group**. The Audio Mixer is a tool that lets you post-process the audio with effects. You can then assign your Audio Mixer to the property to make sure your audio source applies your effects to the audio. 
If you set the property to **None** , the sound will bypass your mixer and the audio will play without your effects. This is the default behavior. 
Then, any **Audio Listener** components in the scene detects the audio from nearby audio sources, and outputs the audio to the user so they can hear it. Audio listeners are usually found on **cameras** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) in the scene, but you can also assign them to other objects. 
For more information about these components, refer to [Audio Listener](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioListener.html)A component that acts like a microphone, receiving sound from Audio Sources in the scene and outputting to the computer speakers. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioListener.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioListener) and [Audio Mixer](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioMixer.html).
## Configure your audio source
You can configure the audio source to play the clip as 2D, 3D, or as a mixture (_SpatialBlend_). The audio can be spread out between speakers (stereo to 7.1) (_Spread_) and morphed between 3D and 2D (_SpatialBlend_). 
If you set **SpatialBlend** to `0.0f`, then Unity will treat the audio clip as a 2D sound. If you set it to `1.0f`, the clip is fully 3D. Anything in between is a blend of 2D and 3D.
Use falloff curves to control the spread over distance. Also, if the [listener](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioListener.html) is within one or multiple [Reverb Zones](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioReverbZone.html), this applies reverberation to the source. You can also apply individual filters to each audio source for an even richer audio experience. For more details, refer to [Audio Effects](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioEffect.html)Any effect that can modify the output of Audio Mixer components, such as filtering frequency ranges of a sound or applying reverb. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioEffectMixer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioEffect).
For a list of Audio Source settings, refer to [Audio Source component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSource-reference.html). 
## API resources
The following is a list of useful API for AudioSource and its related properties. 
  * [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html)
  * [AudioClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioClip.html)
  * [AudioListener](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioListener.html)
  * [AudioMixer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Audio.AudioMixer.html)


## Additional resources
  * [Audio Source](https://docs.unity3d.com/6000.0/Documentation/Manual/Class-AudioSource.html)A component which plays back an Audio Clip in the scene to an audio listener or through an audio mixer. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSource.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioSource)
  * [Introduction to the Audio Source component](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSource-overview.html)
  * [Set up an Audio Source component](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSource-create.html)
  * [Audio Source component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSource-reference.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSource.html)
Audio Source
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSource-reference.html)
Audio Source component reference
