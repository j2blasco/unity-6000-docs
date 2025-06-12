* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioEffectMixer.html

  * [Audio](https://docs.unity3d.com/6000.0/Documentation/Manual/Audio.html)
  * [Audio Reference](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioReference.html)
  * Audio Effects


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioChorusFilter.html)
Audio Chorus Filter
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioLowPassEffect.html)
Audio Low Pass Effect
# Audio Effects
You can modify the output of [Audio Mixer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioMixer.html) components by applying **Audio Effects**. These can filter the frequency ranges of the sound or apply reverb and other effects.
The effects are applied by adding effect components to the relevant section of the Audio Mixer. The ordering of the components is important, since it reflects the order in which the effects will be applied to the source audio. For example, in the image below, the Music section of an Audio Mixer is modified first by a Lowpass effect and then a compressor Effect, Flange Effect and so on.
![The Audio Mixer window displays Audio Groups called Master, Music, Reverb, and Effects. The Music group has multiple effect components, including a Compressor, Low Pass, High Pass, and Flange effects.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AudioMixer1.png) The Audio Mixer window displays Audio Groups called Master, Music, Reverb, and Effects. The Music group has multiple effect components, including a Compressor, Low Pass, High Pass, and Flange effects.
To change the ordering of these and any other components, open a context menu in the **inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) and select the _Move Up_ or _Move Down_ commands. Enabling or disabling an effect component determines whether it will be applied or not.
Though highly optimized, some filters are still CPU intensive. Audio CPU usage can monitored in the [profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler) under the Audio Tab.
See the other pages in this section for further information about the specific effect types available.
AudioEffectMixer
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioChorusFilter.html)
Audio Chorus Filter
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioLowPassEffect.html)
Audio Low Pass Effect
