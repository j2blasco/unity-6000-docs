* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorJsonUtility.ToJson.html

#  [EditorJsonUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorJsonUtility.html).ToJson
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
public static string ToJson(object obj); 
## Declaration
public static string ToJson(object obj, bool prettyPrint); 
### Parameters
Parameter | Description  
---|---  
obj | The object to convert to JSON form.  
prettyPrint | If true, format the output for readability. If false, format the output for minimum size. Default is false.  
### Returns
**string** The object's data in JSON format. 
### Description
Generate a JSON representation of an object.
This is similar to [JsonUtility.ToJson](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JsonUtility.ToJson.html), but it supports any engine object. The output is similar to the properties exposed via the [SerializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) API, or as found in the YAML-serialized form of the object.  
  
If the object contains fields with references to other Unity objects, those references are serialized by recording the asset guid and local file id for each reference. This string can be saved, then deserialized in another session of the Unity Editor, and the references are resolved correctly. However only objects that are located in an non-scene asset file can be referenced. References to objects within a scene, including the same scene, will not be serialized.  
  
Additional resources: [JsonUtility.ToJson](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JsonUtility.ToJson.html), [AssetDatabase.TryGetGUIDAndLocalFileIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.TryGetGUIDAndLocalFileIdentifier.html)
* * *
