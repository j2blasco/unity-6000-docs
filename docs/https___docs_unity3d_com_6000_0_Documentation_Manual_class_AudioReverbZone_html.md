* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioReverbZone.html

  * [Audio](https://docs.unity3d.com/6000.0/Documentation/Manual/Audio.html)
  * [Audio Reference](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioReference.html)
  * Reverb Zones


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioHighPassSimpleEffect.html)
Audio High Pass Simple Effect
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Microphone.html)
Microphone
# Reverb Zones
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioReverbZone.html "Go to AudioReverbZone page in the Scripting Reference")
**Reverb Zones** take an [Audio Clip](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html)A container for audio data in Unity. Unity supports mono, stereo and multichannel audio assets (up to eight channels). Unity can import .aif, .wav, .mp3, and .ogg audio file format, and .xm, .mod, .it, and .s3m tracker module formats. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioClip) and distorts it depending where the **audio listener** A component that acts like a microphone, receiving sound from Audio Sources in the scene and outputting to the computer speakers. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioListener.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioListener) is located inside the reverb zone. They are used when you want to gradually change from a point where there is no ambient effect to a place where there is one, for example when you are entering a cavern.
## Properties
![The AudioGroup Inspector displays the configurable properties of a Reverb Zone.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AudioReverbZone.png) The AudioGroup Inspector displays the configurable properties of a Reverb Zone. **_Property:_** | **_Function:_**  
---|---  
**Min Distance** | Represents the radius of the inner circle in the **gizmo** A graphic overlay associated with a GameObject in a Scene, and displayed in the Scene View. Built-in scene tools such as the move tool are Gizmos, and you can create custom Gizmos using textures or scripting. Some Gizmos are only drawn when the GameObject is selected, while other Gizmos are drawn by the Editor regardless of which GameObjects are selected. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/GizmosMenu.html#GizmosIcons)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Gizmo), this determines the zone where there is a gradually reverb effect and a full reverb zone.  
**Max Distance** | Represents the radius of the outer circle in the gizmo, this determines the zone where there is no effect and where the reverb starts to get applied gradually.  
**Reverb Preset** | Determines the reverb effect that will be used by the reverb zone.  
This diagram illustrates the properties of the reverb zone.
![How the sound works in a reverb zone](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/ReverbZoneExpl.png) How the sound works in a reverb zone
## Hints
You can mix reverb zones to create combined effects.
AudioReverbZone
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioHighPassSimpleEffect.html)
Audio High Pass Simple Effect
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Microphone.html)
Microphone
