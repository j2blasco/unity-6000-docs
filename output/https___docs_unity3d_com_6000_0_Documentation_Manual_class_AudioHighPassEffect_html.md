* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioHighPassEffect.html

  * [Audio](https://docs.unity3d.com/6000.0/Documentation/Manual/Audio.html)
  * [Audio Reference](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioReference.html)
  * [Audio Effects](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioEffectMixer.html)
  * Audio High Pass Effect


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioLowPassEffect.html)
Audio Low Pass Effect
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioEchoEffect.html)
Audio Echo Effect
# Audio High Pass Effect
The **Highpass Effect** passes high frequencies of an AudioMixer group and cuts off signals with frequencies lower than the **Cutoff Frequency**.
## Properties
![The AudioGroup Inspector displays the configurable properties of an Audio High Pass Effect.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AudioHighPassEffect.png) The AudioGroup Inspector displays the configurable properties of an Audio High Pass Effect. **_Property:_** | **_Function:_**  
---|---  
**Cutoff freq** | Highpass cutoff frequency in Hertz (range 10.0 to 22000.0, default = 5000.0).  
**Resonance** | Highpass resonance quality value (range 1.0 to 10.0, default = 1.0).  
## Details
The **Resonance** (short for Highpass Resonance Quality Factor) determines how much the filter’s self-resonance is dampened. Higher highpass resonance quality indicates a lower rate of energy loss, that is the oscillations die out more slowly.
AudioHighPassEffect
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioLowPassEffect.html)
Audio Low Pass Effect
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioEchoEffect.html)
Audio Echo Effect
