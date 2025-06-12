* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil-disableShaderOptimization.html

#  [ShaderUtil](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderUtil.html).disableShaderOptimization
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
disableShaderOptimization; 
### Description
Disables shader optimization in the Editor.
When you set this to `true`, shader compilers don't optimize your shader code in the Editor's Scene view and Game view. This can greatly speed up the time it takes shaders to compile, but can also reduce rendering speed. The effect will depend on which shader compiler your platform uses - see [Shader compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-compilation.html).  
  
If you restart the Editor, this setting is reset to `false`.  
  
This setting doesn't affect your built application.
* * *
