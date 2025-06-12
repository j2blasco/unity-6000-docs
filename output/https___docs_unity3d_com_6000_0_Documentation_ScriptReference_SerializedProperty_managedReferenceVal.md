* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-managedReferenceValue.html

#  [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).managedReferenceValue
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
managedReferenceValue; 
### Description
The object assigned to a field with [SerializeReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeReference.html) attribute.
For use when [propertyType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-propertyType.html) is [SerializedPropertyType.ManagedReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.ManagedReference.html).   
  
  
  
The value object must be a type that is compatible with the base type of the managed reference field (that is, the managed reference field that the serialized property is referencing).  
  
Additional resources: [SerializeReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeReference.html), [propertyType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-propertyType.html), [SerializedPropertyType.ManagedReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.ManagedReference.html). 
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections.Generic;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using Object = UnityEngine.Object;  
  
public class SerializedPropertyManagedReferenceValueExample : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    [Serializable]
    public class Item[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.html)
    {
        public int m_data = 1;  
  
        public int DoCalculation()
        {
            // Could be querying some external data, or other calculation that cannot be
            // made entirely based on the local object state
            m_data++;
            return m_data * 2;
        }
    }  
  
    [SerializeReference[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeReference.html)]
    public Item[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.html) m_Item;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) ManagedReferenceValue Example1")]
    static void TestMethod1()
    {
        var scriptableObject = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<SerializedPropertyManagedReferenceValueExample>();
        var serializedObject = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(scriptableObject);  
  
        // Allocate and assign an object to the m_Item field via managedReferenceValue
        var referenceProperty = serializedObject.FindProperty("m_Item");
        referenceProperty.managedReferenceValue = new Item[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.html)();  
  
        // Change a value of the object's field
        referenceProperty.FindPropertyRelative("m_data").intValue = 99;  
  
        // Apply the change back to the "live" object
        serializedObject.ApplyModifiedProperties();  
  
        // Will print "Value of m_data: 99"
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Value of m_data: " + scriptableObject.m_Item.m_data);
    }  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) ManagedReferenceValue Example2")]
    static void TestMethod2()
    {
        var scriptableObject = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<SerializedPropertyManagedReferenceValueExample>();
        scriptableObject.m_Item = new Item[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.html)();  
  
        var serializedObject = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(scriptableObject);
        var referenceProperty = serializedObject.FindProperty("m_Item");  
  
        // The "live" referenced object can be accessed so we can call a method on it
        (referenceProperty.managedReferenceValue as Item[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Progress.Item.html)).DoCalculation();  
  
        // The serialized state inside the SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) is now out of data with the change
        // of m_data on the live object, but can be brought back in sync by calling Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
        var serializedDataValue = serializedObject.FindProperty("m_Item.m_data").intValue;
        serializedObject.Update();
        var updatedSerializedDataValue = serializedObject.FindProperty("m_Item.m_data").intValue;  
  
        // Will print: "Value of m_data before update: 1 and after update: 2"
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Value of m_data before update: " + serializedDataValue + " and after update: " + updatedSerializedDataValue);
    }
}

```

* * *
