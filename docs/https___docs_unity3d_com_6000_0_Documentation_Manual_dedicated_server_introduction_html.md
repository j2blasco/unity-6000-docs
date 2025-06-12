* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/dedicated-server-introduction.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Dedicated Server](https://docs.unity3d.com/6000.0/Documentation/Manual/dedicated-server.html)
  * Introduction to Dedicated Server


[](https://docs.unity3d.com/6000.0/Documentation/Manual/dedicated-server.html)
Dedicated Server
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dedicated-server-get-started.html)
Get started with Dedicated Server
# Introduction to Dedicated Server
Dedicated Server refers to a computer that’s optimized to run server applications.
The Dedicated Server [build target](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.html) is a sub-target of the three Desktop Platforms (Linux, macOS, and Windows) that’s optimized for running as a dedicated server. Using Dedicated Server build target, you can cut back on your server builds’ CPU, memory, and disk space requirements.
Server builds often contain unnecessary assets and compiled code for headless server processes. The build data might include artifacts such as audio files, textures, meshes, and **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader). In a multiplayer context, rendering and asset management processes occur unnecessarily when building and executing server runtimes.
The goal of the Dedicated Server build target is to reduce the resource demand of server builds, including the disk size, the size in memory, and the CPU usage. Most of the optimizations take place through [stripping code](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-stripping.html) and assets that aren’t necessary for a server build.
## Additional resources
  * [Desktop headless mode](https://docs.unity3d.com/6000.0/Documentation/Manual/desktop-headless-mode.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dedicated-server.html)
Dedicated Server
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dedicated-server-get-started.html)
Get started with Dedicated Server
