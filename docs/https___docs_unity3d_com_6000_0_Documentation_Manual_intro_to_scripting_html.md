* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/intro-to-scripting.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Get started with scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-get-started.html)
  * Introduction to scripting


[](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-get-started.html)
Get started with scripting
[](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)
Creating scripts
# Introduction to scripting
Unity is customizable and extensible by design and almost everything is scriptable to some extent. Many items you can configure through the various [Editor views](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html) have a corresponding public C# class representation that you can interact with in code.
You can use Editor APIs to customize and extend the Editor authoring tools to improve your development workflows. You can use Engine APIs to define the runtime functionality of your application, including graphics, physics, character behavior, and responses to user input.
The [Scripting API reference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/index.html) provides the complete and authoritative reference for all public Unity APIs. The Manual provides additional context and guidance.
## The Unity scripting environment
Unity supports scripting in the C# programming language. C# (pronounced C-sharp) is a managed, object-oriented programming language, which is part of the .NET platform and runs in the cross-platform .NET runtime. Other .NET languages can be used with Unity if they can compile a compatible DLL, refer to [Managed plugins](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins-managed.html) for further details.
The scripting environment refers to both:
  * Your own local environment or context in which you’re writing code. This includes your code editor (IDE) and integrated source control solution and operating system.
  * The C# scripting enviroment Unity provides. A given version of Unity supports given versions of the .NET platform, which determines the .NET libraries you can use in your code.


For more information on the scripting environment and tools, refer to [Environment and tools](https://docs.unity3d.com/6000.0/Documentation/Manual/environment-and-tools.html).
## How scripting in Unity works
C# scripts (files with a `.cs` file extension) are [assets](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetWorkflow.html)Any media or data that can be used in your game or project. An asset may come from a file created outside of Unity, such as a 3D Model, an audio file or an image. You can also create some asset types in Unity, such as an Animator Controller, an Audio Mixer or a Render Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetWorkflow.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Asset) in your project, stored in the `Assets` folder and saved as part of the [asset database](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetDatabase.html). You can create template scripts that derive from the common [built-in Unity types](https://docs.unity3d.com/6000.0/Documentation/Manual/fundamental-unity-types.html) through the **Scripting** submenu of the **Assets > Create** menu.
You configure a default [External Script Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/Preferences.html#external-tools), which is the program Unity opens your script assets in for editing. Usually this will be one of the [supported IDEs](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-ide-support.html) for Unity development.
You can create your own regular C# types and logic to use in your game, as long as the code you write is compatible with the active [.NET profile](https://docs.unity3d.com/6000.0/Documentation/Manual/dotnet-profile-support.html). But your scripted types gain additional functionality in Unity when they inherit from a built-in Unity type.
If your custom types inherit from [UnityEngine.Object](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Object.html), they’ll be assignable to fields in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window. Inheriting from [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MonoBehaviour.html) allows a script to be attached to a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) as a component to control the behaviour of a GameObject in a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). 
For more information on fundamental Unity types you can inherit from, refer to [Fundamental Unity types](https://docs.unity3d.com/6000.0/Documentation/Manual/fundamental-unity-types.html).
For more information on viewing **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) and editing script components in the Inspector, refer to [Inspecting scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/inspecting-scripts.html).
## Compilation and code reload
[Compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/script-compilation.html) transforms the C# code you write into code that runs on a given target platform. Some aspects of compilation are under your control and others aren’t. By [organizing your scripts into assemblies](https://docs.unity3d.com/6000.0/Documentation/Manual/assembly-definition-files.html) you can reduce unnecessary recompilation and manage your dependencies effectively. With [conditional compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/conditional-compilation.html) you can selectively include or exlcude sections of your code from compilation.
Depending on your settings, Unity [recompiles and reloads your code](https://docs.unity3d.com/6000.0/Documentation/Manual/compilation-and-code-reload.html) in various contexts. Reloading code is important for changes to take effect or to preserve state when transitioning between Edit mode and Play mode, but it also impacts performance and iteration times. It’s important to understand these costs and how you can configure Unity’s code reload behavior to mitigate them.
## Additional resources
  * [Creating scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)
  * [Naming scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/naming-scripts.html)
  * [Scripts in the Inspector window](https://docs.unity3d.com/6000.0/Documentation/Manual/inspecting-scripts.html)
  * [Fundamental Unity types](https://docs.unity3d.com/6000.0/Documentation/Manual/fundamental-unity-types.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-get-started.html)
Get started with scripting
[](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)
Creating scripts
