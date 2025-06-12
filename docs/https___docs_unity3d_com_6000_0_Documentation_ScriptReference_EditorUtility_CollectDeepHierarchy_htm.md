* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.CollectDeepHierarchy.html

#  [EditorUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.html).CollectDeepHierarchy
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
public static Object[] CollectDeepHierarchy(Object[] roots); 
### Parameters
Parameter | Description  
---|---  
roots | Array of objects where the search will start.  
### Returns
**Object[]** Array of objects heirarchically attached to the search array. 
### Description
Collect all objects in the hierarchy rooted at each of the given objects.
This is most useful for linearizing entire GameObject hierarchies including all their components.  
Note that the traversal will not include assets referenced from within the hierarchy. For example, having a MeshFilter component in the hierarchy will not cause the referenced Mesh to be included in the resulting list.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class CollectHierarchyExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Create two GameObjects
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)  parent = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)();
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)  child = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)();
        Object[]    roots = new Object[] { parent };  
  
        // Name them
        parent.name = "Parent";
        child.name = "Child";  
  
        // Make one a child of the other.
        child.transform.parent = parent.transform;  
  
        // Collect entire hierarchy
        Object[] result = EditorUtility.CollectDeepHierarchy[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.CollectDeepHierarchy.html)(roots);  
  
        // Dump results.  Will log four objects to the console;
        // two GameObjects ("Parent" and "Child") and two Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html)
        // components (one belonging to "Parent" and one belonging to
        // "Child")
        foreach (Object obj in result)
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(obj);
    }
}

```

* * *
