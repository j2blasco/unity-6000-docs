* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioEffect.html

  * [Audio](https://docs.unity3d.com/6000.0/Documentation/Manual/Audio.html)
  * [Audio Reference](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioReference.html)
  * Audio Filters


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioMixer.html)
Audio Mixer
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioLowPassFilter.html)
Audio Low Pass Filter
# Audio Filters
You can modify the output of [Audio Source](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSource.html)A component which plays back an Audio Clip in the scene to an audio listener or through an audio mixer. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSource.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioSource) and [Audio Listener](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioListener.html)A component that acts like a microphone, receiving sound from Audio Sources in the scene and outputting to the computer speakers. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioListener.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioListener) components by applying **Audio Effects** Any effect that can modify the output of Audio Mixer components, such as filtering frequency ranges of a sound or applying reverb. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioEffectMixer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioEffect). These can filter the frequency ranges of the sound or apply reverb and other effects.
The effects are applied by adding effect components to the object with the Audio Source or Audio Listener. The ordering of the components is important, since it reflects the order in which the effects will be applied to the source audio. For example, in the image below, an Audio Listener is modified first by an **Audio Low Pass Filter** An audio filter that passes low frequencies of an Audio Source or all sound reaching an Audio Listener while removing frequencies higher than the Cutoff Frequency. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioLowPassFilter.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioLowPassFilter) and then an Audio Chorus Filter.
![The Audio Inspector displays an Audio Listener component followed by the Audio Low Pass Filter and Audio Chorus Filter components that modify it.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/FilterGraph1.png) The Audio Inspector displays an Audio Listener component followed by the Audio Low Pass Filter and Audio Chorus Filter components that modify it.
To change the ordering of these and any other components, open a context menu in the **inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) and select the _Move Up_ or _Move Down_ commands. Enabling or disabling an effect component determines whether it will be applied or not.
Though highly optimized, some filters are still CPU intensive. Audio CPU usage can monitored in the [profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler) under the Audio Tab.
See the other pages in this section for further information about the specific filter types available.
AudioEffect
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioMixer.html)
Audio Mixer
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioLowPassFilter.html)
Audio Low Pass Filter
