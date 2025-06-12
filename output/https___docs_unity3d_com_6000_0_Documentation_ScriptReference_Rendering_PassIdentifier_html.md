* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PassIdentifier.html

# PassIdentifier
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
Represents an identifier of a specific Pass in a Shader.
Additional resources: [Shader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html), [ShaderUtil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.html), [Pass](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Pass.html).
### Properties
Property | Description  
---|---  
[PassIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PassIdentifier.PassIndex.html) | The index of the pass within the subshader (Read Only).  
[SubshaderIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PassIdentifier.SubshaderIndex.html) | The index of the subshader within the shader (Read Only).  
### Constructors
Constructor | Description  
---|---  
[PassIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PassIdentifier-ctor.html) | Constructs a new PassIdentifier with the given subshaderIndex and passIndex.  
### Operators
Operator | Description  
---|---  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PassIdentifier-operator_ne.html) | Returns true if the pass identifiers are not the same. Otherwise, returns false.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.PassIdentifier-operator_eq.html) | Returns true if the pass identifiers are the same. Otherwise, returns false.  
* * *
