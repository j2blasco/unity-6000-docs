* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/BackgroundTasksWindow.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Unity's interface](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheEditor.html)
  * The Background Tasks window


[](https://docs.unity3d.com/6000.0/Documentation/Manual/StatusBar.html)
The status bar
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Console.html)
Console window
# The Background Tasks window
The Background Tasks window displays the progress of any running asynchronous tasks. For example, you can see the progress for [shader compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderCompileTargets.html), [lightmap](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmappers.html)A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap) baking, and [occlusion culling](https://docs.unity3d.com/6000.0/Documentation/Manual/OcclusionCulling.html)A process that disables rendering GameObjects that are hidden (occluded) from the view of the camera. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/OcclusionCulling.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Occlusionculling).
To open the Background Tasks window, do one of the following:
  * From the menu, select **Window** > **General** > **Progress**.
  * From the Unity Editor [status bar](https://docs.unity3d.com/6000.0/Documentation/Manual/StatusBar.html), click the global progress bar or the activity indicator (spinner).

![The Background Tasks Window](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/window-bg-tasks-overview.png) The Background Tasks Window
  1. ****Toolbar** A row of buttons and basic controls at the top of the Unity Editor that allows you to interact with the Editor in various ways (e.g. scaling, translation). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Toolbar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Toolbar)**: Provides options to [filter tasks](https://docs.unity3d.com/6000.0/Documentation/Manual/BackgroundTasksWindow.html#filtering-tasks-by-status) and [clear inactive tasks](https://docs.unity3d.com/6000.0/Documentation/Manual/BackgroundTasksWindow.html#clearing-inactive-tasks) from the list.
  2. **Task list** : Displays [progress information](https://docs.unity3d.com/6000.0/Documentation/Manual/BackgroundTasksWindow.html#task-information) about each task for the following:
     * Active tasks, including tasks that have stopped responding.
     * Some finished tasks. By default, Unity removes these from the list, but some are designed to stay in the list until you [clear them](https://docs.unity3d.com/6000.0/Documentation/Manual/BackgroundTasksWindow.html#clearing-inactive-tasks) manually.
     * Failed and cancelled tasks.


## Task information
Each entry in the Background Tasks window displays the following information about the task.
![Components of a background task entry](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/window-bg-tasks-task.png) Components of a background task entry **Screenshot label** | **Section** | **Displays**  
---|---|---  
1 | Task name/description | A name or short description for the task.  
2 | Progress bar | Indicates how close the task is to completion.  
  
If the task is indeterminate, because its progress is not measurable, the bar shows a small filled region that moves from side to side until the task is finished.  
3 | Percent complete | Shows how close the task is to completion, as a percentage.  
  
For indeterminate tasks, whose progress is not measurable, this area is empty.  
4 | Cancel | Click to cancel an active task.   
  
If the task cannot be cancelled, this icon does not appear.  
5 | Status | Optionally displays a short description of the current activity for an active task.   
  
When the task finishes, this area displays its final [status](https://docs.unity3d.com/6000.0/Documentation/Manual/BackgroundTasksWindow.html#viewing-task-status) (for example, finished, failed, or cancelled).  
6 | Time elapsed/remaining/total | When an active task takes longer than a few seconds, displays either the current time elapsed or the estimated time remaining.   
  
When the task finishes, this area displays the total time elapsed.  
### Subtasks
Some tasks spawn subtasks. The progress window displays an overall progress entry in the parent task (1), and a sub progress entry for each child task (2).
![Subtasks in the Background Tasks window](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/window-bg-tasks-subtasks.png) Subtasks in the Background Tasks window
Monitor subtasks to determine which part of a complex task takes the most time. This is useful for operations like lightmap baking, which can have hundreds of subtasks.
## View task status
Background tasks can have the following statuses:
**Status** | **Description** | **Icon**  
---|---|---  
Active | The task is running and reports progress as percent complete, or estimated time remaining. | None  
Indeterminate | The task is running and reports progress, but cannot determine how close it is to being complete. | None  
Finished | The task finished successfully | ![A check mark for a finished task]](../uploads/Main/CompletedTask@2x.png)  
(check mark)  
Unresponsive | The task has not reported any progress for five seconds. | None  
Cancelled | The task is no longer active because you cancelled it manually.  
  
Some tasks cannot be cancelled from the Background Tasks window. |  ![A warning symbol for a cancelled task](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/Warning@2x.png)  
(warning symbol)  
Failed | The task is no longer active because it failed |  ![An error symbol for a failed task](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/Error@2x.png)  
(error symbol)  
### Filter tasks by status
Use the filter options in the Background Tasks window toolbar to hide and show different types of tasks.
![Filter toggles in the Background Tasks window](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/window-bg-tasks-filters.png) Filter toggles in the Background Tasks window Filter option | Shows or hides  
---|---  
![A check mark for a finished task](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/CompletedTask@2x.png)  
(check mark) | Finished tasks  
![A warning symbol for a cancelled or unresponsive task](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/Warning@2x.png)  
(warning symbol) | Cancelled and unresponsive tasks  
![An error symbol for a failed task](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/Error@2x.png)  
(error symbol) | Failed tasks  
## Cancel active tasks
You can cancel some running tasks directly from the Background Tasks window. To cancel a running task click the **cancel** (**x**) icon.
## Clear inactive tasks
Click the **Clear inactive** button in the toolbar to remove all inactive tasks from the list.
Unity automatically clears most finished tasks from the list. However, some tasks are designed to stay in the list until you clear them manually.
Failed and cancelled tasks also stay in the list until you clear them.
To clear unresponsive tasks, you must cancel them first.
## View global progress
The Unity Editor [status bar](https://docs.unity3d.com/6000.0/Documentation/Manual/StatusBar.html) displays a global progress bar that shows the aggregate overall progress of all active tasks. It does not include finished, failed, or cancelled tasks.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/StatusBar.html)
The status bar
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Console.html)
Console window
