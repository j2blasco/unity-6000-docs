* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins-managed.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Compilation and code reload ](https://docs.unity3d.com/6000.0/Documentation/Manual/compilation-and-code-reload.html)
  * [Integrating third-party code libraries (plug-ins)](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)
  * Managed plug-ins


[](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-in-inspector.html)
Import and configure plug-ins 
[](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins-native.html)
Native plug-ins
# Managed plug-ins
Managed **plug-ins** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) are [.NET assemblies](https://docs.unity3d.com/6000.0/Documentation/Manual/dotnet-profile-support.html) you create and compile outside of Unity, into a dynamically linked library (DLL) with tools such as Visual Studio.
This is a different process from standard C# **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts), which Unity stores as source files in the Assets folder in your Unity project. Unity compiles standard C# scripts whenever they change, whereas DLLs are pre-compiled and don’t change. You can add a compiled .dll file to your project and attach the classes it contains to ****GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject)** in the same way as standard scripts.
For more information about managed code in C#, see [Microsoft’s What is managed code? documentation](https://docs.microsoft.com/en-us/dotnet/standard/managed-code).
Managed plug-ins contain only .NET code, which means they can’t access any features that the .NET libraries don’t support. However, managed code is accessible to the standard .NET tools that Unity uses to compile scripts.
When you work with DLLs in Unity, you must complete more steps than when you work with scripts. However, there are situations where you might find it helpful to create and add a .dll file to your Unity project instead, for example:
  * You want to use compilers in your code that Unity doesn’t support.
  * You want to add third-party .NET code in a .dll file.
  * You want to supply code to Unity without the source.


This page explains a general method you can use to create **managed plug-ins** A managed .NET assembly that is created with tools like Visual Studio for use in Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Managedplug-in), as well as how you can create managed plug-ins and set up a debug session using Visual Studio.
## Creating a managed plug-in
To create a managed plug-in, you need to create a DLL. To do this, you need a suitable compiler, such as:
  * [Visual Studio](https://visualstudio.microsoft.com/)
  * [MsBuild](https://docs.microsoft.com/en-us/visualstudio/msbuild/msbuild?view=vs-2019)
  * [.NET SDK](https://docs.microsoft.com/en-us/dotnet/core/sdk)


Not all compilers that produce .NET code are compatible with Unity, so you should test the compiler with some available code before doing significant work with it. For information on the .NET profiles Unity currently supports, refer to [.NET profile support](https://docs.unity3d.com/6000.0/Documentation/Manual/dotnet-profile-support.html).
The method you use to create a DLL depends on if the DLL contains Unity API code:
  * If the DLL contains Unity API code, you need to make Unity’s own DLLs available to the compiler before compiling: 
    1. To find the Unity DLLs: 
       * On Windows, go to: `C:\Program Files\Unity\Hub\Editor\<version-number>\Editor\Data\Managed\UnityEngine`
       * On macOS: 
         1. Find the `Unity.app` file on your computer. The path to the Unity DLLs on macOS is: `/Applications/Unity/Hub/Editor/<version-number>/Unity.app/Contents/Managed/UnityEngine`
         2. Right click on `Unity.app`
         3. Select **Show Package Contents**.
    2. The `UnityEngine` folder contains the .dll files for a number of modules. Reference them to make them available to your script. Some namespaces also require a reference to a compiled library from a Unity project (for example, `UnityEngine.UI`). Locate this in the project folder’s directory: `~\Library\ScriptAssemblies`
  * If the DLL does not contain Unity API code, or if you’ve already made the Unity DLLs available, follow your compiler’s documentation to compile a .dll file.The exact options you use to compile the DLL depend on the compiler you use. As an example, the command line for the Roslyn compiler, `csc`, might look like this on macOS:


`csc /r:/Applications/Unity/Hub/Editor/<version-number>/Unity.app/Contents/Managed/UnityEngine.dll /target:library /out:MyManagedAssembly.dll /recurse:*.cs`
In this example:
  * Use the `/r` option to specify a path to a library to include in the build, in this case, the `UnityEngine` library.
  * Use the `/target` option to specify the type of build you require; “library” signifies a DLL build.
  * Use `/out` to specify the name of the library, which in this case is “MyManagedAssembly.dll”.
  * Add the name of the source files to be included. Use the `/recurse` method to add all the files ending in “.cs’’ in your current working directory and any subfolders. The resulting .dll file appears in the same folder as the source files.


## Using a managed plug-in
After you’ve compiled the DLL, you can drag the .dll file into the Unity project like any other asset. You can then:
  * Expand the managed plug-in to view the separate classes inside the library.
  * Drag classes that derive from MonoBehaviour onto Game Objects.
  * Use non-MonoBehaviour classes directly from other scripts.

![An expanded DLL with the classes visible](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/managed-plugin.png) An expanded DLL with the classes visible
## Create a DLL with Visual Studio
This section explains:
  * How to build and integrate a simple DLL example with Visual Studio
  * How to prepare a debugging session for the DLL in Unity.


### Setting up the Project
  1. Open Visual Studio and create a new project.
  2. Select **File** > **New** > **Project** > **Visual C#** > **.Net Standard** > **Class Library (.NET Standard)**.
  3. Add the following information to the new library: 
     * **Name** : The namespace (for this example, use `DLLTest` as the name).
     * **Location** : The parent folder of the project.
     * **Solution name** : The folder of the project.
  4. Make the Unity DLLs available to your script. In Visual Studio, open the contextual menu for **References** in the Solution Explorer and select **Add Reference** > **Browse** > **Select File**.
  5. Select the required .dll file, located in the UnityEngine folder.


### Coding the DLL
  1. For this example, rename the default class to `MyUtilities` in the Solution browser.
  2. Replace its code with the following:

```
using System;   
using UnityEngine;

namespace DLLTest {

    public class MyUtilities {
    
        public int c;

        public void AddValues(int a, int b) {
            c = a + b;  
        }
    
        public static int GenerateRandom(int min, int max) {
            System.Random rand = new System.Random();
            return rand.Next(min, max);
        }
    }
}

```

  1. Build the project to generate the DLL file along with its debug symbols.


## Debugging a DLL in Unity
To set up a debugging session for a DLL in Unity:
  1. Create a new project in Unity and copy your built .dll file (for example, `<project folder>/bin/Debug/DLLTest.dll`) into the Assets folder.
  2. Create a C# script called Test in the Assets folder.
  3. Replace its contents with a script that creates a new instance of the class you created in your DLL, uses its functions and displays the output in the **Console** window. For example, to create a test script for the DLL from the section above, copy the following code:

```
using UnityEngine;
using System.Collections;
using DLLTest;

public class Test : MonoBehaviour {

     void Start () {
        MyUtilities utils = new MyUtilities();
        utils.AddValues(2, 3);
        print("2 + 3 = " + utils.c);
     }
    
     void Update () {
        print(MyUtilities.GenerateRandom(0, 100));
     }
}

```

  1. Attach this script to a GameObject in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) and click Play.


Unity displays the output of the code from the DLL in the Console window
## Compiling unsafe C# code
[Unsafe C# code](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/unsafe) is code that is able to access memory directly. It is not enabled by default because the compiler can’t verify that it won’t introduce security risks.
You might want to use unsafe code to:
  * Access memory using pointers.
  * Allocate raw memory.
  * Call methods using pointers.


To enable support for compiling unsafe C# code go to **Edit** > **Project Settings** > **Player** > **Other Settings** and enable **Allow Unsafe Code**.
For more information, see [Microsoft’s documentation of unsafe code](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/unsafe-code).
## Additional resources
  * [Native plug-ins](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins-native.html)A platform-specific native code library that is created outside of Unity for use in Unity. Allows you can access features like OS calls and third-party code libraries that would otherwise not be available to Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Nativeplug-in)
  * [Plugins for desktop](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins-for-desktop.html)
  * [Native plug-in interface](https://docs.unity3d.com/6000.0/Documentation/Manual/native-plugin-interface.html)
  * [.NET profile support](https://docs.unity3d.com/6000.0/Documentation/Manual/dotnet-profile-support.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-in-inspector.html)
Import and configure plug-ins 
[](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins-native.html)
Native plug-ins
