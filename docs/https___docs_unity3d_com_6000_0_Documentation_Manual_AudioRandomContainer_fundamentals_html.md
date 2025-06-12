* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AudioRandomContainer-fundamentals.html

  * [Audio](https://docs.unity3d.com/6000.0/Documentation/Manual/Audio.html)
  * [Audio playlist randomization](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioRandomContainer.html)
  * Audio Random Container fundamentals


[](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioRandomContainer-UI.html)
Audio Random Container reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Create-randomized-playlist.html)
Create a randomized playlist with the Audio Random Container
# Audio Random Container fundamentals
This page describes the audio concepts and terminology that you should understand before you use the Audio Random Container to create a randomized audio playlist.
The concepts you must know are the audio cycle and the AudioSource API exceptions.
## Audio cycle
An audio cycle is the full audio clip list length. If the list has three audio clips, an audio cycle is three clips.
### AudioSource API
Use the AudioSource APIs to start, pause, and stop an Audio Random Container. This is similar to when you use the AudioSource APIs to play, pause, and stop an Audio Clip, but with the following exceptions:
  * isPlaying returns true when the Audio Random Container plays an audio clip through an **audio source** A component which plays back an Audio Clip in the scene to an audio listener or through an audio mixer. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSource.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioSource).
  * AudioSource.Play behaves differently depending on whether you set the Audio Random Container to Manual or Automatic. When set to Manual, the AudioSource.Play triggers a new instance in the Audio Clip list based on the Playback mode.


## Additional resources
Audio Clip, the audio cycle, the AudioSource priority, and the AudioSource API exceptions.
  * [Audio Clips](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html)A container for audio data in Unity. Unity supports mono, stereo and multichannel audio assets (up to eight channels). Unity can import .aif, .wav, .mp3, and .ogg audio file format, and .xm, .mod, .it, and .s3m tracker module formats. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioClip)
  * [Audio Source priority](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSource.html)
  * [Audio Mixer](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioMixer.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioRandomContainer-UI.html)
Audio Random Container reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Create-randomized-playlist.html)
Create a randomized playlist with the Audio Random Container
