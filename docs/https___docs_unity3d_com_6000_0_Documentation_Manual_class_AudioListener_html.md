* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioListener.html

  * [Audio](https://docs.unity3d.com/6000.0/Documentation/Manual/Audio.html)
  * [Audio Reference](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioReference.html)
  * Audio Listener


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html)
Audio Clip
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSource.html)
Audio Source
# Audio Listener
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioListener.html "Go to AudioListener page in the Scripting Reference")
The **Audio Listener** acts as a microphone-like device. It receives input from any given [Audio Source](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSource.html)A component which plays back an Audio Clip in the scene to an audio listener or through an audio mixer. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSource.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioSource) in the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) and plays sounds through the computer speakers. For most applications it makes the most sense to attach the listener to the Main [Camera](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html)A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera). If an audio listener is within the boundaries of a [Reverb Zone](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioReverbZone.html) reverberation is applied to all audible sounds in the scene. Furthermore, [Audio Effects](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioEffect.html)Any effect that can modify the output of Audio Mixer components, such as filtering frequency ranges of a sound or applying reverb. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioEffectMixer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioEffect) can be applied to the listener and it will be applied to all audible sounds in the scene. 
![](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/audio_listener_inspector.png)
## Properties
The Audio Listener has no properties. It simply must be added to work. It is always added to the Main Camera by default.
## Details
The Audio Listener works in conjunction with [Audio Sources](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSource.html), allowing you to create the aural experience for your games. When the Audio Listener is attached to a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) in your scene, any Sources that are close enough to the Listener will be picked up and output to the computer’s speakers. Each scene can only have 1 Audio Listener to work properly.
If the Sources are 3D (see import settings in [Audio Clip](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html)A container for audio data in Unity. Unity supports mono, stereo and multichannel audio assets (up to eight channels). Unity can import .aif, .wav, .mp3, and .ogg audio file format, and .xm, .mod, .it, and .s3m tracker module formats. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioClip)), the Listener will emulate position, velocity and orientation of the sound in the 3D world (You can tweak attenuation and 3D/2D behavior in great detail in [Audio Source](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSource.html)) . 2D will ignore any 3D processing. For example, if your character walks off a street into a night club, the night club’s music should probably be 2D, while the individual voices of characters in the club should be mono with their realistic positioning being handled by Unity.
You should attach the Audio Listener to either the Main Camera or to the GameObject that represents the player. Try both to find what suits your game best.
## Hints
  * Each scene can only have one Audio Listener.
  * You access the Project-wide Audio settings using the [Audio](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioManager.html) window (main menu: **Edit** > **Project Settings** , then select the **Audio** category).
  * View the [Audio Clip](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html) Component page for more information about Mono vs Stereo sounds.


AudioListener
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html)
Audio Clip
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSource.html)
Audio Source
