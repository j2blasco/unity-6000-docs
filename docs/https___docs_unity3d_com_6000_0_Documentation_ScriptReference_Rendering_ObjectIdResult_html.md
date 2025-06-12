* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ObjectIdResult.html

# ObjectIdResult
class in UnityEngine.Rendering
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
The results of an ObjectIdRequest, stored in ObjectIdRequest._result, containing the [ObjectIdResult.idToObjectMapping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ObjectIdResult-idToObjectMapping.html) that is needed to interpret the color-encoded object IDs that are rendered in the ObjectIdRequest._destination RenderTexture.
Please see [ObjectIdRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ObjectIdRequest.html) for further information and examples on submitting and using the results of this request.  
  
Additional resources: [ObjectIdRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ObjectIdRequest.html).
### Properties
Property | Description  
---|---  
[idToObjectMapping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ObjectIdResult-idToObjectMapping.html) |  An array of Objects that can be used to deterimine the object at each pixel in ObjectIdRequest._destination, first by decoding colors from ObjectIdRequest._destination to an index using ObjectIdResult.DecodeIdFromColor, and then by looking up this index in this array.   
### Static Methods
Method | Description  
---|---  
[DecodeIdFromColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ObjectIdResult.DecodeIdFromColor.html) |  A utility function that can be used to decode colors from ObjectIdRequest._destination to an index that can then be looked up in ObjectIdResult._idToObjectMapping.   
* * *
