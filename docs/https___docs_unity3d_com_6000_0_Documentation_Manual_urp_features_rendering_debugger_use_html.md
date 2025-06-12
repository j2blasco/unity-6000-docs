* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-debugger-use.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Graphics performance and profiling in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-and-profiling-in-urp.html)
  * [Rendering Debugger in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-debugger.html)
  * Enable the Rendering Debugger in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-debugger.html)
Rendering Debugger in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-debugger-add-controls.html)
Add controls to the Rendering Debugger in URP
# Enable the Rendering Debugger in URP
The Rendering Debugger window is available in the following modes:
Mode | Platform | Availability | How to Open the Rendering Debugger  
---|---|---|---  
Editor | All | Yes (window in the Editor) | Select **Window > Analysis > Rendering Debugger**  
Play mode | All | Yes (overlay in the Game view) | On a desktop or laptop computer, press **LeftCtrl+Backspace** (**LeftCtrl+Delete** on macOS)  
On a console controller, press L3 and R3 (Left Stick and Right Stick)  
Runtime | Desktop/Laptop | Yes (only in Development builds) | Press **LeftCtrl+Backspace** (**LeftCtrl+Delete** on macOS)  
Runtime | Console | Yes (only in Development builds) | Press L3 and R3 (Left Stick and Right Stick)  
Runtime | Mobile | Yes (only in Development builds) | Use a three-finger double tap  
![The Rendering Debugger overlay in Play mode.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/rendering-debugger-play-mode.jpg) The Rendering Debugger overlay in Play mode.
To enable all the sections of the **Rendering Debugger** in your built application, disable **Strip Debug Variants** in **Project Settings > Graphics > URP Global Settings**. Otherwise, you can only use the [Display Stats](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-debugger-reference.html#display-stats) section.
To disable the runtime UI, use the [enableRuntimeUI](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@17.0/api/UnityEngine.Rendering.DebugManager.html#UnityEngine_Rendering_DebugManager_enableRuntimeUI) property.
**Note:** When using the **Rendering Debugger** window in the Development build, clear the **Strip Debug Variants** check box in **Project Settings > Graphics > URP Global Settings**.
##  Navigation at runtime
### Keyboard
Action | Control  
---|---  
**Change the current active item** | Use the arrow keys  
**Change the current tab** | Use the Page up and Page down keys (Fn + Up and Fn + Down keys respectively for MacOS)  
**Display the current active item independently of the debug window** | Press the right Shift key  
### Xbox Controller
Action | Control  
---|---  
**Change the current active item** | Use the Directional pad (D-Pad)  
**Change the current tab** | Use the Left Bumper and Right Bumper  
**Display the current active item independently of the debug window** | Press the X button  
### PlayStation Controller
Action | Control  
---|---  
**Change the current active item** | Use the Directional buttons  
**Change the current tab** | Use the L1 button and R1 button  
**Display the current active item independently of the debug window** | Press the Square button  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-debugger.html)
Rendering Debugger in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-debugger-add-controls.html)
Add controls to the Rendering Debugger in URP
