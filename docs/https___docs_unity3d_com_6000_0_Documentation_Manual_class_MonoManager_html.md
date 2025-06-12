* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-MonoManager.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Editor Features](https://docs.unity3d.com/6000.0/Documentation/Manual/EditorFeatures.html)
  * [Project Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)
  * Script Execution Order settings


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html)
Quality settings tab reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TagManager.html)
Tags and Layers
# Script Execution Order settings
Use the **Script Execution Order** settings to specify the relative order that Unity invokes the event functions of different [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) classes. For example, you can specify that Unity should run the event functions of your `Rotation` MonoBehaviour script before it runs those of your `MoveForward` MonoBehaviour script. 
The order applies to each category of event function separately, so Unity calls any [Awake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Awake.html) functions it needs to invoke during a frame in the specified order and, later, calls any [Update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Update.html) functions of active **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) in the same order.
You can adjust the script execution order in the Project Settings Inspector. Go to menu: **Edit** > **Project Settings** A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ProjectSettings), and then select the **Script Execution Order** category.
**Note:** If you assign multiple script types to multiple GameObjects, the script execution order specifies that all **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) of one type are executed before all scripts of another type, regardless of which GameObject they are attached to.
![The Script Execution Order section of the Project Settings window displays a list of script classes and their currently configured execution order values.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/ScriptExecSet.png) The Script Execution Order section of the Project Settings window displays a list of script classes and their currently configured execution order values.
Use the Plus (+) button to add scripts to the settings **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window and select the class name. To remove a script, use the Minus (-) button located to the right of each item in the list.
To specify the execution order, drag items in the list into the desired position or edit the order numbers of a class in the list. The assigned numbers express the relative order. Unity executes the list from top to bottom (from scripts with more negative order numbers to those with higher positive numbers). Unity executes any scripts not in the list during the **Default Time** slot, which occurs after any scripts with negative order numbers and before any scripts with positive order numbers.
The order numbers are arbitrary and do not represent any physical quantity. The Editor stores these values in the script metadata files. You can leave gaps between order numbers to help avoid extraneous file changes when you add or move other scripts in the list.
When multiple scenes are [loaded additively](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.LoadSceneMode.Additive.html), the configured script execution order is applied in full for one scene at a time. For example, if the configured execution order is `Script1` > `Script2` > `Script3`, Unity updates all instances of `Script1` in the first scene, then all instances of `Script2` in the first scene, then all instances of `Script3` in the first scene, before running any updates in the next scene.
If you prefer to specify the script execution order from code rather than configuring it in the Editor, you can do so by applying the `[DefaultExecutionOrder]` attribute to your MonoBehaviour-derived classes. For more information, refer to [DefaultExecutionOrder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DefaultExecutionOrder.html) in the Scripting API. 
**Note:** The execution order specified in the Script Execution Order settings window doesn’t affect the order of functions marked with the [RuntimeInitializeOnLoadMethod](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimeInitializeOnLoadMethodAttribute.html) attribute because you can’t specify an order for runtime initialization. Additionally, the script execution order doesn’t affect [OnDisable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnDisable.html) and [OnDestroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnDestroy.html) functions.
For information about when Unity invokes each of the different categories of event functions in a frame, refer to [order of execution for event functions](https://docs.unity3d.com/6000.0/Documentation/Manual/execution-order.html).
MonoManager
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html)
Quality settings tab reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TagManager.html)
Tags and Layers
