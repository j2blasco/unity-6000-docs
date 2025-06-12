* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.Update.html

#  [SerializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html).Update
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
## Declaration
public void Update(); 
### Description
Update serialized object's representation.
When a SerializedObject is constructed, the target objects are serialized, and the SerializeObject and SerializedProperty API provide read and write access to that serialized representation. If one or more of the target objects are changed, via another SerializedObject instance or direct writes to the target objects, then the SerializedObject internal serialized representation can get out of sync. Calling Update() will reserialize the target objects so that the SerializedObject reflects their latest state.  
  
Calling Update() will discard any locally modified properties that have not yet been applied.  
  
Additional resources: [SerializedObject.hasModifiedProperties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject-hasModifiedProperties.html), [SerializedObject.ApplyModifiedProperties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.ApplyModifiedProperties.html)
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Text;
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class SerializeObjectUpdate : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    public int m_Field = 1;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)")]
    static void UpdateExample()
    {
        var scriptableObject = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<SerializeObjectUpdate>();
        var sb = new StringBuilder();  
  
        using (var serializedObject = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(scriptableObject))
        {
            SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) field = serializedObject.FindProperty("m_Field");  
  
            // Change underlying object
            scriptableObject.m_Field = 2;  
  
            // SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) still thinks value is 1
            sb.Append($"SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) value before Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html): {field.intValue} ");  
  
            //hasModifiedProperties returns false because no changes have been made via SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) API
            sb.Append($"(SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) dirty: {serializedObject.hasModifiedProperties}), ");  
  
            // Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) so that SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) sees the new value
            serializedObject.Update();
            sb.AppendLine($"after Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html): {field.intValue}");  
  
            // Another scenario is when Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html) is called while there are pending changes in the SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)
            field.intValue = 3;
            sb.Append($"SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) value before Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html): {field.intValue} ");
            sb.Append($"(SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) dirty: {serializedObject.hasModifiedProperties}), ");  
  
            // Value reverts back to 2, because ApplyModifiedProperties was not called
            // and SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) has been put back in sync with the object's state
            serializedObject.Update();
            sb.AppendLine($"after Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html): {field.intValue}. (Dirty: {serializedObject.hasModifiedProperties})");  
  
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(sb.ToString());
        }
    }
}

```

* * *
