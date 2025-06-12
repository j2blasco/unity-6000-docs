* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AudioMixerNativeAudioPlugin.html

  * [Audio](https://docs.unity3d.com/6000.0/Documentation/Manual/Audio.html)
  * Native audio plug-in SDK


[](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioMixerUsage.html)
Overview of Usage and API
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioNativeDSPPlugin.html)
Develop a native DSP audio plug-in
# Native audio plug-in SDK
The Unity native audio **plug-in** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) SDK lets you develop custom audio plug-ins for Unity. You can use this SDK to extend the audio capabilities of Unity and create advanced audio processing solutions tailored to your project’s needs. Examples of custom audio plug-ins you can create include **audio effects** Any effect that can modify the output of Audio Mixer components, such as filtering frequency ranges of a sound or applying reverb. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioEffectMixer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioEffect) and **audio spatializers** A plug-in that changes the way audio is transmitted from an audio source into the surrounding space. It takes the source and regulates the gains of the left and right ear contributions based on the distance and angle between the AudioListener and the AudioSource. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSpatializerSDK.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioSpatializer).
The native audio plug-in system consists of two parts: 
  * The native audio Digital Signal Processing (DSP) plug-in
  * The managed graphical user interface (GUI)


Refer to the following pages to learn more about how to create an audio plug-in, customize the plug-in’s GUI, and access useful examples. 
**Topic** | **Description**  
---|---  
**[Develop a native audio DSP plug-in for Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioNativeDSPPlugin.html)** | Learn how to create your own native DSP plug-in.  
**[Customize the Unity GUI for your audio plug-in](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioNativeCustomGUI.html)** | Learn how to customize the GUI of your audio plug-in.  
**[Import your audio plug-in and GUI to Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioNativePluginImport.html)** | Learn how to prepare your plug-in and GUI for Unity and import them.  
**[Example plug-ins](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioNativePluginExamples.html)** | Example DSP plug-ins with and without GUI customization.  
## Important files your DSP and GUI code uses
The `AudioPluginInterface.h` file has the necessary structures, types, and function declarations required to create a custom audio plug-in. 
Both native DSP and GUI DLLs can contain multiple plug-ins. To add multiple plug-in effects within the same DLL, Unity provides additional code to handle the effect definition and parameter registration in a unified manner:
  * `AudioPluginUtil.h`
  * `AudioPluginUtil.cpp`


If you want your DLLs to contain multiple effects, include `AudioPluginUtil.h` in your code. 
## Additional resources
  * [Audio Mixer](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioMixer.html)
  * [Audio Spatializer SDK](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSpatializerSDK.html)
  * [Ambisonic Audio](https://docs.unity3d.com/6000.0/Documentation/Manual/AmbisonicAudio.html)


* * *
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioMixerUsage.html)
Overview of Usage and API
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioNativeDSPPlugin.html)
Develop a native DSP audio plug-in
