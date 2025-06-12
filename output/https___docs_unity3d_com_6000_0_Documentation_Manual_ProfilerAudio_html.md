* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerAudio.html

  * [Audio](https://docs.unity3d.com/6000.0/Documentation/Manual/Audio.html)
  * Audio Profiler module


[](https://docs.unity3d.com/6000.0/Documentation/Manual/Create-randomized-playlist.html)
Create a randomized playlist with the Audio Random Container
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AmbisonicAudio.html)
Ambisonic Audio
# Audio Profiler module
The Audio Profiler module monitors the performance of the audio system in your application, such as the total load and voice counts. To open the Profiler window, go to menu: **Window > Analysis > Profiler**.
![The Audio Profiler in the Profiler Window](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/audio-profiler-module.png) The Audio Profiler in the Profiler Window
The Audio **Profiler** A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler) module’s chart tracks the time spent on the audio in your application. The timings are divided into four categories. To change the order of the categories in the chart, you can drag and drop them in the chart’s legend. You can also click a category’s colored legend to toggle its display.
**Chart** | **Description**  
---|---  
**Playing Audio Sources** | The total number of audio sources playing in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) at the frame selected. This is useful to monitor to see if the audio is overloaded.  
**Audio Voices** | The number of audio (FMOD channels) voices used in the selected frame.  
**Total Audio CPU** | The amount of CPU usage the audio used in the selected frame.  
**Total Audio Memory** | The amount of RAM the audio engine used in the selected frame.  
## Module details pane
When you select the Audio Profiler module, the details pane below it displays a breakdown of the audio data for the selected frame. There are two views you can use to inspect the audio profiler data: **Simple** and **Detailed**. To change the display, use the top-left dropdown in the details pane (set to **Simple** by default). 
### Simple view
The **Simple** view contains the following information about the audio data for the frame you selected.
**Data** | **Description**  
---|---  
**Total Audio Sources** | Total number of [audio sources](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSource.html)A component which plays back an Audio Clip in the scene to an audio listener or through an audio mixer. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSource.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioSource) in the Scene.  
**Playing Audio Sources** | Total number of audio sources playing in the Scene  
**Paused Audio Sources** | The total number of paused audio sources in the Scene.  
**Audio Clip Count** | Total number of [audio clips](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html)A container for audio data in Unity. Unity supports mono, stereo and multichannel audio assets (up to eight channels). Unity can import .aif, .wav, .mp3, and .ogg audio file format, and .xm, .mod, .it, and .s3m tracker module formats. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioClip) in the Scene.  
**Audio Voices** | The total number of audio channels (FMOD channels) your Project uses.  
**Total Audio CPU** | The total amount of CPU the audio uses.  
**DSP CPU** | The amount of CPU your Project uses by mixing, **audio effects** Any effect that can modify the output of Audio Mixer components, such as filtering frequency ranges of a sound or applying reverb. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioEffectMixer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioEffect), and decompression of non-streamed sounds that have the [Compressed In Memory](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html) load type. This does not cover the CPU required for sounds that Unity decodes in the background whose load type is **Decompress On Load** and have the **Load In Background** flag checked.  
**Streaming CPU** | The amount of CPU your Project uses to stream the audio in your application.  
**Other CPU** | General CPU overhead not covered by the above.  
**Total Audio Memory** | The amount of memory the audio uses in your Project.  
**Streaming File Memory** | The amount of memory that audio files with the load type of **Streaming** use for short-term buffering of compressed audio data as it is progressively read from disk.  
**Streaming Decode Memory** | The amount of memory that audio files with the load type of **Streaming** use for buffering the decoded sample stream.  
**Sample Sound Memory** | The amount of memory that audio files with the load type of **Decompress On Load** use for the decompressed sample data.  
  
**Note:** Unity pools the memory that the audio system allocates and it keeps growing until it reaches saturation over the run time of your application. The audio system internally reuses the allocated memory, which cannot be compacted during runtime.  
Other Memory | Overhead caused by various subsystems in the audio system.  
### Detailed view
The **Detailed** view contains all of the information in the **Simple** view, and additionally contains detailed per-frame logging of audio events. You can view these either as **Channels** , **Groups** , or **Channels and Groups**. To open this view, open the dropdown at the top of the module details pane, select **Detailed** , and then select one of the views from the **toolbar** A row of buttons and basic controls at the top of the Unity Editor that allows you to interact with the Editor in various ways (e.g. scaling, translation). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Toolbar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Toolbar) at the top of the pane. 
The **Groups** view shows the hierarchy of the buses in the audio mixer. The **Channels and Groups** view displays this information alongside information about the playing sounds.
![The Audio Profiler Groups view](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/audio-profiler-module-groups.png) The Audio Profiler Groups view ![The Audio Profiler Channel and Groups view](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/audio-profiler-module-channel-groups.png) The Audio Profiler Channel and Groups view
Select the **Reset play count on play** to reset the number in the **Plays** column the next time you click Play in the Player window, or when you connect to a new target device.
The information in the detailed view is arranged into the following columns:
**Column** | **Description**  
---|---  
**Object** | The **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) that contains the Audio Source playing the audio.  
**Asset** | The audio Asset that the corresponding GameObject Audio Source is playing.  
**Volume** | The volume the Audio Source applies to the audio. This is a combination of its overall volume property, and the dynamic volume that the distance-dependent attenuation curve applies.  
**Audibility** | The actual level at which the audio plays. This is the sum of the Audio Source’s volume and the other attenuations the mixer channels apply to it.  
**Plays** | The number of times Unity has played the audio. This information is useful to debug logic errors where Unity might not use some audio files.  
**3D** | Displays **YES** if the audio uses [dynamic distance-dependent attenuation](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioMixerOverview.html) and directional panning.  
**Paused** | Displays **YES** if the audio is paused in this frame.  
**Muted** | Displays **YES** if the audio is muted in this frame.  
**Virtual** | Displays **YES** if the audio is suspended because of the **Max Real Voice Count** , which you can set in the [Audio Project Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioManager.html). The **Max Real Voice Count** sets the maximum amount of Audio Sources that Unity simultaneously plays at once. If this displays true, Unity has prioritized other audio that has higher audibility or priority in this frame.  
**OneShot** | Displays **YES** if [AudioSource.PlayOneShot()](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.PlayOneShot.html) played the audio.  
**Looped** | Displays **YES** if [AudioSource.Play()](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.Play.html) played the audio.  
**Distance** | The distance from the Audio Source to the [AudioListener](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioListener.html).  
**MinDist** | The minimum distance defined on the [AudioSource curve editor](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSource.html). This defines a spherical region around the audio where the volume stays at a constant level within it.  
**MaxDist** | The maximum distance defined on the Audio Source curve editor. This defines a spherical region around the audio where the volume stays at a constant level outside of it.  
**Time** | The current relative time in the audio’s playback. While the audio playback is paused, this time does not advance.  
**Duration** | The length of the audio in seconds.  
## Additional resources
  * [Profiler window introduction](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerWindow.html)
  * [Profiling your application](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-profiling-applications.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Create-randomized-playlist.html)
Create a randomized playlist with the Audio Random Container
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AmbisonicAudio.html)
Ambisonic Audio
