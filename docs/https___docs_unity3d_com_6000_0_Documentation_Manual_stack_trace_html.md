* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/stack-trace.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Debugging and diagnostics](https://docs.unity3d.com/6000.0/Documentation/Manual/debugging-and-diagnostics.html)
  * Stack trace logging


[](https://docs.unity3d.com/6000.0/Documentation/Manual/log-files.html)
Log files reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/roslyn-analyzers.html)
Roslyn analyzers and source generators
# Stack trace logging
Unity Console messages and log files can include detailed stack trace information. The console also links to the line of code that generated the message. This is useful when you want to identify the line, method, or sequence of function calls that caused the log entry to appear.
**Tip:** Another way to inspect your code is to [attach a debugger](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-debugging.html) to the Editor or your built player.
## Stack trace for managed and unmanaged code
Unity can provide stack trace information for both managed and unmanaged code:
  * **Managed code:** Managed DLLs or C# **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) running in Unity. These can be scripts that ship with Unity, custom scripts that you write, third-party scripts included with an **Asset store** A growing library of free and commercial assets created by Unity and members of the community. Offers a wide variety of assets, from textures, models and animations to whole project examples, tutorials and Editor extensions. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStore.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AssetStore) **plug-in** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in), or any other C# script that runs in the engine.
  * **Unmanaged code:** Native Unity engine code, or code from a native plugin running directly on your machine or on a target build platform. Unmanaged code is usually compiled from C or C++ code. You can only access it if you have the original source code of the native binary. Typically, you will use stack trace for unmanaged code only if you need to determine whether an error is caused by your code or the engine code, and which part of the engine code.


Unity offers three stack trace options:
  * **None:** Unity doesn’t output stack trace information.
  * **ScriptOnly:** Unity outputs stack trace information only for managed code. This is the default option.
  * **Full:** Unity outputs stack trace information for both managed and unmanaged code.


## Stack trace resource requirements
Resolving a stack trace, especially a full stack trace, is a resource-intensive operation. Some best practices for stack traces include:
  * Use stack traces only to debug. Do not deploy an application to users with stack trace enabled.
  * Limit the type of messages that display a stack trace. For example, consider using stack trace only for exceptions and warnings.


## Setting the stack trace type
**Note:** The stack trace option is a build setting and affects the built player. It is not a view preference in the Editor.
To specify how much detail to include in the stack trace, you can use the scripting API or the Editor:
  * To control stack trace logging through the scripting API, use [Application.SetStackTraceLogType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.SetStackTraceLogType.html). You can use the API to change the stack trace setting of a player before it’s built, or while it’s running.
  * To use the Console, select the Console menu button, then: 
    * To select the same stack trace option for all Console message types, select **Stack Trace Logging** > **All**.
    * To select a stack trace option for just one of the Console message types, select **Stack Trace Logging** > **[MESSAGE TYPE]**. Rebuild your player with the new setting.
  * To use the Player Settings window, select **Edit** > **Project Settings** > **Player** > **Other Settings**. Rebuild your player with the new setting.

![Stack trace logging options from the Console. This example shows the options for Exception.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/StackTraceInConsole.png) Stack trace logging options from the Console. This example shows the options for Exception.
## Open source files from the stack trace output
The full text of a message includes references to specific lines in code files with links. Click any link to open the file in your IDE at the referenced line.
## Find the output log file of a built application
Built applications do not output to the Console. To see the stack trace, [use the application’s log file](https://docs.unity3d.com/6000.0/Documentation/Manual/log-files.html).
## Additional resources
  * [Console window](https://docs.unity3d.com/6000.0/Documentation/Manual/Console.html)A Unity Editor window that shows errors, warnings and other messages generated by Unity, or your own scripts. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Console.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Consolewindow)
  * [Log files](https://docs.unity3d.com/6000.0/Documentation/Manual/log-files.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/log-files.html)
Log files reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/roslyn-analyzers.html)
Roslyn analyzers and source generators
