* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioLowPassFilter.html

  * [Audio](https://docs.unity3d.com/6000.0/Documentation/Manual/Audio.html)
  * [Audio Reference](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioReference.html)
  * [Audio Filters](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioEffect.html)
  * Audio Low Pass Filter


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioEffect.html)
Audio Filters
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioHighPassFilter.html)
Audio High Pass Filter
# Audio Low Pass Filter
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioLowPassFilter.html "Go to AudioLowPassFilter page in the Scripting Reference")
The **Audio Low Pass Filter** passes low frequencies of an [AudioSource](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSource.html) or all sound reaching an [AudioListener](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioListener.html) while removing frequencies higher than the **Cutoff Frequency**.
## Properties
![The AudioGroup Inspector displays the configurable properties of an Audio Low Pass Filter.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AudioLowPassFilter.png) The AudioGroup Inspector displays the configurable properties of an Audio Low Pass Filter. **_Property:_** | **_Function:_**  
---|---  
**Cutoff Frequency** | Lowpass cutoff frequency in Hertz (range 0.0 to 22000.0, default = 5000.0).  
**Lowpass Resonance Q** | Lowpass resonance quality value (range 1.0 to 10.0, default = 1.0).  
## Details
The **Lowpass Resonance Q** (short for Lowpass Resonance Quality Factor) determines how much the filter’s self-resonance is dampened. Higher lowpass resonance quality indicates a lower rate of energy loss, that is the oscillations die out more slowly.
The **Audio Low Pass Filter** has a Rolloff curve associated with it, making it possible to set **Cutoff Frequency** over distance between the AudioSource and the AudioListener.
Sounds propagates very differently given the environment. For example, to compliment a visual fog effect add a subtle low-pass to the **Audio Listener** A component that acts like a microphone, receiving sound from Audio Sources in the scene and outputting to the computer speakers. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioListener.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioListener). The high frequencies of a sound being emitted from behind a door will be filtered out by the door and so won’t reach the listener. To simulate this, simply change the Cutoff Frequency when opening the door.
AudioLowPassFilter
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioEffect.html)
Audio Filters
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioHighPassFilter.html)
Audio High Pass Filter
