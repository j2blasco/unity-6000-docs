* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.GetGPUProjectionMatrix.html

#  [GL](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.html).GetGPUProjectionMatrix
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
public static [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) GetGPUProjectionMatrix([Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) proj, bool renderIntoTexture); 
### Parameters
Parameter | Description  
---|---  
proj | Source projection matrix.  
renderIntoTexture | Will this projection be used for rendering into a RenderTexture?  
### Returns
**Matrix4x4** Adjusted projection matrix for the current graphics API. 
### Description
Compute GPU projection matrix from camera's projection matrix.
In Unity, projection matrices follow OpenGL convention. However on some platforms they have to be transformed a bit to match the native API requirements. Use this function to calculate how the final projection matrix will be like. The value will match what comes as `UNITY_MATRIX_P` matrix in a shader.  
  
The `renderIntoTexture` value should be set to true if you intend to render into a [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) with this projection matrix. On some platforms it affects how the final matrix will look like.  
  
Additional resources: [Camera.projectionMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-projectionMatrix.html), [Matrix4x4.Perspective](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Perspective.html), [Platform differences](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PlatformDifferences.html), [Built-in shader variables](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-UnityShaderVariables.html).
* * *
