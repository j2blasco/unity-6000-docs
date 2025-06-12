* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-hasMultipleDifferentValues.html

#  [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).hasMultipleDifferentValues
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
hasMultipleDifferentValues; 
### Description
Does this property represent multiple different values due to multi-object editing? (Read Only)
Returns true when there are multiple target objects, and they do not all have the same value. Additional resources: [SerializedObject.targetObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject-targetObjects.html), [SerializedObject.SetIsDifferentCacheDirty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.SetIsDifferentCacheDirty.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class SerializePropertyHasMultipleDifferentValuesExample : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    public int m_Matching;
    public int m_Different;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) hasMultipleDifferentValues Example")]
    static void HasMultipleDifferentValuesExample()
    {
        var instance1 = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<SerializePropertyHasMultipleDifferentValuesExample>();
        instance1.m_Matching = 1;
        instance1.m_Different = 1;  
  
        var instance2 = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<SerializePropertyHasMultipleDifferentValuesExample>();
        instance2.m_Matching = 1;
        instance2.m_Different = 2;  
  
        using (var serializedObject = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(new ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)[] { instance1, instance2 }))
        {
            var matchingProperty = serializedObject.FindProperty("m_Matching");
            var differentProperty = serializedObject.FindProperty("m_Different");  
  
            // Outputs
            //m_Matching  value: 1, matching: True
            //m_Different value: 1, matching: False
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"m_Matching  value: {matchingProperty.intValue}, matching: {!matchingProperty.hasMultipleDifferentValues}\n" +
                $"m_Different value: {differentProperty.intValue}, matching: {!differentProperty.hasMultipleDifferentValues}");
        }
    }
}

```

* * *
