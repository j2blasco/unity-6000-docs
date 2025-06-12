* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/low-level-native-plugin-rendering-extensions.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Compilation and code reload ](https://docs.unity3d.com/6000.0/Documentation/Manual/compilation-and-code-reload.html)
  * [Integrating third-party code libraries (plug-ins)](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)
  * [Low-level native plug-in interface](https://docs.unity3d.com/6000.0/Documentation/Manual/native-plugin-interface.html)
  * Low-level native plug-in rendering extensions


[](https://docs.unity3d.com/6000.0/Documentation/Manual/native-plugin-interface.html)
Low-level native plug-in interface
[](https://docs.unity3d.com/6000.0/Documentation/Manual/low-level-native-plugin-shader-compiler-access.html)
Low-level native plug-in Shader compiler access
# Low-level native plug-in rendering extensions
On top of the [low-level native plug-in interface](https://docs.unity3d.com/6000.0/Documentation/Manual/native-plugin-interface.html), Unity also supports low level rendering extensions that can receive callbacks when certain events happen. This is mostly used to implement and control low-level rendering in your **plug-in** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) and enable it to work with Unity’s multithreaded rendering.
Due to the low-level nature of this extension the plug-in might need to be preloaded before the devices get created. Currently the convention is name-based; the plug-in name must begin _GfxPlugin_ (for example: _GfxPluginMyNativePlugin_).
The rendering extension definition exposed by Unity is in the file _IUnityRenderingExtensions.h_ , provided with the Editor (see file path _Unity\Editor\Data\PluginAPI_).
All platforms supporting **native plug-ins** A platform-specific native code library that is created outside of Unity for use in Unity. Allows you can access features like OS calls and third-party code libraries that would otherwise not be available to Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Nativeplug-in) support these extensions.
## Rendering extensions API
To take advantage of the rendering extension, a plug-in should export _UnityRenderingExtEvent_ and optionally _UnityRenderingExtQuery_. There is a lot of documentation provided inside the include file.
## plug-in callbacks on the rendering thread
A plug-in gets called via _UnityRenderingExtEvent_ whenever Unity triggers one of the built-in events. The callbacks can also be added to CommandBuffers via [CommandBuffer.IssuePluginEventAndData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.IssuePluginEventAndData.html) or [CommandBuffer.IssuePluginCustomBlit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.IssuePluginCustomBlit.html) from **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts).
## Additional resources
  * [Low-level native plug-in shader compiler access](https://docs.unity3d.com/6000.0/Documentation/Manual/low-level-native-plugin-shader-compiler-access.html)
  * [Low-level native plug-in memory manager API](https://docs.unity3d.com/6000.0/Documentation/Manual/low-level-native-plugin-memory-manager-api.html)
  * [Low-level native plug-in memory manager API reference](https://docs.unity3d.com/6000.0/Documentation/Manual/low-level-native-plugin-memory-manager-api-reference.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/native-plugin-interface.html)
Low-level native plug-in interface
[](https://docs.unity3d.com/6000.0/Documentation/Manual/low-level-native-plugin-shader-compiler-access.html)
Low-level native plug-in Shader compiler access
