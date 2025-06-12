* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DefaultExecutionOrder.html

# DefaultExecutionOrder
class in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
### Description
Specifies the script execution order for a MonoBehaviour-derived class relative to other MonoBehaviour-derived types.
The `DefaultExecutionOrder` attribute offers a way to specify the execution order between different MonoBehaviour scripts from code, rather than through the [Project settings](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html) window in the Unity Editor. For more information on script execution order and configuring it in the Editor, refer to [Script Execution Order](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MonoManager.html) in the Manual.  
  
This attribute targets classes, but it only has an effect on classes that inherit from [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html).  
  
The integer value supplied as a parameter is equivalent to the integer values set in the **Script Execution Order** section of the **Project settings** window. The integer value assigned to a MonoBehaviour-derived type determines the execution order priority for script components of that type relative to the other MonoBehaviour scripts. Scripts are executed in order from lowest first to highest last, for example: -200, -100, -50, 50, 100, 200.  
  
**Note** : Use this attribute with caution. Execution order defined in code with `DefaultExecutionOrder` does not show in the **Script Execution Order** section of the Editor's **Project settings**. If you define an execution order for a MonoBehaviour-derived type in code with `DefaultExecutionOrder` but define a different value for the same type in the Editor's **Project settings** window, Unity uses the value defined in the Editor UI.  
  
See Also: [MonoBehaviour](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
```
using UnityEngine;
// Add this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
[DefaultExecutionOrder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DefaultExecutionOrder.html)(50)]
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
// This Start function will execute after the Start functions of any other MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html) scripts that
// have an execution order < 50 and before any with an execution order > 50. If you define a different
// execution order value for this ExampleClass in the Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)'s Script Execution Order settings, the
// value defined in Script Execution Order settings is the one applied at runtime.
    void Start()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Execution order 50");
    }
}

```

### Properties
Property | Description  
---|---  
[order](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DefaultExecutionOrder-order.html) | Integer which defines the execution priority order for a MonoBehaviour-derived class.  
### Constructors
Constructor | Description  
---|---  
[DefaultExecutionOrder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DefaultExecutionOrder-ctor.html) | Sets the script execution order for a MonoBehaviour-derived class to the value of the supplied integer parameter.  
* * *
