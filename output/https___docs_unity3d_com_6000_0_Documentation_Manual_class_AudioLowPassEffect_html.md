* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioLowPassEffect.html

  * [Audio](https://docs.unity3d.com/6000.0/Documentation/Manual/Audio.html)
  * [Audio Reference](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioReference.html)
  * [Audio Effects](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioEffectMixer.html)
  * Audio Low Pass Effect


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioEffectMixer.html)
Audio Effects
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioHighPassEffect.html)
Audio High Pass Effect
# Audio Low Pass Effect
The **Audio Low Pass Effect** passes low frequencies of an [AudioMixer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioMixer.html) group while removing frequencies higher than the **Cutoff Frequency**.
## Properties
![The AudioGroup Inspector displays the configurable properties of an Audio Low Pass Effect.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AudioLowPassEffect.png) The AudioGroup Inspector displays the configurable properties of an Audio Low Pass Effect. **_Property:_** | **_Function:_**  
---|---  
**Cutoff freq** | Lowpass cutoff frequency in Hertz (range 10.0 to 22000.0, default = 5000.0).  
**Resonance** | Lowpass resonance quality value (range 1.0 to 10.0, default = 1.0).  
## Details
The **Resonance** (short for Lowpass Resonance Quality Factor) determines how much the filter’s self-resonance is dampened. Higher lowpass resonance quality indicates a lower rate of energy loss, that is the oscillations die out more slowly.
AudioLowPassEffect
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioEffectMixer.html)
Audio Effects
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioHighPassEffect.html)
Audio High Pass Effect
