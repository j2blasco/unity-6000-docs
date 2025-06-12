* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-depth.html

#  [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).depth
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
depth; 
### Description
Nesting depth of the property. (Read Only)
Additional resources: [propertyPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-propertyPath.html).
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Text;
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class SerializePropertyDepthExample : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    // Declare fields to demonstrate data at different depths
    public int m_depth0;  
  
    [Serializable]
    public struct Nested
    {
        public int m_depth1;  
  
        [Serializable]
        public struct NestedInNested
        {
            public int m_depth2;
            public Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) m_vectorDepth2; // Contains x,y at depth 3
        };
        public NestedInNested m_Nested1;
    };
    public Nested m_Nested0;
    public bool m_boolDepth0;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) depth Example")]
    static void DepthExample()
    {
        var scriptableObject = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<SerializePropertyDepthExample>();  
  
        using (var serializedObject = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(scriptableObject))
        {
            var report = new StringBuilder();  
  
            var iterator = serializedObject.FindProperty("m_depth0");  
  
            const bool visitChildren = true;
            do
            {
                report.AppendLine($"Found {iterator.propertyPath} (depth {iterator.depth})");
            }
            while (iterator.Next(visitChildren));  
  
            //Output:
            //Found m_depth0 (depth 0)
            //Found m_Nested0 (depth 0)
            //Found m_Nested0.m_depth1 (depth 1)
            //Found m_Nested0.m_Nested1 (depth 1)
            //Found m_Nested0.m_Nested1.m_depth2 (depth 2)
            //Found m_Nested0.m_Nested1.m_vectorDepth2 (depth 2)
            //Found m_Nested0.m_Nested1.m_vectorDepth2.x (depth 3)
            //Found m_Nested0.m_Nested1.m_vectorDepth2.y (depth 3)
            //Found m_boolDepth0 (depth 0)
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(report.ToString());
        }
    }
}

```

* * *
