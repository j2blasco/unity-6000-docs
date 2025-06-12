* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-shadowNormalBias.html

#  [Light](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html).shadowNormalBias
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Light.html "Go to Light Component in the Manual")
shadowNormalBias; 
### Description
Shadow mapping normal-based bias.
Shadow caster surfaces are pushed inwards along their normals by this amount, to help prevent self-shadowing ("shadow acne") artifacts. Units of normal-based bias are expressed in terms of shadowmap texel size; typically values between 0.3-0.7 work well.  
  
Larger values prevent shadow acne better, at expense of making shadow shape smaller than the object actually is.  
  
Currently normal-based bias is only implemented for directional lights; it has no effect for other light types.  
  
Additional resources: [shadows](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-shadows.html), [shadowBias](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light-shadowBias.html) properties.
* * *
