* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioEchoFilter.html

  * [Audio](https://docs.unity3d.com/6000.0/Documentation/Manual/Audio.html)
  * [Audio Reference](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioReference.html)
  * [Audio Filters](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioEffect.html)
  * Audio Echo Filter


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioHighPassFilter.html)
Audio High Pass Filter
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioDistortionFilter.html)
Audio Distortion Filter
# Audio Echo Filter
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioEchoFilter.html "Go to AudioEchoFilter page in the Scripting Reference")
The **Audio Echo Filter** repeats a sound after a given **Delay** , attenuating the repetitions based on the **Decay Ratio**.
## Properties
![The AudioGroup Inspector displays the configurable properties of an Audio Echo Filter.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AudioEchoFilter.png) The AudioGroup Inspector displays the configurable properties of an Audio Echo Filter. **_Property:_** | **_Function:_**  
---|---  
**Delay** | Echo delay in ms. 10 to 5000. Default = 500.  
**Decay Ratio** | Echo decay per delay. 0 to 1. 1.0 = No decay, 0.0 = total decay (ie simple 1 line delay). Default = 0.5.L  
**Wet Mix** | Volume of echo signal to pass to output. 0.0 to 1.0. Default = 1.0.  
**Dry Mix** An audio setting that allows you to set the volume of the original signal to pass to output.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DryMix) | Volume of original signal to pass to output. 0.0 to 1.0. Default = 1.0.  
## Details
The **Wet Mix** value determines the amplitude of the filtered signal, where the **Dry Mix** determines the amplitude of the unfiltered sound output.
Hard surfaces reflects the propagation of sound. For example a large canyon can be made more convincing with the Audio Echo Filter.
Sound propagates slower than light - we all know that from lightning and thunder. To simulate this, add an Audio Echo Filter to an event sound, set the Wet Mix to 0.0 and modulate the Delay to the distance between [AudioSource](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSource.html) and [AudioListener](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioListener.html).
AudioEchoFilter
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioHighPassFilter.html)
Audio High Pass Filter
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioDistortionFilter.html)
Audio Distortion Filter
