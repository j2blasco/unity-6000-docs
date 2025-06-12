* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ResourcePathAttribute.html

# ResourcePathAttribute
class in UnityEngine.Rendering
/
Inherits from:[Rendering.ResourcePathsBaseAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ResourcePathsBaseAttribute.html)
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
This attribute is used to describe what path to the asset should be used.
This is only used in the editor and doesn't have any effect at runtime. See [IRenderPipelineResources](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.IRenderPipelineResources.html) for usage.
### Constructors
Constructor | Description  
---|---  
[ResourcePathAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ResourcePathAttribute-ctor.html) | Creates a new ResourcePathAttribute for a single resource. Defaults to Project resource path location.  
### Inherited Members
### Properties
Property | Description  
---|---  
[isField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ResourcePathsBaseAttribute-isField.html) | Disambiguish array of 1 element and fields. As we don't store it at runtime, you cannot rely on this property for runtime operation.  
[location](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ResourcePathsBaseAttribute-location.html) | The lookup method. As we don't store it at runtime, you cannot rely on this property for runtime operation.  
[paths](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ResourcePathsBaseAttribute-paths.html) | Search paths. As we don't store it at runtime, you cannot rely on this property for runtime operation.  
* * *
