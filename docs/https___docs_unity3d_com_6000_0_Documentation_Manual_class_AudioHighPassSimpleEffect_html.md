* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioHighPassSimpleEffect.html

  * [Audio](https://docs.unity3d.com/6000.0/Documentation/Manual/Audio.html)
  * [Audio Reference](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioReference.html)
  * [Audio Effects](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioEffectMixer.html)
  * Audio High Pass Simple Effect


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioLowPassSimpleEffect.html)
Audio Low Pass Simple Effect
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioReverbZone.html)
Reverb Zones
# Audio High Pass Simple Effect
The **Highpass Simple Effect** passes high frequencies of an AudioMixer group and cuts off signals with frequencies lower than the **Cutoff Frequency**.
## Properties
![The AudioGroup Inspector displays the configurable property of an Audio High Pass Simple Effect.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AudioHighPassSimpleEffect.png) The AudioGroup Inspector displays the configurable property of an Audio High Pass Simple Effect. **_Property:_** | **_Function:_**  
---|---  
**Cutoff freq** | Highpass cutoff frequency in Hertz (range 10.0 to 22000.0, default = 5000.0).  
## Details
The **Resonance** (short for Highpass Resonance Quality Factor) determines how much the filter’s self-resonance is dampened. Higher highpass resonance quality indicates a lower rate of energy loss, that is the oscillations die out more slowly.
For additional control over the resonance value of the high pass filter use the [Audio High Pass effect](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioHighPassEffect.html).
AudioHighPassSimpleEffect
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioLowPassSimpleEffect.html)
Audio Low Pass Simple Effect
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioReverbZone.html)
Reverb Zones
