* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.CameraDescription.TryGetProperty.html

#  [CameraDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.CameraDescription.html).TryGetProperty
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
public bool TryGetProperty(string propertyName, out float value); 
## Declaration
public bool TryGetProperty(string propertyName, out [Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) value); 
## Declaration
public bool TryGetProperty(string propertyName, out string value); 
## Declaration
public bool TryGetProperty(string propertyName, out int value); 
### Parameters
Parameter | Description  
---|---  
propertyName | Name of the property.  
value | The retrieved value.  
### Returns
**bool** Returns true if the property exists on the camera. Returns false otherwise. 
### Description
Retrieves the value of a specified camera property.
* * *
