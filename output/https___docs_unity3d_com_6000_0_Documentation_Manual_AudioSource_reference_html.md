* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSource-reference.html

  * [Audio](https://docs.unity3d.com/6000.0/Documentation/Manual/Audio.html)
  * [Audio Reference](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioReference.html)
  * [Audio Source](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSource.html)
  * Audio Source component reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSource-overview.html)
Introduction to the Audio Source component
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSource-create.html)
Set up an Audio Source component
# Audio Source component reference
View and edit the properties and settings of the audio source to change how it plays audio.
To open the audio source’s settings, select a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) that contains an **Audio Source** A component which plays back an Audio Clip in the scene to an audio listener or through an audio mixer. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSource.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioSource) component. To learn how to create an audio source, refer to [Set up an Audio Source component](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSource-create.html). 
![The Audio Source Inspector window](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AudioSourceInspector.png) The Audio Source Inspector window
## Audio Source component settings
Use the following settings to change how an audio source plays an audio clip. 
**Property** | **Description**  
---|---  
**Audio Resource** | Reference to the audio resource the audio source will play. You can assign a [Audio Clip](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html) or an [Audio Random Container](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioRandomContainer.html) to this property.  
**Output** | Determines how the audio source will route and process the audio before it reaches the user’s speakers. By default, the clip is output directly to the [Audio Listener](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioListener.html) in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). Use this property to output the clip to an [Audio Mixer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioMixer.html) instead.  
**Mute** | If you enable this property, the audio track still plays but makes no audible sound.  
**Spatialize** | Enables or disables custom spatialization for the Audio Source. This property is only available if you install an [audio spatializer SDK](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSpatializerSDK.html), and select it in your project’s global [audio](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioManager.html) settings.  
**Spatialize Post Effect** | Determines whether the Audio Source applies the custom spatializer before or after other effects. Enable this property to apply the custom spatializer after other effects attached to the Audio Source. This property is only available if you enable the **Spatialize** property for the Audio Source.  
**Bypass Effects** | Enable this property to ignore any filter effects applied to the audio source. This is a simpler way to turn all effects on/off.  
**Bypass Listener Effects** | Enable this property to ignore all Listener effects on the audio source. This is a simpler way to toggle listener effects.  
**Bypass Reverb Zones** | Enable this property to ignore all Reverb Zones in the scene. This lets you toggle whether any environmental reverb effects affect the audio.  
**Play On Awake** Set this to true to make an Audio Source start playing on awake [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PlayOnAwake) | Enable this property to play the sound the moment the scene launches. If you disable this property, you need to use the `Play()` command in your **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) to start the audio.  
**Loop** | Enable this to make the **Audio Clip** A container for audio data in Unity. Unity supports mono, stereo and multichannel audio assets (up to eight channels). Unity can import .aif, .wav, .mp3, and .ogg audio file format, and .xm, .mod, .it, and .s3m tracker module formats. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioClip) loop when it reaches the end.  
**Priority** | Determines the priority of this audio source among all the ones that coexist in the scene. (Priority: 0 is most important, while 256 is least important. Default is 128.). Use 0 for music tracks to avoid it getting occasionally swapped out.  
**Volume** | How loud the sound is at a distance of one world unit (1 m) from the **Audio Listener** A component that acts like a microphone, receiving sound from Audio Sources in the scene and outputting to the computer speakers. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioListener.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioListener).  
**Pitch** | Amount of change in pitch due to slowdown/speed up of the **Audio Clip**. Value 1 is normal playback speed.  
**Stereo Pan** | Sets the position in the stereo field of 2D sounds.  
**Spatial Blend** | Sets how much the 3D engine has an effect on the audio source.  
**Reverb Zone Mix** | Sets the amount of the output signal that gets routed to the reverb zones. The amount is linear in the 0 to 1 range, but allows for a 10 dB amplification in the 1 to 1.1 range which can be useful to achieve the effect of near-field and distant sounds.  
### 3D Sound settings
The following settings are applied proportionally to the **Spatial Blend** parameter.
**Property** | **Description**  
---|---  
**Doppler Level** | Determines how much Doppler effect you want to apply to this audio source. For no effect, set this to 0.  
**Spread** | Sets the spread angle to 3D stereo or multichannel sound in speaker space.  
**Min Distance** | Within the MinDistance, the sound will stay at the maximum volume. Outside MinDistance, attenuation begins. Increase the MinDistance of a sound to make it ‘louder’ in a 3D world, and decrease it to make it ‘quieter’ in a 3D world.  
**Max Distance** | In linear mode, this is the point where the volume reaches zero and the sound becomes inaudible. For custom curves, this is the distance where the sound stops attenuation and stays constant. If you use **Logarithmic Rolloff** , Unity ignores this setting.  
**Volume Rolloff** | How fast the sound fades. The higher the value, the closer the listener has to be before they can hear the sound.  
**- Logarithmic Rolloff** | The sound is loud when you’re close to the audio source and quickly disappears as you initially move away, but then slowly tapers off progressively and never quite disappears. This is more physically accurate and good for more localized sources of sounds.  
**- Linear Rolloff** | The further away from the audio source you go, the less you can hear it. But, due to how hearing perception is logarithmic, this makes sounds appear more present at further distances and less localized.  
**- Custom Rolloff** | The sound from the audio source behaves according to how you set the **Volume** distance curve.  
![Rolloff Modes that an audio source can have.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/TypesOfRollOff.png) Rolloff Modes that an audio source can have.
## Distance functions Curve Editor
The **Audio Source** component contains a group of curves you can use to modify several properties of the audio. These curves represent each property as a function of the distance between the audio source and the audio listener. 
The following are audio properties you can use the curves to configure:
**Property** | **Description**  
---|---  
**Volume** | Defines how loud the audio is (0.0 to 1.0) as its distance from the audio listener changes. If you edit this curve, Unity automatically changes the **Volume Rolloff** to **Custom Rolloff**.  
**Spatial Blend** | 2D (original channel mapping) to 3D (all channels down-mixed to mono and attenuated according to distance and direction).  
**Spread** | Angle (degrees 0.0 to 360.0) over distance.  
**Low-Pass** | Cutoff frequency (22000.0 to 10.0) over distance. This property only appears if you attach a LowPassFilter component to the same GameObject as the audio source.  
**Reverb Zone** | Amount of signal routed to the reverb zones. Note that the volume property and distance and directional attenuation are applied to the signal first and therefore affect both the direct and reverberated signals.  
![Distance functions for Volume, Spatial Blend, Spread, Low-Pass audio filter, and Reverb Zone Mix. The current distance to the Audio Listener is marked in the graph by the red vertical line.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AudioDistanceFunctions.png) Distance functions for Volume, Spatial Blend, Spread, Low-Pass audio filter, and Reverb Zone Mix. The current distance to the Audio Listener is marked in the graph by the red vertical line.
To modify the distance functions, you can edit the curves directly. For more information, refer to the guide to [Editing Curves](https://docs.unity3d.com/6000.0/Documentation/Manual/EditingCurves.html).
## Additional resources
  * [Audio Source](https://docs.unity3d.com/6000.0/Documentation/Manual/Class-AudioSource.html)
  * [Introduction to the Audio Source component](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSource-overview.html)
  * [Set up an Audio Source component](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSource-create.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSource-overview.html)
Introduction to the Audio Source component
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSource-create.html)
Set up an Audio Source component
