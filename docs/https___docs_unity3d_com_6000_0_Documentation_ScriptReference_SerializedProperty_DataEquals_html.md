* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.DataEquals.html

#  [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).DataEquals
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
public static bool DataEquals([SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) x, [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) y); 
### Description
Compares the data for two SerializedProperties. This method ignores paths and SerializedObjects.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class SerializedPropertyDataEqualsExample : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    [Serializable]
    public struct SomeData
    {
        public string aStringValue;
        public float aFloatValue;
    }  
  
    [Serializable]
    public struct SomeOtherData
    {
        public string anotherStringValue;
        public float anotherFloatValue;
    }  
  
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    SomeData someData;
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    SomeOtherData[] otherDataArray;  
  
    static bool AreBothPropertiesEquals()
    {
        // Create an instance of the ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
        var testObject = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<SerializedPropertyDataEqualsExample>();
        // Set the first class to some values
        testObject.someData.aStringValue = "ThisValue";
        testObject.someData.aFloatValue = 5.1f;
        // Set the first array entry of the second class to the exact same values
        testObject.otherDataArray = new SomeOtherData[1];
        testObject.otherDataArray[0].anotherStringValue = "ThisValue";
        testObject.otherDataArray[0].anotherFloatValue = 5.1f;  
  
        var serializedObject = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(testObject);
        // Serialized property that refers to data from the first class
        var propertyOne = serializedObject.FindProperty("someData");
        // SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) that refers to data from the first entry of the second class array
        var propertyTwo = serializedObject.FindProperty("otherDataArray.Array.data[0]");
        // Compare data from each SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).
        bool result = SerializedProperty.DataEquals[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.DataEquals.html)(propertyOne, propertyTwo);  
  
        serializedObject.Dispose();
        DestroyImmediate(testObject);
        return result;
    }  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/SerializedPropertyDataEqualsExample")]
    static void TestMethod()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Are properties equals ? " + AreBothPropertiesEquals());
    }
}

```

* * *
