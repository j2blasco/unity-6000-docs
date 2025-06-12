* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-creating-custom-modules.html

  * [Optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/analysis.html)
  * [Unity Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)
  * [Collect performance data](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-collect-data.html)
  * [Data visualization](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-visualizing-data.html)
  * [Customizing Profiler modules](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-customizing.html)
  * Creating Profiler modules


[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-customizing.html)
Customizing Profiler modules
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-customizing-details-view.html)
Creating Profiler module detail panels
# Creating Profiler modules
A **Profiler** A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler) module displays performance data from your system in the Profiler window.
You can create your own profiler module in one of the following ways:
  * [Use the Profiler Module Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-creating-custom-modules.html#Creating-custom-Profiler-module-editor).
  * [Create a `ProfilerModule` script](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-creating-custom-modules.html#creating-profiler-modules-code).


A custom module displays the counters you specified in code in the Profiler window chart view (A), and the counters appear as a list in the module details panel (B). 
![A custom Profiler module with custom data dsiplayed.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/Profiler_Tank_module.png) A custom Profiler module with custom data dsiplayed.
## Creating Profiler modules with the Profiler Module Editor
You can use Unity’s built-in [Profiler Module Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-module-editor.html) to create your own Profiler module. To collect data in your Profiler module, you must add at least one counter for the module to track. You can add both built-in Unity counters, or use the [`ProfilerCounter` API](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest?subfolder=/api/Unity.Profiling.ProfilerCounter-1.html) to [create your own counters](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-add-counters-code.html) to add to the module. The list of available counters appears in the **Available Counters** pane.
To create your own module:
  1. Open the Profiler window (**Window > Analysis > Profiler**).
  2. Select the Profiler Modules dropdown, then select the cog icon. The Profiler Module Editor opens.
  3. Select the **Add** button in the bottom left corner of the window. Unity then adds a new Profiler module to the list called **New Profiler Module.** To rename the module, click the text field and use your keyboard to set a name.
  4. Select the counters you want to display in the module from the **Available Counters** panel, then double click on them to add them to the module. To select multiple counters, hold Shift and click to select a range, or hold down Ctrl (Command on macOS) to select counters one at a time.
  5. To reorder the counters, drag them. You can only add a maximum of 10 counters to a module.
  6. Select the Save Changes button in the bottom right corner of the Profiler Module Editor window. Unity closes the window, and Unity displays the new module in the Profiler Window.


**Important:** If you don’t have any data loaded into the Profiler window, then any counters you’ve created don’t appear in the Available Counters pane when you load the Profiler Module Editor. To view custom counters, [capture or load some data](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-collect-data.html) that has your emitted counters in with the Profiler, and reopen the Profiler Module Editor.
![Profiler Module Editor with User counters listed.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/profiler-module-editor-user-counters.png) Profiler Module Editor with User counters listed.
## Creating Profiler modules in code
To create a Profiler module via code, you must create a new `ProfilerModule` script and define the module’s properties including the counters it displays, its name, and its icon.
To define a Profiler module, your script must do the following:
  1. Define a class derived from [`ProfilerModule`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Editor.ProfilerModule.html) in your project or package. In the following example, the class is called `TankEffectsProfilerModule`:
```
public class TankEffectsProfilerModule : ProfilerModule

```

  2. Assign the [`[ProfilerModuleMetadata]`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Profiling.Editor.ProfilerModuleMetadataAttribute.html) attribute to this class and specify the module’s display name in the attribute’s argument. In the following example, the display name is “Tank Effects”:
```
[ProfilerModuleMetadata("Tank Effects")] 

```

  3. Implement a constructor that has no parameter, and pass a list of chart counter descriptions to the base constructor. In the following example, the constructor with no parameter is `TankEffectsProfilerModule()`, the list of chart counter descriptors is `k_Counters`, and the base constructor is `base`:
```
static readonly ProfilerCounterDescriptor[] k_Counters = new ProfilerCounterDescriptor[]
{
    new ProfilerCounterDescriptor(GameStatistics.TankTrailParticleCountName, GameStatistics.TanksCategory),
    new ProfilerCounterDescriptor(GameStatistics.ShellExplosionParticleCountName, GameStatistics.TanksCategory),
    new ProfilerCounterDescriptor(GameStatistics.TankExplosionParticleCountName, GameStatistics.TanksCategory),
};
        
public TankEffectsProfilerModule() : base(k_Counters) { }

```



## Displaying a custom Profile module in the Profiler window
When you define your own Profiler module, the Profiler window automatically detects it. To view data in your Profiler module in the Profiler window:
  1. Connect the Profiler to your application. For more information, refer to [Profiling your application](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-profiling-applications.html).
  2. Run your application.


You can also run the Profiler when your application is in Play mode. However, if you profile an application in Play mode, the Profiler displays data that is not representative of how your application runs when you build it on a hardware device.
## Additional resources
  * [Collecting performance data](https://docs.unity3d.com/6000.0/Documentation/Manual/profiling-collect-data-introduction.html)
  * [Profiler modules introduction](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-modules-introduction.html)
  * [Profiler Module Editor reference](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-module-editor.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-customizing.html)
Customizing Profiler modules
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-customizing-details-view.html)
Creating Profiler module detail panels
