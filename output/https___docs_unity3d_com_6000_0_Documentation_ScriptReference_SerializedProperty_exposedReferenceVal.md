* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-exposedReferenceValue.html

#  [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).exposedReferenceValue
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
exposedReferenceValue; 
### Description
A reference to another Object in the Scene. This reference is resolved in the context of the SerializedObject containing the SerializedProperty.
Additional resources: [ExposedReference<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExposedReference_1.html), [SerializedPropertyType.ExposedReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.ExposedReference.html), [SerializedObject.context](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject-context.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class SerializedPropertyTest : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Object mComponent1;
    public Object mComponent2;  
  
    void Start()
    {
        var timeline = Resources.Load[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.Load.html)("myTimeline");
        var so1 = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(timeline, mComponent1);
        var so2 = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(timeline, mComponent2);  
  
        var theCamera = so1.FindProperty("sceneCamera").exposedReferenceValue;
        var anotherCamera = so2.FindProperty("sceneCamera").exposedReferenceValue;
    }
}

```

In this example, the same asset is loaded into two different contexts, `mComponent1` and `mComponent2`. The same object (called “sceneCamera”) in each context resolves to a different reference to a different Camera Object.
* * *
