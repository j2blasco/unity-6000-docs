* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideInInspector.html

# HideInInspector
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
Flags a variable to not appear in the Inspector.
By default, a serialized variable automatically appears in the Inspector, even if the variable is private. A variable with this attribute can be serialized and not display in the Inspector.  
  
Additional resources: [SerializedObject.forceChildVisibility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject-forceChildVisibility.html), [SerializedProperty.NextVisible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.NextVisible.html), [SerializedProperty.hasVisibleChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-hasVisibleChildren.html).
```
using UnityEngine;  
  
public class HideInInspectorExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // All these fields are serialized, but only c is visible in the inspector
    [HideInInspector[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideInInspector.html)]
    public int a = 5;  
  
    [HideInInspector[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideInInspector.html), SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    private int b = 3;  
  
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    private int c = 3;
}

```

* * *
