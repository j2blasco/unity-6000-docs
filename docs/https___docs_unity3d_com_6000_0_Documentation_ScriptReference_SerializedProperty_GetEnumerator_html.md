* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.GetEnumerator.html

#  [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).GetEnumerator
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
public IEnumerator GetEnumerator(); 
### Description
Retrieves an iterator for enumerating over the visible child properties of the current property. If the property is an array it will enumerate over the array elements.
Additional resources: [NextVisible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.NextVisible.html), [GetEndProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.GetEndProperty.html), [GetArrayElementAtIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.GetArrayElementAtIndex.html)
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class EnumerateExample : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) m_vector3 = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(1.0f, 2.0f, 3.0f);
    public int m_anotherField = 2;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) GetEnumerator Example")]
    static void Example()
    {
        EnumerateExample obj = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<EnumerateExample>();
        SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) serializedObject = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(obj);
        SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property = serializedObject.FindProperty("m_vector3");  
  
        // Visit the x, y, z values of the vector, stopping once m_anotherField is reached
        var enumerator = property.GetEnumerator();
        while (enumerator.MoveNext())
        {
            property = enumerator.Current as SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html);
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(property.propertyPath + " : " + property.floatValue);
        }
    }
}

```

* * *
