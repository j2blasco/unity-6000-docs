* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-module-editor.html

  * [Optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/analysis.html)
  * [Unity Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)
  * [Collect performance data](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-collect-data.html)
  * [Data visualization](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-visualizing-data.html)
  * [Customizing Profiler modules](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-customizing.html)
  * Profiler Module Editor reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-customizing-details-view.html)
Creating Profiler module detail panels
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-cpu.html)
CPU performance data
# Profiler Module Editor reference
The **Profiler** A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler) Module Editor is a tool you can use to add your own custom modules to the Unity Profiler window. You can also add built-in counters to modules, or use the runtime API to add your own custom counters to modules. For information on how to implement your own counters, refer to [Adding profiler counters to your code](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-add-counters-code.html).
![The Profiler Module Editor window, with a new module selected](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/profiler-module-editor-user-counters.png) The Profiler Module Editor window, with a new module selected
To use the Profiler Module Editor, open the Profiler Window (**Window > Analysis > Profiler**) and then select the Profiler Modules dropdown.
Select the gear icon, and the **Profiler Module Editor** window opens. 
## Profiler Module Editor panels
Property | Description  
---|---  
**Profiler Modules** | Contains all the available modules you can add to the Profiler Window. Built-in modules are greyed-out in the list, indicating that you can’t edit their contents. You can drag and drop the modules to reorder their appearance in the Profiler window. When you create your own custom Profiler Module, it also appears in this list.  
**Add** | Select Add to add a custom Profiler module to the list. The following panels appear:  
**Profiler Module information pane** | Set a name for the Profiler module. Also lists the counters added to the custom module.  
**Available Counters** | Lists all available counters that you can add to a custom module. This list includes in-built Unity counters, and any custom counters you’ve added to your code.  
## Additional resources
  * [Profiler modules introduction](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-modules-introduction.html)
  * [Creating Profiler modules](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-creating-custom-modules.html)
  * [Adding profiler counters to your code](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-add-counters-code.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-customizing-details-view.html)
Creating Profiler module detail panels
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-cpu.html)
CPU performance data
