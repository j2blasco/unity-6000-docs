* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SketchUpImportCamera.html

# SketchUpImportCamera
struct in UnityEditor
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
Structure to hold camera data extracted from a SketchUp file.
When importing a SketchUp file, Unity retrieves the current camera view the file is saved with and the camera view of all the scenes in the SketchUp file. The camera data of each Scene is stored in [SketchUpImportScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SketchUpImportScene.html)  
  
This can be extracted later from [SketchUpImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SketchUpImporter.html).
### Properties
Property | Description  
---|---  
[aspectRatio](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SketchUpImportCamera-aspectRatio.html) | Aspect ratio of the camera.  
[farPlane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SketchUpImportCamera-farPlane.html) | The near clipping plane distance.  
[fieldOfView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SketchUpImportCamera-fieldOfView.html) | Field of view of the camera.  
[isPerspective](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SketchUpImportCamera-isPerspective.html) | Indicate if the camera is using a perspective or orthogonal projection.  
[lookAt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SketchUpImportCamera-lookAt.html) | The position the camera is looking at.  
[nearPlane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SketchUpImportCamera-nearPlane.html) | The far clipping plane distance.  
[orthoSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SketchUpImportCamera-orthoSize.html) | The orthogonal projection size of the camera. This value only make sense if SketchUpImportCamera.isPerspective is false.  
[position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SketchUpImportCamera-position.html) | The position of the camera.  
[up](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SketchUpImportCamera-up.html) | Up vector of the camera.  
* * *
