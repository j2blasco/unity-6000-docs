* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-managedReferenceId.html

#  [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).managedReferenceId
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
managedReferenceId; 
### Description
Id associated with a managed reference.
Available when [propertyType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-propertyType.html) is [SerializedPropertyType.ManagedReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.ManagedReference.html). If the reference is null then the Id is SerializeUtility.RefIdNull.  
  
Additional resources: [SerializeReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeReference.html), [managedReferenceValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-managedReferenceValue.html), [ManagedReferenceUtility.GetManagedReferenceIdForObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Serialization.ManagedReferenceUtility.GetManagedReferenceIdForObject.html).
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class SerializedPropertyManagedReferenceIdExample : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    [Serializable]
    public class Item[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.html)
    {
        public int m_data = 1;
    }  
  
    [SerializeReference[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeReference.html)]
    public Item[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.html) m_Item;  
  
    [SerializeReference[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeReference.html)]
    public Item[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.html) m_Item2;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) ManagedReferenceId Example")]
    static void TestMethod1()
    {
        var scriptableObject = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<SerializedPropertyManagedReferenceIdExample>();
        scriptableObject.m_Item = new Item[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.html)();  
  
        using (var serializedObject = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(scriptableObject))
        {
            var itemProperty = serializedObject.FindProperty("m_Item");
            var item2Property = serializedObject.FindProperty("m_Item2");  
  
            // Set m_Item2 to point to the same object as m_Item
            // Note: managedReferenceValue could also be used here, for the same result
            item2Property.managedReferenceId = itemProperty.managedReferenceId;  
  
            serializedObject.ApplyModifiedProperties();
        }  
  
        // Check the results back on the live object  
  
        //Will print "Value of m_Item2.m_data: 1"
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Value of m_Item2.m_data: " + scriptableObject.m_Item2.m_data);  
  
        // Prove that both fields point to the same object
        scriptableObject.m_Item.m_data = 2;  
  
        //Will print "Value of m_Item2.m_data: 2"
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Value of m_Item2.m_data: " + scriptableObject.m_Item2.m_data);
    }
}

```

* * *
