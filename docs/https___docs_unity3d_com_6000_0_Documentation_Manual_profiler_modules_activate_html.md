* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-modules-activate.html

  * [Optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/analysis.html)
  * [Unity Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)
  * [Collect performance data](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-collect-data.html)
  * [Data visualization](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-visualizing-data.html)
  * Activating and enabling Profiler modules


[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-modules-introduction.html)
Profiler modules introduction
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-customizing.html)
Customizing Profiler modules
# Activating and enabling Profiler modules
Profiler modules collect performance data about your application. For information about **Profiler** A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler) modules, refer to [Profiler modules introduction](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-modules-introduction.html).
Some Profiler modules have a large data collection overhead, such as the GPU, UI, and audio Profiler module. To prevent these modules from affecting your application’s performance, you can deactivate them. 
## Activating and deactivating Profiler modules
To activate or deactivate a module:
  1. Open the Profiler window (**Window > Analysis > Profiler**)
  2. Select the **Profiler Modules** dropdown
  3. Enable or disable the modules you want to display

![Profiler windows Profiler Modules dropdown menu](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/profiler-modules-dropdown.png) Profiler window’s Profiler Modules dropdown menu
Disabling a module removes the module from the window, stops the Profiler from collecting that module’s data, and lowers the overhead of the Profiler. When you enable a Profiler module, it starts collecting data, but shows no data for the period in which it wasn’t active.
**Important:** The [CPU Usage module](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerCPU.html) always collects data even when it’s not active, because other modules rely on it.
## Reordering Profiler modules
To change the order that the Profiler modules appear in the window, use the [Profiler Module Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-module-editor.html):
  1. Open the Profiler window (**Window > Analysis > Profiler**)
  2. Select the **Profiler Modules** dropdown
  3. Select the cog icon (⚙). The Profiler Module Editor opens in its own window.
  4. Click and drag the handle (≡) next to the module’s name to the desired order.
  5. Select **Save Changes** and close the window

![Profiler Module Editor window](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/profiler-module-editor-empty.png) Profiler Module Editor window
The Profiler window now displays the new order of Profiler modules.
## Additional resources
  * [Profiler modules introduction](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-modules-introduction.html)
  * [Navigating the Profiler window](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-window-navigating.html)
  * [Profiler window reference](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerWindow.html)
  * [Profiling your application](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-profiling-applications.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-modules-introduction.html)
Profiler modules introduction
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-customizing.html)
Customizing Profiler modules
