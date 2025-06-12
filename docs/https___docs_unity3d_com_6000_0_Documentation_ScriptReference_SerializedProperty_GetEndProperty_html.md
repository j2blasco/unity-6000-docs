* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.GetEndProperty.html

#  [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).GetEndProperty
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
public [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) GetEndProperty(); 
## Declaration
public [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) GetEndProperty(bool includeInvisible); 
### Description
Retrieves the SerializedProperty that defines the end range of this property.
It's the first property that's not a child or grandchild of this property. The end property can be used to iterate over all children of a property by using [EqualContents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.EqualContents.html).
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class GetEndPropertyExample : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    public Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) m_vector2 = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(1.0f, 2.0f);
    public bool m_bool = false;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) GetEndProperty Example")]
    static void Example()
    {
        GetEndPropertyExample obj = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<GetEndPropertyExample>();
        SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) serializedObject = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(obj);
        SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property = serializedObject.FindProperty("m_vector2");  
  
        // Visit the x, y values of the vector, stopping once m_bool is reached
        var endOfChildrenIteration = property.GetEndProperty();
        while (property.NextVisible(true) && !SerializedProperty.EqualContents[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.EqualContents.html)(property, endOfChildrenIteration))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(property.propertyPath + " : " + property.floatValue);
        }
    }
}

```

* * *
