* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MetadataValue.html

# MetadataValue
struct in UnityEngine.Rendering
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
### Description
Contains a single metadata value for a batch.
A metadata value is a uint32 value tied to a DOTS-instanced property. Unity passes this metadata to the shader.
### Properties
Property | Description  
---|---  
[NameID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MetadataValue.NameID.html) | The name ID of the property that the metadata value is tied to. To specify a value for a property declared with UNITY_DOTS_INSTANCED_PROP(float4, Example), pass Shader.PropertyToID("Example") here.  
[Value](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.MetadataValue.Value.html) | Unity passes this uint32 value to the shader for this property. The value is shared between all instances in the batch.Usage example: provide a buffer address for the property.  
* * *
