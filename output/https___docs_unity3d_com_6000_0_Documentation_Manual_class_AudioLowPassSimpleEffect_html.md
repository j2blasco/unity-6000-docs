* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioLowPassSimpleEffect.html

  * [Audio](https://docs.unity3d.com/6000.0/Documentation/Manual/Audio.html)
  * [Audio Reference](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioReference.html)
  * [Audio Effects](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioEffectMixer.html)
  * Audio Low Pass Simple Effect


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioReverbEffect.html)
Audio SFX Reverb Effect
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioHighPassSimpleEffect.html)
Audio High Pass Simple Effect
# Audio Low Pass Simple Effect
The **Audio Low Pass Simple Effect** passes low frequencies of an [AudioMixer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioMixer.html) group while removing frequencies higher than the **Cutoff Frequency**.
## Properties
![The AudioGroup Inspector displays the configurable property of an Audio Low Pass Simple Effect.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AudioLowPassSimpleEffect.png) The AudioGroup Inspector displays the configurable property of an Audio Low Pass Simple Effect. **_Property:_** | **_Function:_**  
---|---  
**Cutoff freq** | Lowpass cutoff frequency in Hertz (range 10.0 to 22000.0, default = 5000.0).  
## Details
The **Resonance** (short for Lowpass Resonance Quality Factor) determines how much the filter’s self-resonance is dampened. Higher lowpass resonance quality indicates a lower rate of energy loss, that is the oscillations die out more slowly.
For additional control over the resonance value of the low pass filter use the [Audio Low Pass effect](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioLowPassEffect.html).
AudioLowPassSimpleEffect
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioReverbEffect.html)
Audio SFX Reverb Effect
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioHighPassSimpleEffect.html)
Audio High Pass Simple Effect
