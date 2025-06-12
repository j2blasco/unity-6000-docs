* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JsonUtility.FromJson.html

#  [JsonUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JsonUtility.html).FromJson
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
public static T FromJson(string json); 
### Parameters
Parameter | Description  
---|---  
json | The JSON representation of the object.  
### Returns
**T** An instance of the object. 
### Description
Create an object from its JSON representation.
Internally, this method uses the Unity serializer; therefore the type you are creating must be supported by the serializer. It must be a plain class/struct marked with the Serializable attribute. Fields of the object must have types supported by the serializer. Fields that have unsupported types, as well as private fields or fields marked with the NonSerialized attribute, will be ignored.  
  
Only plain classes and structures are supported; classes derived from UnityEngine.Object (such as MonoBehaviour or ScriptableObject) are not. Note that classes derived from MonoBehaviour or ScriptableObject **can** be used with [JsonUtility.FromJsonOverwrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JsonUtility.FromJsonOverwrite.html) as an alternative.  
  
If the JSON representation is missing any fields, they will be given their default values (i.e. a field of type T will have value default(T) - it will not be given any value specified as a field initializer, as the constructor for the object is not executed during deserialization).  
  
If the input is null or empty, FromJson returns null.  
  
The versions of this method that take strings can be called from background threads. The versions that take a TextAsset must be called from the main thread.
```
using UnityEngine;  
  
[System.Serializable]
public class PlayerInfo
{
    public string name;
    public int lives;
    public float health;  
  
    public static PlayerInfo CreateFromJSON(string jsonString)
    {
        return JsonUtility.FromJson[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JsonUtility.FromJson.html)<PlayerInfo>(jsonString);
    }  
  
    // Given JSON input:
    // {"name":"Dr Charles","lives":3,"health":0.8}
    // this example will return a PlayerInfo object with
    // name == "Dr Charles", lives == 3, and health == 0.8f.
}

```

* * *
## Declaration
public static object FromJson(string json, Type type); 
### Parameters
Parameter | Description  
---|---  
json | The JSON representation of the object.  
type | The type of object represented by the Json.  
### Returns
**object** An instance of the object. 
### Description
Create an object from its JSON representation.
Internally, this method uses the Unity serializer; therefore the type you are creating must be supported by the serializer. It must be a plain class/struct marked with the Serializable attribute. Fields of the object must have types supported by the serializer. Fields that have unsupported types, as well as private fields or fields marked with the NonSerialized attribute, will be ignored.  
  
Only plain classes and structures are supported; classes derived from UnityEngine.Object (such as MonoBehaviour or ScriptableObject) are not. Note that classes derived from MonoBehaviour or ScriptableObject **can** be used with [JsonUtility.FromJsonOverwrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JsonUtility.FromJsonOverwrite.html) as an alternative.  
  
If the JSON representation is missing any fields, they will be given their default values (i.e. a field of type T will have value default(T) - it will not be given any value specified as a field initializer, as the constructor for the object is not executed during deserialization).  
  
The versions of this method that take strings can be called from background threads. The versions that take a TextAsset must be called from the main thread.
* * *
