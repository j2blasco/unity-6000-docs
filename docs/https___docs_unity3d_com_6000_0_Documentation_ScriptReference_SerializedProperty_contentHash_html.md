* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-contentHash.html

#  [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).contentHash
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
contentHash; 
### Description
Provides the hash value for the property. (Read Only)
You can use this to track if there has been any changes to the value at the property path (Additional resources: [SerializedProperty.propertyPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-propertyPath.html)).   
  
Please note that:   
-If the size of the property's content is smaller than or equal to 32 bits, then the content will be returned instead of a hash.   
-If the property path leads to an array or complex type, the hash will correspond to the entire content.   
-If the property is a field with [SerializeReference] attribute, or a compound type that contains such a field, then the content hashing doesn't include the content of the referenced object, instead it only hashes the reference id (Additional resources: [SerializedProperty.managedReferenceId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-managedReferenceId.html)).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class MyObject : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    public string myString = "answer to life the universe and everything";
    public string[] myStringArray = { "answer", "to", "life", "the", "universe", "and", "everything" };
    public int[] myIntArray = { 42, 442, 422, 4242 };  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Output contentHash from SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html)")]
    static void OutputContentHashFromSerializedProperty()
    {
        var scriptableObject = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<MyObject>();  
  
        using (var serializedObject = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(scriptableObject))
        {
            SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) serializedPropertyMyString = serializedObject.FindProperty("myString");
            SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) serializedPropertyMyStringArray = serializedObject.FindProperty("myStringArray");
            SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) serializedPropertyMyIntArray = serializedObject.FindProperty("myIntArray");  
  
            uint myStringHash = serializedPropertyMyString.contentHash;
            uint myStringArrayHash = serializedPropertyMyStringArray.contentHash;
            uint MyIntArrayHash = serializedPropertyMyIntArray.contentHash;  
  
            serializedPropertyMyString.stringValue = "new string";
            serializedPropertyMyIntArray.DeleteArrayElementAtIndex(1);  
  
            serializedObject.ApplyModifiedPropertiesWithoutUndo();  
  
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(string.Format("myString: before={0}, after={1}, changed={2}", myStringHash, serializedPropertyMyString.contentHash, myStringHash == serializedPropertyMyString.contentHash ? "no" : "yes"));
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(string.Format("myStringArrayHash: before={0}, after={1}, changed={2}", myStringArrayHash, serializedPropertyMyStringArray.contentHash, myStringArrayHash == serializedPropertyMyStringArray.contentHash ? "no" : "yes"));
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(string.Format("MyIntArrayHash: before={0}, after={1}, changed={2}", MyIntArrayHash, serializedPropertyMyIntArray.contentHash, MyIntArrayHash == serializedPropertyMyIntArray.contentHash ? "no" : "yes"));
        }
    }
}

```

* * *
