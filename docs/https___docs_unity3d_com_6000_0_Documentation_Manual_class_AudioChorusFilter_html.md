* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioChorusFilter.html

  * [Audio](https://docs.unity3d.com/6000.0/Documentation/Manual/Audio.html)
  * [Audio Reference](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioReference.html)
  * [Audio Filters](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioEffect.html)
  * Audio Chorus Filter


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioReverbFilter.html)
Audio Reverb Filter
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioEffectMixer.html)
Audio Effects
# Audio Chorus Filter
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioChorusFilter.html "Go to AudioChorusFilter page in the Scripting Reference")
The **Audio Chorus Filter** takes an [Audio Clip](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html)A container for audio data in Unity. Unity supports mono, stereo and multichannel audio assets (up to eight channels). Unity can import .aif, .wav, .mp3, and .ogg audio file format, and .xm, .mod, .it, and .s3m tracker module formats. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioClip) and processes it creating a chorus effect. 
## Properties
![The AudioGroup Inspector displays the configurable properties of an Audio Chorus Filter.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AudioChorusFilter.png) The AudioGroup Inspector displays the configurable properties of an Audio Chorus Filter. **_Property:_** | **_Function:_**  
---|---  
**Dry Mix** An audio setting that allows you to set the volume of the original signal to pass to output.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DryMix) | Volume of original signal to pass to output. 0.0 to 1.0. Default = 0.5.  
**Wet Mix 1** | Volume of 1st chorus tap. 0.0 to 1.0. Default = 0.5.  
**Wet Mix 2** | Volume of 2nd chorus tap. This tap is 90 degrees out of phase of the first tap. 0.0 to 1.0. Default = 0.5.  
**Wet Mix 3** | Volume of 3rd chorus tap. This tap is 90 degrees out of phase of the second tap. 0.0 to 1.0. Default = 0.5.  
**Delay** | The LFO’s delay in ms. 0.1 to 100.0. Default = 40.0 ms  
**Rate** | The LFO’s modulation rate in Hz. 0.0 to 20.0. Default = 0.8 Hz.  
**Depth** | Chorus modulation depth. 0.0 to 1.0. Default = 0.03.  
**Feed Back** | Chorus feedback. Controls how much of the wet signal gets fed back into the filter’s buffer. 0.0 to 1.0. Default = 0.0.  
## Details
The chorus effect modulates the original sound by a sinusoid low frequency oscillator (LFO). The output sounds like there are multiple sources emitting the same sound with slight variations - resembling a choir.
You can tweak the chorus filter to create a flanger effect by lowering the feedback and decreasing the delay, as the flanger is a variant of the chorus.
Creating a simple, dry echo is done by setting **Rate** and **Depth** to 0 and tweaking the mixes and **Delay**
AudioChorusFilter
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioReverbFilter.html)
Audio Reverb Filter
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioEffectMixer.html)
Audio Effects
