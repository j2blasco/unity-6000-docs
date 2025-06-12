* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.NextVisible.html

#  [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).NextVisible
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
public bool NextVisible(bool enterChildren); 
### Description
Move to next visible property.
Additional resources: [Next](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.Next.html), [hasVisibleChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-hasVisibleChildren.html), [isExpanded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-isExpanded.html), [Reset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.Reset.html), [HideInInspector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideInInspector.html).
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Text;
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class SerializePropertyNextVisible : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    public bool m_SeeMe1;  
  
    [HideInInspector[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideInInspector.html)]
    public bool m_HideMe1;  
  
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    private bool m_SeeMe2;  
  
    [HideInInspector[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideInInspector.html)]
    public bool m_HideMe2;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) NextVisible Example")]
    static void TestNextOnCyclicGraph()
    {
        var scriptableObject = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<SerializePropertyNextVisible>();
        using (var serializedObject = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(scriptableObject))
        {
            var serializedProperty = serializedObject.GetIterator();  
  
            var sb = new StringBuilder();
            sb.AppendLine("Visible Properties:");  
  
            // Move from the root to the first visible property
            bool visitChild = true;
            serializedProperty.NextVisible(visitChild);  
  
            // Rest of scan stays at same level
            visitChild = false;
            do
            {
                // Note: some properties from the supporting Unity base objects are exposed
                // (and visible in the inspector), for example "m_Script".
                sb.AppendLine(serializedProperty.name);
            }
            while (serializedProperty.NextVisible(visitChild));  
  
            /*Expected output
            m_Script
            m_SeeMe1
            m_SeeMe2
            */
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(sb.ToString());
        }
    }
}

```

* * *
