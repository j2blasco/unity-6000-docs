* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AudioNativePluginImport.html

  * [Audio](https://docs.unity3d.com/6000.0/Documentation/Manual/Audio.html)
  * [Native audio plug-in SDK](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioMixerNativeAudioPlugin.html)
  * Use your native audio DSP plug-in and GUI in Unity


[](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioNativeCustomGUI.html)
Customize the GUI for your audio plug-in 
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioNativePluginExamples.html)
Example native audio plug-ins included in the SDK
# Use your native audio DSP plug-in and GUI in Unity
Once you create your [audio DSP plug-in](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioNativeDSPPlugin.html) and [customize your GUI to your liking](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioNativeCustomGUI.html), you can build your file and import it into Unity. 
## 1. Compile and build your plug-ins
You must implement your **plug-ins** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) as a dynamic library for your preferred platform. Unlike with **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts), any platform that you want to support must be able to compile this file, along with platform-specific optimizations. 
For information about how to build your plug-in into a library file for each platform, refer to [Building plug-ins for desktop platforms](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins-for-desktop.html). 
## 2. Rename your audio plug-in DLL file
  * Add the prefix “audioplugin” to the name of your DLL file (case insensitive). For example `audioplugin-myplugin.dll`


Unlike other **native plug-ins** A platform-specific native code library that is created outside of Unity for use in Unity. Allows you can access features like OS calls and third-party code libraries that would otherwise not be available to Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Nativeplug-in), Unity needs to load audio plug-ins before it creates any mixer assets that might need effects from a plug-in. But Unity doesn’t do this by default. 
Add the prefix “audioplugin” to the name of your DLL file so that the Unity Editor detects and adds your plug-in to a list of plug-ins that Unity automatically loads as the build starts. 
## 3. Import your audio plug-in into Unity
Click and drag your plug-in library file into the Asset folder of your Unity project. Unity automatically installs your plug-in and it is ready to use. 
## 4. Link the plug-in to a platform
Native audio plug-ins use the same scheme as other native or **managed plug-ins** A managed .NET assembly that is created with tools like Visual Studio for use in Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Managedplug-in): You must use the plug-in importer **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) to associate your plug-in with your preferred platforms. For more information, refer to [Plugin Inspector](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-in-inspector.html).
## Additional resources
  * [Audio Mixer](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioMixer.html)
  * [Native audio plug-in SDK](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioMixerNativeAudioPlugin.html)
  * [Audio Spatializer](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSpatializerSDK.html)A plug-in that changes the way audio is transmitted from an audio source into the surrounding space. It takes the source and regulates the gains of the left and right ear contributions based on the distance and angle between the AudioListener and the AudioSource. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioSpatializerSDK.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AudioSpatializer)
  * [Building plug-ins for desktop platforms](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins-for-desktop.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioNativeCustomGUI.html)
Customize the GUI for your audio plug-in 
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AudioNativePluginExamples.html)
Example native audio plug-ins included in the SDK
