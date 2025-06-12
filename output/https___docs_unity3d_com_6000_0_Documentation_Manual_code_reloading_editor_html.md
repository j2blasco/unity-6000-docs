* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/code-reloading-editor.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Compilation and code reload ](https://docs.unity3d.com/6000.0/Documentation/Manual/compilation-and-code-reload.html)
  * Code and scene reload on entering Play mode


[](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-restrictions.html)
Scripting restrictions
[](https://docs.unity3d.com/6000.0/Documentation/Manual/configurable-enter-play-mode.html)
Configuring how Unity enters Play mode
# Code and scene reload on entering Play mode
Authoring your application in Edit mode and then switching to Play mode to preview its runtime behavior is a core feature of iterative development in the Unity Editor. By default the Editor reloads both your code and **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) assets as part of the transition from Edit mode to Play mode. It’s important to understand what Unity reloads, why and when it does so, and how you can configure the reloading behavior. This helps you make informed trade-offs between development iteration time and the degree to which Play mode accurately reflects your built application’s performance.
**Topic** | **Description**  
---|---  
[Configuring how Unity enters Play mode](https://docs.unity3d.com/6000.0/Documentation/Manual/configurable-enter-play-mode.html) | Configure the Unity Editor to enter Play mode more quickly and improve your development iteration times.  
[Enter Play mode with domain reload disabled](https://docs.unity3d.com/6000.0/Documentation/Manual/domain-reloading.html) | Understand how disabling domain reload on enter Play mode affects your application state and how you can compensate for these effects in your code.  
[Enter Play mode with scene reload disabled](https://docs.unity3d.com/6000.0/Documentation/Manual/scene-reloading.html) | Understand how disabling scene reload on enter Play mode affects your application and how you can compensate for these effects in your code.  
[Details of disabling domain and scene reload](https://docs.unity3d.com/6000.0/Documentation/Manual/configurable-enter-play-mode-details.html) | Understand the work Unity performs during domain and scene reload and what’s skipped when they’re disabled.  
## Additional resources
  * [Script compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/script-compilation.html)
  * [Scripting back ends](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-restrictions.html)
Scripting restrictions
[](https://docs.unity3d.com/6000.0/Documentation/Manual/configurable-enter-play-mode.html)
Configuring how Unity enters Play mode
